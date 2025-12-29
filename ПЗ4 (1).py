from time import *
from logging import *

basicConfig(level=INFO, filename='PZ_4.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')


def iterative_fibonachi(n):
    a = 0
    b = 1
    for _ in range(n):
        a1 = a
        a = b
        b = a1 + b
    return a


def recursive_fibonachi(n):
    if n <= 1:
        return n
    return recursive_fibonachi(n - 1) + recursive_fibonachi(n - 2)


start_time = time()
print(iterative_fibonachi(50))
end_time = time()
execution_time = end_time - start_time
info(f'Время работы итеративной функции: {execution_time:.6f} секунд')

start_time = time()
print(recursive_fibonachi(50))
end_time = time()
execution_time = end_time - start_time
info(f"Время работы рекурсивной функции: {execution_time:.6f} секунд")
