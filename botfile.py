
import os
import configparser  # импортируем библиотеку
def path_finder():
    return os.path.dirname(os.path.abspath(__file__))
def write_to_config(section, name, value):
    ''' Writing data in config file. Warnings!!! it erases other data '''
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    conf.set(section, name, value)
    with open('config.ini', 'w') as configfile:
        conf.write(configfile)


def read_from_config(section: str, key: str):
    ''' Read data from config file '''
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    return conf[section][key]

write_to_config('telegram', 'password', '112233')
#read_from_config('telegram', 'password')
#print(read_from_config('telegram', 'password'))
