# Висновок:
    в третьому завданні було здійснено дослідження швидкодії алгоритмів пошуку, а саме:
    - Боєра-Мура
    - Кнута-Морріса-Пратта
    - Рабіна-Карпа

В якості експериментального середовище використовувались 2 текстові файли.
Сам експеримент поділився на 3 частини:
1) дослідження швидкодії пошуку в першому текстовому файлі
2) дослідження швидкодії пошуку в другому текстовому файлі
3) дослідження швидкодії пошуку в другому текстовому файлі за неправильного вхідного рядка

Крім того, для кожного з вищенаведених алгоритмів пошук, шуканий рядок був вибраний різної довжини: 
- короткиий рядок (декілька слів), 
- рядок середньої довжини (1 речення) 
- довгий рядок (1 абзац)

Враховуючи више сказане, було проведено дослідження швидкодії алгоритмів пошуку, і їх результати наведено в таблицях 1 - 3
В таблиці 1 зображена робота алгоритмів пошуку. Як видно найкращим алгоритмом являється алгоритм Боєра-Мура. Швидкість знаходження коротких рядків та рядків середньої довжини практично однакові. А ось при пошуку рядків-абзаців спостерігається практично подвоєння часу пошуку.
Найгіршим по швидкодії є алгорити Рабіна-Карпа.

![list](assets/table_1.png)

Як видно з результатів роботи алгоритмів пошуку (таблиця 2), найшвидшим алгоритмом, як і в попередньому досліді, є алгоритм Боєра-Мура. Який практично на порядок швидше знаходить короткі рядки, в порівнянні з іншими алгоритмами. Однак, тут гарно видно, що при збільшенні довжини рядка зменшується час пошуку.

![list](assets/table_2.png)

В останньому досліді було здійснено пошук наперед заданих неправильних рядків (таблиця 3). Результатом такого пошуку є те, що для коротких та середньої довжини рядків спостерігається зростання часу пошуку для всіх алгоритмів практично в 2 рази (а порівнянні з попередніми дослідами). Однак для довгих рядків спостерігається, в деяких випадках, краща швидкодія ніж в порівнянні з валідним пошуком (алгоритм Боєра-Мура). Швидкодія алгоритмів Рабіна-Карпа та Кнута-Морріса-Пратта практично не змінюється, незалежно від довжини рядка. 

![list](assets/table_3.png)

Підсумовуючи все, можна сказати, що найшвидшим алгоритмом пошуку являється алгоритм Боєра-Мура. За неправильно вхідного рядка, час виконання алгоритмів пошуку зростає біль ніж в 2 рази, що свідчить про асимптотичну складність Однак для довгих рядків різниця не є такою значною, а в деяких випадках, навіть меншою ніж за нормального валідного пошуку.


