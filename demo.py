import mlflow
import os
import argparse

def evaluate(a , b):
    metric = a**2 + b**2
    return metric

def main(p1,p2):
    with mlflow.start_run():
        mlflow.log_param("param1" , p1) ## key value pair
        mlflow.log_param("param2" , p2)

        metric = evaluate(a=p1 ,b= p2)
        mlflow.log_metric("Result"  , metric)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--param1" , "-p1" , type=int , default =2 , required=True)
    args.add_argument("--param2" , "-p2" , type=int , default =5 , required=True )
    parsed_args = args.parse_args()
    main(parsed_args.param1 , parsed_args.param2)



