# Python for Neuroscience — a 12-session mini-course

A free, short course that takes you from your first variable to a real analysis of open fMRI data. Each notebook is one session of roughly ten minutes. Everything runs in your browser on Google Colab with no installation.

## The sessions

| # | Session | Open in Colab | Video |
|---|---------|---------------|-------|
| 1 | Why Python for Neuroscience? | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/01_why_python_for_neuroscience.ipynb) | [![YouTube](https://img.shields.io/badge/YouTube-Watch-red?logo=youtube&logoColor=white)](https://youtu.be/a3dNow_hkXw?si=vX_5FJaUUAgv6xGa) |
| 2 | Variables, Types and Arithmetic | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/02_variables_types_arithmetic.ipynb) | [![YouTube](https://img.shields.io/badge/YouTube-Watch-red?logo=youtube&logoColor=white)](https://youtu.be/K3fknG_5jPY?si=SCvYtrZpWixaLQeS) |
| 3 | Control Flow and Functions | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/03_control_flow_and_functions.ipynb) | [![YouTube](https://img.shields.io/badge/YouTube-Watch-red?logo=youtube&logoColor=white)](https://youtu.be/L0z1OBtBk5I?si=l84A9XS0Cz14ja8i) |
| 4 | Lists, Dictionaries and Tuples | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/04_lists_dicts_tuples.ipynb) | [![YouTube](https://img.shields.io/badge/YouTube-Watch-red?logo=youtube&logoColor=white)](https://youtu.be/r0kG0r46Vxg?si=2OxJ0C0_gu0vJadV) |
| 5 | NumPy Fundamentals | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/05_numpy_fundamentals.ipynb) | [![YouTube](https://img.shields.io/badge/YouTube-Watch-red?logo=youtube&logoColor=white)](https://youtu.be/p68fenO7HnA) |
| 6 | pandas and Tabular Data | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/06_pandas_fundamentals.ipynb) | [![YouTube](https://img.shields.io/badge/YouTube-Watch-red?logo=youtube&logoColor=white)](https://youtu.be/DbCYgPWw8UE) |
| 7 | Plotting with Matplotlib and Seaborn | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/07_plotting.ipynb) | — |
| 8 | Signal Processing: Sampling and Filtering | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/08_signal_processing.ipynb) | — |
| 9 | Statistics for Neuroscience | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/09_statistics.ipynb) | — |
| 10 | Brain Networks and Graph Theory | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/10_brain_networks.ipynb) | — |
| 11 | Capstone Part 1: Real Data In | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/11_capstone_real_data.ipynb) | — |
| 12 | Capstone Part 2: Analyse and Conclude | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/saeedrafsharx/python-for-neuroscience/blob/main/notebooks/12_capstone_analyse_conclude.ipynb) | — |

## How it fits together

Sessions 1 to 4 are Python itself, taught with neuroscience examples from the first line.

Sessions 5 to 9 build on one synthetic signal, created by `generate_toy_signal()` in session 5 and reused after that. It is a sine wave plus noise, and it is labelled as a toy every time it appears so nobody mistakes it for a recording.

Sessions 10 to 12 move to networks and then to real data. The capstone uses the open [development fMRI dataset](https://osf.io/5hju4/) distributed with `nilearn`: children and adults watching a short film in the scanner. Session 12 reproduces a well-replicated developmental result, that within-network default mode connectivity is stronger in adults than in children.

## Running the notebooks

**On Colab.** Click any badge above. Nothing to install.

**Locally.**

```bash
git clone https://github.com/saeedrafsharx/python-for-neuroscience.git
cd python-for-neuroscience
pip install -r requirements.txt
jupyter lab notebooks/
```

## What is in `data/`

| File | What it is |
|------|------------|
| `one_subject_timeseries.csv` | 39 region time series from one participant. Used for the demo in session 1 and as a fallback in session 11. |
| `dev_fmri_timeseries.npz` | 50 participants (25 children, 25 adults), 168 timepoints, 39 regions. The session 12 dataset. |
| `participants.csv` | Participant id, age, group. |
| `msdl_regions.csv` | The 39 MSDL atlas regions, their network membership and coordinates. |

All of it is derived from the public nilearn dataset by `scripts/prepare_capstone_data.py`. Extracting the time series for 50 people takes a few minutes, which is why it is cached here rather than run live. Delete the folder and rerun the script to rebuild it from scratch.

## If you fork or rename this repo

Notebooks 1 and 12 load data over the network when they are run on Colab. They build the URL from a constant near the top:

```python
REPO_RAW = "https://raw.githubusercontent.com/saeedrafsharx/python-for-neuroscience/main/data/"
```

Change that line to point at your own repo. When the notebook is run locally it uses `../data/` instead and ignores the URL.

## Licence

Notebooks and text: CC BY 4.0. Code: MIT. The fMRI dataset keeps its own licence from the original authors.
