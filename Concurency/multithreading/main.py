import os
import threading
import requests


def banchmark(inner_func):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = inner_func(*args, **kwargs)
        end = time()
        print(f'Time for {inner_func.__name__}: {end - start} s.')
        return result
    return wrapper


def get_process_threads_info() -> None:
    print(f'Current process id: {os.getpid()}')
    print(f'Quantity of threads in process: {threading.active_count()}')
    print(f'Current thread\'s name: {threading.current_thread().name}')


def print_fibonacci_number(number: int) -> None:
    def fibonacci(n: int) -> int:
        if n <= 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    print(f'Fibonacci({number}) = {fibonacci(number)}')


@banchmark
def fibonacci_with_no_threading(number1: int, number2: int) -> None:
    print_fibonacci_number(number1)
    print_fibonacci_number(number2)


@banchmark
def fibonacci_with_threads(number1: int, number2: int) -> None:
    thread1 = threading.Thread(target=print_fibonacci_number, args=(number1, ))
    thread2 = threading.Thread(target=print_fibonacci_number, args=(number2, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


def print_status_code_from_webapi(url: str) -> None:
    response = requests.get(url)
    print(response.status_code)


@banchmark
def print_status_codes_with_no_threads(url1: str, url2: str) -> None:
    print_status_code_from_webapi(url1)
    print_status_code_from_webapi(url2)


@banchmark
def print_status_code_with_threads(url1: str, url2: str) -> None:
    thread1 = threading.Thread(target=print_status_code_from_webapi, args=(url1, ))
    thread2 = threading.Thread(target=print_status_code_from_webapi, args=(url2, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == '__main__':
    # fibonacci_with_no_threading(40, 42)
    # fibonacci_with_threads(40, 42)

    # print_status_codes_with_no_threads('https://www.example.com/', 'https://www.example.com/')
    print_status_code_with_threads('https://www.example.com/', 'https://www.example.com/')
