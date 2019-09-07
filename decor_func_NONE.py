import time
from datetime import datetime
from random import randint
from random import choice

data = {}


# запись в словарь
def run_data_decorator(func_run):

    def wrapper(*args, **kwargs):
        global data

        now_use = {datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"):
                       {'Получила': [args, kwargs], 'Вернула': [func_run(*args, **kwargs)]}}

        if data.get(func_run.__name__) == None:
            data.update({func_run.__name__: now_use})
        elif data.get(func_run.__name__) != None:
            dict_up = data.get(func_run.__name__)
            dict_up.update(now_use)
            data[func_run.__name__] = dict_up

    return wrapper


# запись лога в файл
def log_file_decorator(func_show):
    def wrapper(data):
        func_show(data)
        f = open('function_log.txt', 'a')
        for item in data.items():
            f.write('Функция ({})'.format(item[0]) + '\n')
            for call in item[1].items():
                f.write('     ' + 'Вызывалась: {}'.format(call[0]) + '\n')
                for value in call[1].items():
                    f.write('       ' + str(value[0]) + ' значение' + ':' + str(value[1]) + '\n')
                f.write('\n')
        f.write(' --------------------END CALL-------------------- \n')
        f.close()
    return wrapper


def none_decorator(func_show):
    # в задании было что именно отображение None, то можно отобразиить data без перезаписи ключей
    # (то несоответсвие если функция вызывалась 2 и более раз)
    # просто распарсить data снова, я не знаю или так верно, не вызывая функции
    def wrapper(data):
        format_value = None
        for item in data.items():
            print('Функция ({})'.format(item[0]))
            for call in item[1].items():
                print('     ' + 'Вызывалась: {}'.format(format_value))
                for value in call[1].items():
                    print('     ', end='')
                    print(f'{value[0]}' + ' значение', format_value, sep=': ')
                print()
    return wrapper


@log_file_decorator     # в лог пишем реальные данные
@none_decorator         # в консоль выводим None, интересная конструкция получилась
def data_show(data):
    for item in data.items():
        print('Функция ({})'.format(item[0]))
        for time in item[1].items():
            print('     '+'Вызывалась: {}'.format(time[0]))
            for value in time[1].items():
                print('     ', end='')
                print(str(value[0])+' значение', value[1], sep=': ')
            print()


# с функциями сильно не заморачивался, написал типичные
@run_data_decorator
def func_1(*args, **kwargs):
    res = 0
    for arg in args:
        if type(arg) == int:
            res += arg
        elif type(arg) == list or type(arg) == tuple:
            for elem in arg:
                res += int(elem)
    return res

@run_data_decorator
def func_2(*args, **kwargs):
    return 'Отравить', args, kwargs

@run_data_decorator
def func_3(*args, **kwargs):
    return 'Done'

@run_data_decorator
def my_random_str(n):
    return_str = ''
    try:
        n = int(n)
    except ValueError:
        return_str = '(n)__input__ERROR!'
    else:
        source_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-()'
        if n > 0:
            for i in range(n):
                return_str += choice(source_str)
        else:
            return_str = '(n)_is not positive__input__ERROR!'
    finally:
        return return_str

@run_data_decorator
def multiply(*args, **kwargs):
    res = 1
    for arg in args:
        res = res*int(arg)
    return res


# вызов функций
func_1(5, -6, 10, 15)
func_2('2', 'new')
func_3('3', 'new')
my_random_str(10)
multiply(10, 5, 8, 10)

time.sleep(1)
func_1([-x for x in range(10)])
func_2('None', None)
multiply(101, 5, 8, 101)
time.sleep(1)
my_random_str(randint(1, 20))
time.sleep(1)
my_random_str('not int')

# словарь с действиями
data_show(data)