import threading
from time import time, sleep


class FibonacciException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def banchmark(inner_func):
    def wrapper(*args, **kwrgs):
        start_time = time()
        result = inner_func(*args, **kwrgs)
        end_time = time()
        print(f'Функция {inner_func.__name__} проработала {round(end_time - start_time, 2)} с.')
        return result
    return wrapper


def recursion_fibonacci(num: int) -> int:
    if num <= 1:
        return 1
    return recursion_fibonacci(num - 1) + recursion_fibonacci(num - 2)


def recursion_factorial(num: int) -> int:
    if num <= 1:
        return 1
    return recursion_factorial(num - 1) * num
 

@banchmark
def print_fibonacci(num: int) -> None:
    print(f'Число fibonacci({num}) =', recursion_fibonacci(num))


def danger_fibonacci(num: int):
    if num < 0:
        raise FibonacciException('You cannot pass a negative number in fibonacci function!')
    
    if num <= 1:
        return 1
    return danger_fibonacci(num - 2) + danger_fibonacci(num - 1)


def worker():
    thread = threading.current_thread()
    name = thread.name
    identifier = hex(threading.get_ident())
    native_identifier = hex(threading.get_native_id())
    print(f'Работает поток: {name} с id: {identifier} и системным id: {native_identifier}')
    sleep(1)
    print(f'Поток {name} завершил свою работу')


def custom_excepthook(args: threading.ExceptHookArgs):
    print(args.exc_value)
    # Additional logging for example


def write_data_in_file(file_name: str, data: str) -> None:
    with open(file_name, 'w') as file:
        file.write(data)

    
def clear_file() -> None:
    with open('test1.txt', 'w') as file:
        file.truncate(0)
    with open('test2.txt', 'w') as file:
        file.truncate(0)
