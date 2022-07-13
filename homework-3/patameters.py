import time
import math


def waiting(call_count: int, start_sleep_time: int, factor: int, border_sleep_time: int):
    def decorator(func):
        print(f'Кол-во запусков = {call_count}')
        print(f'Начало работы')

        def wrapper(*args):
            f = func(*args)
            s = factor
            t = start_sleep_time
            for i in range(call_count):
                if t < border_sleep_time:
                    print(f'Время ожидания: {t}')
                    time.sleep(t)
                    print(f'Результат декорируемой функций = {f}')
                    t = start_sleep_time * (math.exp(s))
                else:
                    t = border_sleep_time
                    print(f'Время ожидания: {t}')
                    time.sleep(t)
                    print(f'Результат декорируемой функций = {f}')
                s += 1
            print(f'Конец работы')
            return

        return wrapper

    return decorator


@waiting(call_count=5, start_sleep_time=1, factor=1, border_sleep_time=15)
def multi(number: int):
    return number * 2


if __name__ == "__main__":
    multi(2)
