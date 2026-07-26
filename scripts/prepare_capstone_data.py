"""Build the cached dataset used by notebooks 1, 11 and 12.

Downloads the nilearn 'development fMRI' dataset (children watching a movie,
plus adult controls), extracts one time series per MSDL atlas region, and
saves everything as small plain files so the live sessions never wait on a
download or a masker.

Run once:  python prepare_capstone_data.py
"""

import os
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

from nilearn import datasets
from nilearn.maskers import NiftiMapsMasker

N_CHILD = 25
N_ADULT = 25
OUT = "data"
os.makedirs(OUT, exist_ok=True)

print("fetching atlas ...")
atlas = datasets.fetch_atlas_msdl()
labels = list(atlas.labels)
networks = list(atlas.networks)
coords = np.asarray(atlas.region_coords)

pd.DataFrame(
    {
        "region": labels,
        "network": networks,
        "x": coords[:, 0],
        "y": coords[:, 1],
        "z": coords[:, 2],
    }
).to_csv(f"{OUT}/msdl_regions.csv", index=False)

print("fetching fMRI ...")
kids = datasets.fetch_development_fmri(n_subjects=N_CHILD, age_group="child")
adults = datasets.fetch_development_fmri(n_subjects=N_ADULT, age_group="adult")
func_all = list(kids.func) + list(adults.func)
conf_all = list(kids.confounds) + list(adults.confounds)
pheno = pd.concat([pd.DataFrame(kids.phenotypic), pd.DataFrame(adults.phenotypic)],
                  ignore_index=True)

masker = NiftiMapsMasker(maps_img=atlas.maps, standardize="zscore_sample", verbose=0)

series, rows = [], []
for func, conf, (_, meta) in zip(func_all, conf_all, pheno.iterrows()):
    ts = masker.fit_transform(func, confounds=conf)
    series.append(ts.astype(np.float32))
    rows.append(
        {
            "participant_id": meta["participant_id"],
            "age": float(meta["Age"]),
            "group": meta["Child_Adult"],
            "n_timepoints": ts.shape[0],
        }
    )
    print("  ", meta["participant_id"], meta["Child_Adult"], ts.shape)

n_t = min(s.shape[0] for s in series)
print("trimming all subjects to", n_t, "timepoints")
stack = np.stack([s[:n_t] for s in series])  # subjects x time x regions

parts = pd.DataFrame(rows)
parts.to_csv(f"{OUT}/participants.csv", index=False)
np.savez_compressed(
    f"{OUT}/dev_fmri_timeseries.npz",
    timeseries=stack,
    participant_id=parts["participant_id"].to_numpy(),
    group=parts["group"].to_numpy(),
    age=parts["age"].to_numpy(),
    regions=np.array(labels),
    networks=np.array(networks),
)

# single-subject CSV used by notebook 1 and notebook 11
one = parts.index[parts["group"] == "adult"][0]
df = pd.DataFrame(stack[one], columns=labels)
df.insert(0, "time_s", np.arange(n_t) * 2.0)
df.to_csv(f"{OUT}/one_subject_timeseries.csv", index=False)
print("notebook-1 subject:", parts.loc[one, "participant_id"])

print(parts["group"].value_counts())
print("saved to", OUT)
