# this is my end to end project

# first initialize the git

```
git init
```

```
git add abc.txt
git add .
```
```
git commit -m "this is my first commit"
```

```

git pull

```
### for shell scripting
```
bash your_file_name.sh
```

```
python setup.py install
```

# another way you can mention -e . in your requirement file and you can run

```
pip install -r requirements.txt
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### local cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/LolaPrasad/Dimond_Price_Prediction.mlflow \
MLFLOW_TRACKING_USERNAME=LolaPrasad \
MLFLOW_TRACKING_PASSWORD=b3dd566df7aa0993bd001ce80436a98f1df03907 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/LolaPrasad/Dimond_Price_Prediction.mlflow

export MLFLOW_TRACKING_USERNAME=LolaPrasad

export MLFLOW_TRACKING_PASSWORD=b3dd566df7aa0993bd001ce80436a98f1df03907

```


### DVC cmd
- dvc init
- dvc repro
- dvc dag

