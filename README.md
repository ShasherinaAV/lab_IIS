# Описание проекта

Проект посвящен решеню задачи прогнозирования сердечных заболеваний. Ссылка на исходную выборку: https://www.kaggle.com/datasets/krishujeniya/heart-diseae 

# Запуск
```
git clone https:/github.com/ShasherinaAV/lab_IIS.git/
cd {директория с проектом}
python3 -m venv .venv_IIS
source .venv_IIS/bin/activate
pip install -r requirements.txt
```
# Описани датасета


303 строки, 14 столбца

1. age - возраст пациента (29 - 77)
2. sex - пол пациента (0 - женщина, 1 - мужчина)
3. cp - тип боли в груди (1-4)
4. trestbps - артериальное давление в состоянии покоя (94-200)
5. chol - уровень холестерина в крови (126-564)
6. fbs - уровень сахара в крови натощак > 120мг/дл? (1 - верно, 0 - неверно)
7. restecg - результаты электрокардиографии в состоянии покоя (0-2)
8. thalach - максимальная частота сердечных сокращений (71 - 202)
9. exang - стенокардия, вызванная физической нагрузкой (1 = да; 0 = нет)
10. oldpeak - депрессия ST, вызванная физической нагрузкой, по сравнению с отдыхом (0 - 6.2)
11. slope - непонятные данные
12. ca - непонятные данные
13. thal - непонятные данные
14. target - результат (1 - есть сердечное заболевание, 0 - нет сердечного заболевания)

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




# Лабораторная работа №2. Проведение экспериментов по настройке модели

*Цель работы*: Провести ряд экспериментов по настройке модели, логируя все результаты в MLFlow. Научиться пользоваться инструментами autofeat, mlxtend, MLFlow


 