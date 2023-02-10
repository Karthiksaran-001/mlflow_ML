# mlflow WineQuality Dataset
Starting with ML-Flow

## Create a new python Environment and activate 

```
conda create --prefix ./env python==3.7 -y && conda activate ./env
```

## install mlflow

```
pip install mlflow
```
## Run Python file
```
python demo.py 
```

## To test the model using ui

```
mlflow models serve -m F:/AIOPS/ML-Flow/mlflow_ML/mlruns/0/0df96c7b964b47c789d47e469f915226/artifacts/model/ -p 1234
```
