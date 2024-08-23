import threading
from time import sleep

from library import (
    banchmark, recursion_factorial, recursion_fibonacci, worker,
    danger_fibonacci, custom_excepthook, write_data_in_file,
    clear_file
)


@banchmark
def sequential_cpu_bound_execution() -> None:
    recursion_fibonacci(35)
    recursion_factorial(35)


@banchmark
def concurrent_cpu_bound_execution() -> None:
    fibonacci_thread = threading.Thread(target=recursion_fibonacci, args=(35, ))
    factorial_thread = threading.Thread(target=recursion_factorial, args=(35, ))

    fibonacci_thread.start()
    factorial_thread.start()

    fibonacci_thread.join()
    factorial_thread.join()


@banchmark
def sequential_io_bound_execution() -> None:
    write_data_in_file('test1.txt', 'Lorem ipsum Doler sit amet' * 10**7)
    write_data_in_file('test2.txt', 'Lorem ipsum Doler sit amet' * 10**7)


@banchmark
def concurrent_io_bound_execution() -> None:
    thread1 = threading.Thread(target=write_data_in_file, args=('test1.txt', 'Lorem ipsum Doler sit amet' * 10**7, ))
    thread2 = threading.Thread(target=write_data_in_file, args=('test2.txt', 'Lorem ipsum Doler sit amet' * 10**7, ))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


def create_six_threads(func) -> None:
    for i in range(0, 6):
        thread = threading.Thread(target=func, args=(), name=f'Beautiful Thread-{i}')
        thread.start()


def execute_danger_fibonacci() -> None:
    thread = threading.Thread(target=danger_fibonacci, args=(-10, ))
    thread.start()
    thread.join()   


if __name__ == '__main__':
    sequential_cpu_bound_execution()
    concurrent_cpu_bound_execution()
    print('\n')

    sequential_io_bound_execution()
    sleep(1)
    clear_file()
    concurrent_io_bound_execution()
    clear_file()
    print('\n')

    print(f'Количество активных потоков до вызова функции create_six_threads: {threading.active_count()}\n')
    create_six_threads(worker)
    print(f'\nКоличество активных потоков после вызова функции create_six_threads: {threading.active_count()}\n\n')
    
    active_threads = threading.enumerate()
    print('Список активных потоков в системе:')
    for thread in active_threads:
        print(thread.name)

    # Мы не можем обрабатывать исключения, которые возникли в дочерних потоках через
    # обвчный try-catch. Для этого мы используем threading.excepthook
    
    sleep(1)
    threading.excepthook = custom_excepthook
    print('Main-Thread работает\n')
    execute_danger_fibonacci()
    print('\nMain-Thread продолжает работать')

    main_thread = threading.main_thread()
    print(main_thread.name)
    
    