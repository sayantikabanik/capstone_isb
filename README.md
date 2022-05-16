# capstone_isb


### Installing miniconda/light version of anaconda 
- [Info + details](https://docs.conda.io/en/latest/miniconda.html)

```shell
conda env create --file environment.yml
```
```shell
conda activate fp2
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
### Installing the package in local 
```shell
pip install -e .
```

### Basic flow how to make best use of the workflow
- Clone the repo
- Create the env using the above commands 
- Install the package 
- All the tests goes into the `tests` directory 
- Any test experiements eg- `Data wraggling/inital exploration notebooks` goes under `experiments` directory
- All modelling and related details into `analysis_framework`, create subdirectories as required 
- Under forecasting_framework there are three submodules `utils`, `model`, `data` 
  - `utils` reusable code components
  - `model` all modelling aspects (**python scripts only**)
  - `data` pipepine and raw data

### How to contribute to the repo
- Create a separate branch for your usecase 
- Raise PR (**DO NOT** commit to main)


#### Meeting 
- 23rd April 2022 (9:30 PM) [Zoom link to be updated]

Topic: Capstone Project Selection

Time: Apr 23, 2022 09:30 PM India

Join Zoom Meeting
https://ISB.zoom.us/j/5046859164?pwd=MlBVYTZBenJYZmhXcWVvWGc0NXB6dz09

Meeting ID: 504 685 9164
Passcode: 874071
