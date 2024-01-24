from timeit import timeit
from typing import Callable

from rich.table import Table
from rich.console import Console

from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search
from rabin_karp_search import rabin_karp_search
        
def read_file(filename):
    with open(filename, 'r', encoding='cp1251') as f:
        return f.read()


def execution_time(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)

def build_comparison_table(data: list, title) -> Table:
    table = Table(title=title, style="blue", show_lines=True)

    table.add_column("Algorithm", justify="center", style="green",min_width=20, no_wrap=True)
    table.add_column("Time,s (short str)", style="yellow", justify="center", max_width=35, no_wrap=False)
    table.add_column("Time,s (middle str)", justify="center",min_width=20, style="yellow")
    table.add_column("Time,s (long str)", justify="center",min_width=20, style="yellow")
    for elem in data:
        table.add_row(elem[0], f'{elem[1][0]:.5f}', f'{elem[1][1]:.5f}', f'{elem[1][2]:.5f}')
    return table

def create_row(func: Callable, arr: list, text: str, patterns: list) -> list:
    times = []
    for pattern in patterns:
        time = execution_time(func, text, pattern)
        times.append(time)
    arr.append((func.__name__, times))
    return arr

def task3():
    console = Console()
    file_1 = read_file('article_1.txt')
    file_2 = read_file('article_2.txt')
    
    fake_pattern_short = 'Ти знаєш, що ти — людина.'
    fake_pattern_middle = 'Ти знаєш, що ти — людина. Ти знаєш про це чи ні. Усмішка твоя — єдина, Мука твоя — єдина, Очі твої — одні.'
    fake_pattern_long = 'Ти знаєш, що ти — людина. Ти знаєш про це чи ні. Усмішка твоя — єдина, Мука твоя — єдина, Очі твої — одні. Більше тебе не буде. Завтра на цій землі Інші ходитимуть люди, Інші кохатимуть люди — Добрі, ласкаві й злі. Сьогодні усе для тебе — Озера, гаї, степи. І жити спішити треба, Кохати спішити треба — Гляди ж не проспи! Бо ти на землі — людина, І хочеш того чи ні —'
    
    short_pattern_1 = "При рівномірно розподілених"
    middle_pattern_1 = "У жадібному алгоритмі завжди робиться вибір, який здається найкращим у даний момент - тобто виробляється локально оптимальний вибір у надії, що він приведе до оптимального рішення глобальної задачі."
    long_pattern_1 = 'Кожна система містить набір обмежень і вимог. Правильно підібраний алгоритм пошуку, що враховує ці обмеження відіграє визначальну роль у продуктивності системи. Алгоритми, призначені для вирішення завдань оптимізації, звичайно являють собою послідовність кроків, на кожному з яких надається деяка множина виборів. Визначення найкращого вибору, керуючись принципами динамічного програмування, у багатьох задачах оптимізації нагадує стрілянину з гармати по горобцях; іншими словами, для цих завдань краще підходять більш прості й ефективні алгоритми.'
    
    
    short_pattern_2 = "розмір сесії 192"
    middle_pattern_2 = "Для кожного агента випадковим чином генерується від 1 до n вподобань."
    long_pattern_2 = "Хеш-таблиця (hash map) – це структура даних, у якій пошук елементу здійснюється на основі його ключа. Хеш від ключа вказує, у якій комірці розташовується елемент. Якщо кілька елементів мають однаковий хеш, то виникає колізія. Існує два методи розв’язання колізій – закрита та відкрита адресації. При закритій адресації кожен елемент таблиці – це зв’язний список і усі елементи з однаковим хешем додаються до одного списку. Це найпростіший спосіб розв’язання колізій, але він використовує додаткову пам’ять для вказівників і не дозволяє використовувати переваги кешування при обході елементів хеш-таблиці. При відкритій адресації у випадку колізії обирається нова позиція елементу. Нова позиція може обиратися як за допомогою додаткової хеш-функції, так і шляхом зміщення позиції на декілька елементів. Пошук повторюється, доки не буде досягнуто порожнього елемента."

    
    results = []
    create_row(boyer_moore_search, results, file_1, [short_pattern_1, middle_pattern_1, long_pattern_1])
    create_row(kmp_search, results, file_1, [short_pattern_1, middle_pattern_1, long_pattern_1])
    create_row(rabin_karp_search, results, file_1, [short_pattern_1, middle_pattern_1, long_pattern_1])

    console.print(build_comparison_table(results, 'Table 1 - Searching time comparison table for first file'))
    
    results_2 = []
    create_row(boyer_moore_search, results_2, file_2, [short_pattern_2, middle_pattern_2, long_pattern_2])
    create_row(kmp_search, results_2, file_2, [short_pattern_2, middle_pattern_2, long_pattern_2])
    create_row(rabin_karp_search, results_2, file_2, [short_pattern_2, middle_pattern_2, long_pattern_2])

    console.print(build_comparison_table(results_2, 'Table 2 - Searching time comparison table for second file'))
    
    results_fake = []
    create_row(boyer_moore_search, results_fake, file_2, [fake_pattern_short, fake_pattern_middle, fake_pattern_long])
    create_row(kmp_search, results_fake, file_2, [fake_pattern_short, fake_pattern_middle, fake_pattern_long])
    create_row(rabin_karp_search, results_fake, file_2,[fake_pattern_short, fake_pattern_middle, fake_pattern_long])

    console.print(build_comparison_table(results_fake, 'Table 3 - Searching time comparison table for second file with fake pattern'))

if __name__ == '__main__':
    task3()