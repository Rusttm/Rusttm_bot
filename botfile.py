
import os
import configparser  # импортируем библиотеку
def write_to_config(section, name, value):
    ''' Writing data in config file. Warnings!!! it erases other data '''
    conf = configparser.ConfigParser()  # создаём объекта парсера
    conf[section]={name: value}
    with open('config.ini', 'w') as configfile:
        conf.write(configfile)
def read_from_config(section: str, key: str):
    ''' Read data from config file '''
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    return conf[section][key]
print(read_from_config('id', 'rustam'))
