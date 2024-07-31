import time
import datetime
import calendar


def print_structu_time(t: time.struct_time) -> None:
    for attr in t.__dir__():
        if '__' not in attr and '_' in attr:
            print(f'\t{attr}: {getattr(t, attr, "")}')


if __name__ == '__main__':
    print(f'Количество секунд, прошедших с эпохи: {time.time()}')
    print(f'Местное время с прошедшей эпохи [Дата эпохи + 123 секунды]: {time.ctime(123)}\n\n')

    # print('Начинается выполняться функция time.sleep(3). Поток выполнения заблокируется на 3 секунды')
    # time.sleep(3)
    # print('Поток выполнения продолжается')

    print('Функция time.localtime(123) возвращает объект struct_time, который является надстройкой над обычным tuple')
    print('Этот объект содержит информацию о том, какой год, месяц, день, час и т.д. с момента после эпохи\n')
    print('Объект struct_time в локальном формате:')
    print_structu_time(time.localtime(86400 * 35))
    print('\nОбъект struct_time в UTC формате:')
    print_structu_time(time.gmtime(86400 * 35))

    print(f'\nКоличество секунд, прошедших с начала эпохи и до определенной даты: '
          f'{time.mktime((1980, 6, 22, 5, 3, 4, 1, 1, 1))}')

    s_time = time.localtime(123)
    print(time.mktime(s_time))

