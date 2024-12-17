import requests
import time
import random

for i in range(50):
    params = {'patient_id': i}
    data = {
        "age":random.randint(15,90),
        "sex":random.randint(0,1),
        "cp":random.randint(0,3),
        "trestbps":random.randint(70,220),
        "chol":random.randint(100,600),
        "fbs":random.randint(0,1),
        "restecg":random.randint(0,2),
        "thalach":random.randint(60,220),
        "exang":random.randint(0,1),
        "oldpeak":3.5,
        "slope":random.randint(0,2),
        "ca":random.randint(0,4),
        "thal":random.randint(1,3),
        "target":random.randint(0,1)} 
    response = requests.post('http://heart-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())