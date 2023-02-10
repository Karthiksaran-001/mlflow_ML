import mlflow
import mlflow.sklearn
import os
import argparse
import time
from sklearn.metrics import mean_absolute_error , mean_squared_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import numpy as np
import pandas as pd

def evaluate(actual , predicted):
    rmse = np.sqrt(mean_absolute_error(actual , predicted))
    mae = mean_absolute_error(actual , predicted)
    r2 = r2_score(actual , predicted)
    return rmse , mae , r2

def get_data():
    URL ="https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv"
    try:
        df = pd.read_csv(URL)
        return df
    except Exception as e:
       raise e


def main(alpha , l1_ratio):
    df = get_data()
    x =df.iloc[: , :-1]
    y = df[["quality"]]
    X_train, X_test, y_train, y_test =train_test_split(x , y , test_size=0.2 )

    ## mlflow implementation
    with mlflow.start_run():

        mlflow.log_param("alpha" , alpha) ## use key value pair
        mlflow.log_param("l1_ratio" , l1_ratio)


        model_lr = ElasticNet(alpha=alpha , l1_ratio=l1_ratio , random_state=42)
        model_lr.fit(X_train , y_train)
        pred = model_lr.predict(X_test)

        rmse , mae , r2 = evaluate(y_test , pred)

        mlflow.log_metric("root mean squared error" , rmse)
        mlflow.log_metric("mean absolute error" , mae)
        mlflow.log_metric("r2-score" , r2)

        print(f"params-- alpha:{alpha}, l1_ratio:{l1_ratio}")
        print(f"rmse: {rmse} , mae: {mae} , r2: {r2}")

        mlflow.sklearn.log_model(model_lr , "model") ## model , path








if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--alpha" , "-a" , type=float , default =0.5)
    args.add_argument("--l1_ratio" , "-l1" , type=float , default =0.6)
    parsed_args = args.parse_args()
    main(alpha = parsed_args.alpha , l1_ratio = parsed_args.l1_ratio)



