# 4_json

Pretty print JSON файлов

```{r, engine=bash}
$ python pprint_json.py --help
usage: pprint_json.py [-h] -f FILEPATH [-i INDENT]

Pretty print for JSON

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        Input file
  -i INDENT, --indent INDENT
                        Indentation size. Default: 4
```


## Использование

```{r, engine=bash}
$ python pprint_json.py -f unformatted.json
[
    {
        "Number": 1,
        "Id": "ae3e9479-070f-4d66-9429-de3acd8427ac",
        "Cells": {
            "Name": "Юнион Джек",
            "District": "Мещанский район",
            "SocialPrivileges": "нет",
            "geoData": {
                "coordinates": [
                    37.62158794615201,
                    55.76536695660836
                ],
                "type": "Point"
            },
            "SeatsCount": 30,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 621-19-63"
                }
            ],
            "global_id": 20660594,
            "IsNetObject": "нет",
            "OperatingCompany": null,
            "AdmArea": "Центральный административный округ",
            "Address": "Нижний Кисельный переулок, дом 3, строение 1"
        }
    },
    {
        "Number": 2,
...
```

Пример взят из списка [московских баров](http://data.mos.ru/opendata/7710881420-bary)

> Скрипт использует python 3 версии.


## Параметры

- `-f/--filepath` - путь до исходного файла с неотформатированным JSON
- `-i/--indent` - размер индентации. По умолчанию - 4.


## Лицензия

[Creative Commons Attribution License](http://creativecommons.org/licenses/by/2.0/)

