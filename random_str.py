def my_random_str(n):
    return_str = ''

    try:
        n = int(n)

    except ValueError:
        return_str = '(n)__input__ERROR!'
    else:
        # лучьше разместить здесь чтоб код не отрабатывал
        # ramdom и строка не подгружались если exception
        from random import choice
        source_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-()'

        if n > 0:
            for i in range(n):
                return_str += choice(source_str)
        else:
            return_str = '(n)_is not positive__input__ERROR!'
    finally:
        return return_str

def write_file(input_str):
    f = open('bred.txt', 'a')
    f.write(input_str+'\n')
    f.close()
def read_file(file_name):
    f = open(str(file_name), 'r')
    for line in f:
        print(line)
    f.close()
def erase_file(file_name):
    f = open(str(file_name), 'w')
    f.close()


exit_flag = False

while not exit_flag:
    inp_n = input('Введите кол-во элементов(or exit to stop):')
    if inp_n == 'exit':
        exit_flag = True
    elif inp_n == 'erase':
        erase_file('bred.txt')
    else:
        result = my_random_str(inp_n)
        write_file(result)
        print(result)

print('____END_PROGRAM____')
read_file('bred.txt')