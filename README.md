# Описание проекта

Проект посвящен решеню задачи прогнозирования сердечных заболеваний. Ссылка на исходную выборку: https://www.kaggle.com/datasets/krishujeniya/heart-diseae 

# Запуск проекта
```
git clone https://github.com/ShasherinaAV/lab_IIS.git/
cd {директория с проектом}
python3 -m venv .venv_IIS
source .venv_IIS/bin/activate
pip install -r requirements.txt
```
# Запуск MLFlow

Скрипт для запуска MLFlow находится в папке mlflow в файле start_mlflow.

Для локального развертывания MLFlow достаточно перейтив папку со скриптом и выполнить команду:

```
sh start_mlflow.sh
```

Проверить, что фреймворк успешно запустился, можно пройдя в браузере на http://localhost:5000/.

# Описани датасета


Набор данных состоит из медицинских карт 303 пациентов, каждая из которых характеризуется 14 различными признаками, которые могут быть полезны для прогнозирования сердечно-сосудистых заболеваний. В набор данных включены следующие атрибуты:

1. <u>age</u> - возраст пациента в годах (29 - 77)
2. sex - пол пациента (0 = женщина, 1 = мужчина)
3. cp - тип боли в груди (0 = типичная стенокардия, 1 = атипичная стенокардия, 2 = неангиальная боль, 3 = бессимптомная)
4. <u>trestbps</u> - артериальное давление в состоянии покоя измеренное в мм рт.ст. при поступлении. (94 - 200)
5. <u>chol</u> - уровень холестерина в крови в мг/дл. (126 - 564)
6. fbs - уровень сахара в крови натощак > 120 мг/дл? (1 = верно, 0 = неверно)
7. restecg - результаты электрокардиографии в состоянии покоя (0 = в норме, 1 = аномалия зубца ST-T, 2 = возможная или определенная гипертрофия левого желудочка)
8. <u>thalach</u> - максимальная достигнутая частота сердечных сокращений, достигнутая во время тестирования с физической нагрузкой (71 - 202)
9. exang - была ли у пациента стенокардия, вызванная физической нагрузкой (1 = да; 0 = нет)
10. <u>oldpeak</u> - депрессия сегмента ST, наблюдаемая на электрокардиограмме во время физической нагрузки по сравнению с отдыхом. (0 - 6.2)
11. slope - описывает наклон сегмента ST при максимальной нагрузке (0 = наклонный вверх, 1 = плоский, 2 = наклонный вниз )
12. ca - количество крупных сосудов, видимых при коронарография. (0-4)
13. thal - талассемия, заболевание крови (1 = нормальное, 2 = фиксированный дефект, 3 = обратимый дефект) 
14. target - указывает на наличие или отсутствие сердечно-сосудистых заболеваний  (1 = наличие, 0 = отсутствие)

# Исследование данных

<u>В ходе исследования были проведены действия:</u>
* Изменен тип данных с числового на категориальный для 9 столбцов (sex, cp, fbs, restecg, exang, slope, ca, thal, target)
* изменен тип данных с int64 на int8/int16  для 4 столбцов (age, trestbps, chol, thalach)
* изменен тип данных с float164 float16 для 1 столбца (oldpeak)

Начальный объем датасета: 33.3 KB --> Итоговый объем датасета: 6.8 KB

<u> В ходе анализа были выявлены следующие закономерности:</u>

* У мужчин сердечные заболевания встречаются чаще, чем у женщин (см график `./eda/graph1.png`)
* Корреляция признаков слабая. Только у максимальной частотой сердечных сокращений (thalach) с возрастом (age) и депрессией ST (oldpeak) наблюдается некоторая корреляция (см график `./eda/graph2.png`)
* Нулевой и третий типы боли сердца в среднем встречаются у людей более старшего возраста (см график `./eda/graph3.png`)
* Зависимость уровня холестерина в крови от возраста (см график `./eda/graph4.png`)

Обработанная выборка сохранена в файл `clean_data.pkl`


# (ЛР2) Проведение экспериментов по настройке модели

В ходе исследования было построено несколько моделей. Все модели показали достаточно хорошие результаты, лучшие результаты были получены после предобработка столбцов с помощью PolynomialFeaturesи оптимальными параметрами, полученными с помощью библиотеки optuna.

Метрики полученные при обучении модели следующие:
- recall: 0.9069767441860465,
- precision: 0.9069767441860465,
- f1: 0.9069767441860465,
- roc_auc: 0.8928823114869625

Данные метрики получены при следующих параметрах модели:
- n_estimators: 115, 
- max_depth: 115, 
- max_features: 0.35393600475059334

RunID финальной модели: 631930cba3004003a5b966dc1e642aec


# (ЛР3) Создание сервиса предсказаний

ml_service:

- main.py -  файл с экземпляром FastAPI-приложения

- api_handler.py - файл с описанием класса-обработчика запросов к API

- requirements.txt - файл используемый для сборки образа, в нем находятся только необходимые зависимости и их версии

- Docerfile - файл с описанием алгоритма сборки образа

- scrin - скриншоты FastApi


models:

- get_model.py - скрипт для выгрузки модели из mlflow



**Команды для создания образа и запуска контейнера:**
```
docker build . --tag disease_model:0
docker run -p 8001:8000 -v $(pwd)/../models:/models disease_model:0
```


**Проверка роботоспособности сервиса:**
```
import requests
import random

params = {'id': 4}
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

response = requests.post('http://127.0.0.1:8001/api/prediction', params=params, json=data)
print(response.json())
```

# (Лр4) Мониторинг микросервиса

Был налажен веб-интерфейс prometheus, существующий для сбора и хранения метрик, генерируемых сервисами. Доступ к веб-интерфейсу осуществляется по адресу http://localhost:9090.

Были получены следующие скриншоты:

Гистограмма предсказаний модели
![Гистограмма предсказаний модели](services/prometheus/prometheus.png)


Частота запросов к сервису
![Частота запросов к сервису](services/prometheus/rate.png)


Частота запросов к сервису с кодами ошибок 4** и 5**

![Гистограмма предсказаний модели](services/prometheus/error.png)



# Дашбоард

 Был разработан сервис grafana. Сервис, созданный для визуализации метрик путём создания дашбордов. Веб-интерфейс запускается по адресу http://localhost:3000. В качестве database используется сервис prometheus.

Панель

![Панель](services/grafana/grafana.png)



Описание метрик, полученных на дашборде выше:

1.Первый график 

Среднее предсказанное значение

2. Предсказания

Гистограмма, отображающая распределение предсказаний модели по классам. 

3. Запросы

Временной ряд, показывающий количество полученных запросов. Уровень мониторинга: прикладной уровень.

4. CPU seconds total

Показывает время работы процессора