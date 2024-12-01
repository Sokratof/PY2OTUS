# Проект: Сервис для формирования статистического отчета
Данный проект - статистический отчет о характеристиках запросов к сервису на основании анализа логов, создаваемых Nginx.

## Функциональные возможности cтатистического анализа
  - Среднее время ответа  +
  - Медианное время ответа  +
  - Максимальное время ответа +
  - Минимальное время ответа  +

## Оформление проекта
Проект разработан в соответствии с наилучшими практикантками.

## Интеграция в систему непрерывной интеграции (CI)
Run flake8 .
./HW1/parser.py:6:80: E501 line too long (168 > 79 characters)
./HW1/parser.py:21:80: E501 line too long (89 > 79 characters)
./HW1/parser.py:22:59: E261 at least two spaces before inline comment
./HW1/parser.py:22:80: E501 line too long (89 > 79 characters)
./HW1/parser.py:25:5: E701 multiple statements on one line (colon)
Error: Process completed with exit code 1.

## Подключение линтеров
(myenv) sokratov@sokratov:~/PROPYOTUS/HW1$ pylint parser.py
************* Module parser
parser.py:5:0: C0301: Line too long (168/100) (line-too-long)
parser.py:1:0: C0114: Missing module docstring (missing-module-docstring)
parser.py:11:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
parser.py:24:6: C0103: Constant name "average_time" doesn't conform to UPPER_CASE naming style (invalid-name)
parser.py:24:21: C0103: Constant name "median_time" doesn't conform to UPPER_CASE naming style (invalid-name)
parser.py:24:35: C0103: Constant name "max_time" doesn't conform to UPPER_CASE naming style (invalid-name)
parser.py:24:46: C0103: Constant name "min_time" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 6.50/10 (previous run: 5.00/10, +1.50)

## Подключение чекеров
(myenv) sokratov@sokratov:~/PROPYOTUS/HW1$ mypy parser.py
Success: no issues found in 1 source file

## Dockerfile - для контейнеризации приложения
sokratov@sokratov:~/PROPYOTUS$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
docker_hw1   latest    9ac3def9c2ce   About a minute ago   277MB


**README** оформлен так же в лучших практиках