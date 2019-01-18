# Ближайшие бары

Скрипт определяет среди баров: 
- бар с  наибольшим количеством мест;
- бар с наименьшим количеством мест;
- бар, ближайший к указанным координатам;

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 

Необходимо загрузить файл c JSON базой баров. \
Это можно сделать на сайте [Портала открытых данных](https://data.mos.ru/)
или по прямой [ссылке](https://devman.org/fshare/1503831681/4/) с сайта *devman.ru*. \
Скрипт ожидает обнаружить файл с именем *bars.json* в дирректории, из которой был запущен. 

Запуск на Linux:

```bash
# possibly requires call of python3 executive instead of just python
$ python bars.py -h
usage: bars.py [-h] [-c L L] [-f DATA_FILE]

Choose the best bar for the evening :)

optional arguments:
  -h, --help            show this help message and exit
  -c L L, --coordinate L L
                        longitude and latitude to find closest bar
  -f DATA_FILE, --data_file DATA_FILE
                        path to file with JSON data of bars
```
Для точки с координатами 55.957956 с. ш. 37.440356 в. д. 

```bash
$ python bars.py -c 37.440356 55.957956
Biggest bar: 
		"Спорт бар «Красная машина»"
	Автозаводская улица, дом 23, строение 1
	+7 (905) 795-15-84

Smallest bar: 
		"БАР. СОКИ"
	Дубравная улица, дом 34/29
	+7 (495) 258-94-19

Closest bar: 
		"Бар IMAX"
	Правобережная улица, дом 1Б
	+7 (495) 775-77-79
```
```bash
$ python bars.py -f ./bars.json
Tell please longitude and latitude to find closest bar
longitude: 37.440356
latitude: 55.957956
Biggest bar: 
		"Спорт бар «Красная машина»"
	Автозаводская улица, дом 23, строение 1
	+7 (905) 795-15-84

Smallest bar: 
		"БАР. СОКИ"
	Дубравная улица, дом 34/29
	+7 (495) 258-94-19

Closest bar: 
		"Бар IMAX"
	Правобережная улица, дом 1Б
	+7 (495) 775-77-79


```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
