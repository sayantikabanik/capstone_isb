# Capstone project : ISB <> Peakhealth

### Demo link 
[Click to view the demo ](https://www.canva.com/design/DAFJrdvMG4Y/lMlZ51AY9niIN_5QBLOBQQ/watch?utm_content=DAFJrdvMG4Y&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

### How to contribute to the repo 🤔
- Create a separate branch for your usecase 
- Rebase with main branch
- Raise PR (**DO NOT** commit to main)

### Info how to make best use of the workflow ⏯
- Clone the repo
- Create the env using the above commands 
- Install the package 
- All the tests goes into the `tests` directory 
- Any test experiments eg- `Data wraggling/inital exploration notebooks` goes under `experiments` directory
- All modelling and related details into `analysis_framework`, create subdirectories as required 
- Under forecasting_framework there are three submodules `utils`, `data` and `pipelines`
  - `utils` reusable code components
  - `data` raw dataset are stored 
  - `pipeline` dagster pipeline and related computation output
  
### Flowchart for repo structure 
![github_capstone repo](https://user-images.githubusercontent.com/17350312/183260548-a2b2c501-b4eb-4d7b-bf79-478a8658ffaa.png)

### More on Git/version control usage 
[Material link](https://gist.github.com/sayantikabanik/8189ffdeee52f5c8f072244f4be94069)

### Repository setup
- Set up authentication using OAuth, SSH or push token
```shell
# for the first time
git clone <repo>

# change working directory to root of repo cloned
cd <repo location>
```

### Installing env setup using miniconda 💁🏽‍♀️
- [Instructions](https://docs.conda.io/en/latest/miniconda.html)

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
### Installing the analysis_framework package in local ⬇️
```shell
pip install -e .
```

### Update the `capstone` environment (post making changes to environment file)
```shell
conda env update --file environment.yml --prune
```
### To switch between different environment
```shell
conda deactivate
```

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
![Dagit UI](https://user-images.githubusercontent.com/17350312/183594876-8ca08737-137b-4f8e-b19b-2b204febd0c0.png)
![Lancher](https://user-images.githubusercontent.com/17350312/183594904-07d0ae7f-be4f-4e37-957e-0207f63c512f.png)



### Dashboard

- Tools used - Panel, Holoviews 
- Main files `app.py` (panel serve requirements and layout components) and `base.py` (contains all the logic)
- Command to trigger the dashboard (subject to change) - `python analysis_framework/dashboard/app.py`

![Dashboard](https://user-images.githubusercontent.com/17350312/183809714-e38adfa3-8ea8-4804-8623-57741c36157c.png)
