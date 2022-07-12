# capstone_isb


### Installing miniconda/light version of anaconda 💁🏽‍♀️
- [Info + details](https://docs.conda.io/en/latest/miniconda.html)

### Commands to install the packages via conda/ env activation ✍️
```shell
conda env create --file environment.yml
```
```shell
conda activate capstone
```
```shell
conda list
```
```shell
conda info
```
```shell
conda deactivate
```
### Installing the analysis_framework package in local ⬇️
```shell
pip install -e .
```

### Info how to make best use of the workflow ⏯
- Clone the repo
- Create the env using the above commands 
- Install the package 
- All the tests goes into the `tests` directory 
- Any test experiments eg- `Data wraggling/inital exploration notebooks` goes under `experiments` directory
- All modelling and related details into `analysis_framework`, create subdirectories as required 
- Under forecasting_framework there are three submodules `utils`, `model`, `data` 
  - `utils` reusable code components
  - `model` all modelling aspects (**python scripts only**)
  - `data` pipepine and raw data

### About pre-commit-hooks and activating 🔌
Just like the name suggests, precommit-hooks are designed to format the code based on PEP standards before committing. [More details 🗒](https://pre-commit.com/)
```python
pip install pre-commit
pre-commit install

"""---commit your changes---
- check for errors, hooks format the code by deafult
- add the files
- commit it again
- push the changes 
"""
```

### Data pipeline 🛠

- Built using `Dagster`, an open source orchestration tool 

**Commands to trigger the pipeline**
- Command to run the pipeline from root `capstone_isb`
```shell
python analysis_framework/pipeline/process.py
```
- Command to view the dagit UI
```shell
dagit -f analysis_framework/pipeline/process.py
```
![Dagit UI](/experiments/outputs/pipeline_dagit.png)

### Dashboard

- Tools used - Panel, Holoviews 
- Main files `app.py` (panel serve requirements and layout components) and `base.py` (contains all the logic)
- Command to trigger the dashboard (subject to change) - `python analysis_framework/dashboard/app.py`

### How to contribute to the repo 🤔
- Create a separate branch for your usecase 
- Raise PR (**DO NOT** commit to main)


#### Meeting 📞
- 23rd April 2022 (9:30 PM) [Zoom link to be updated]

Topic: Capstone Project Selection

Time: Apr 23, 2022 09:30 PM India

Join Zoom Meeting
https://ISB.zoom.us/j/5046859164?pwd=MlBVYTZBenJYZmhXcWVvWGc0NXB6dz09

Meeting ID: 504 685 9164
Passcode: 874071
