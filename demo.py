import mlflow
import os
import argparse
import time

def evaluate(a , b):
    metric = a**2 + b**2
    return metric

def main(p1,p2):
    with mlflow.start_run():
        mlflow.log_param("param1" , p1) ## key value pair
        mlflow.log_param("param2" , p2)

        metric = evaluate(a=p1 ,b= p2)
        mlflow.log_metric("Result"  , metric)

        ## Create a File and print the current time and store it as log
        os.makedirs("temp" , exist_ok=True)
        with open("temp/sample.txt" , "w") as f:
            f.write(time.asctime())
        
        mlflow.log_artifact("temp")  ## it will create a sample.txt in a artifacts folder in mlruns



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--param1" , "-p1" , type=int , default =2)
    args.add_argument("--param2" , "-p2" , type=int , default =5)
    parsed_args = args.parse_args()
    main(parsed_args.param1 , parsed_args.param2)



