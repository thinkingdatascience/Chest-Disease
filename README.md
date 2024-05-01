# Chest-Disease-Classification-from-Chest-CT-Scan-Image

 - [Data link](https://drive.google.com/file/d/1-B_zHEL3RsnNgs5uz6odUGNVR2pp_xc7/view?usp=sharing)

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity (Inside entity/config_entity.py)
4. Update the configuration manager in src config (Inside config/configuration.py)
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml 



## Live matarials docs

[link](https://docs.google.com/document/d/1UFiHnyKRqgx8Lodsvdzu58LbVjdWHNf-uab2WmhE0A4/edit?usp=sharing)


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n chest python=3.8 -y
```

```bash
conda activate chest
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

### Mlflow dagshub connection uri

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/thinkingdatascience/Chest-Disease.mlflow
export MLFLOW_TRACKING_USERNAME=thinkingdatascience
export MLFLOW_TRACKING_PASSWORD=b05d4dd4de23d79323f7b895b587f8f2aac213fb
python script.py
```


### RUN from bash terminal

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Chest-Disease-Classification-from-Chest-CT-Scan-Image.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```



### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag