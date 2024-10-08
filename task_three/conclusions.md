# Порівняння алгоритмів пошуку підрядка

## Опис алгоритмів

- **Боєр-Мур:** Використовує правило поганого символа та хорошого суфікса для швидкого пошуку.
- **Кнут-Морріс-Пратт (KMP):** Використовує префікс-функцію для уникнення повторного порівняння символів.
- **Рабін-Карп:** Використовує хешування для швидкого порівняння підрядків.

## Результати тестування

### Стаття 1

- **Боєр-Мур:**
  - Час на існуючий підрядок: 0.0008996000105980784 секунд
  - Час на неіснуючий підрядок: 0.02404220000607893 секунд
- **Кнут-Морріс-Пратт:**
  - Час на існуючий підрядок: 0.003789500013226643 секунд
  - Час на неіснуючий підрядок: 0.27027259999886155 секунд
- **Рабін-Карп:**
  - Час на існуючий підрядок: 0.0034189000143669546 секунд
  - Час на неіснуючий підрядок: 0.21627580001950264 секунд

### Стаття 2

- **Боєр-Мур:**
  - Час на існуючий підрядок: 0.014307300007203594 секунд
  - Час на неіснуючий підрядок: 0.042131499998504296 секунд
- **Кнут-Морріс-Пратт:**
  - Час на існуючий підрядок: 0.052902900002663955 секунд
  - Час на неіснуючий підрядок: 0.356216799991671 секунд
- **Рабін-Карп:**
  - Час на існуючий підрядок: 0.04376400000182912 секунд
  - Час на неіснуючий підрядок: 0.3357671999838203 секунд

## Висновки

- Найшвидший алгоритм для статті 1: [Боєр-Мур]
- Найшвидший алгоритм для статті 2: [Боєр-Мур]
- Загальний висновок:
  На основі проведених тестів алгоритм Боєра-Мура показав найкращі результати у всіх випадках, як для пошуку існуючого підрядка, так і для пошуку неіснуючого підрядка в обох текстах. Це свідчить про його високу ефективність і оптимальність у задачах пошуку підрядка, особливо коли мова йде про обробку великих текстів або коли підрядки мають складні структури. Завдяки ефективному використанню таблиці "поганих символів" і можливості пропускати великі частини тексту, алгоритм Боєра-Мура забезпечує значну економію часу порівняно з іншими класичними алгоритмами пошуку підрядка.

  Таким чином, алгоритм Боєра-Мура рекомендується як найкращий вибір для задач пошуку підрядка, коли пріоритетом є швидкість виконання.
