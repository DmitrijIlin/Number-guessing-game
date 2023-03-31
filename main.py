from random import choice, randint
import time


# приглашение в игру
def ask_game():
    count = 0
    phrases_questions = ('Я тебя не понял!', 'Повтори ещё разок!', 'Что так сложно ответить на вопрос?',
                         'Даю тебе последний шанс!!!', 'Ааааааа... ВСЁ, НЕ ХОЧУ С ТОБОЙ ИГРАТЬ!!!!')

    while (question := input("Введи 'да' или 'нет': ").lower()) not in ('да', 'lf', 'нет', 'ytn'):
        print(phrases_questions[count])
        count += 1
        if count > 4:
            break
    else:
        if question in ('нет', 'ytn'):
            print('Ну что ж, как передумаешь, обязательно приходи!;)')
        else:
            print()
            start()


# проверка значеня диапазона на число
def is_valid_range(value):
    if len(value) > 0 and (value.isdigit() or (value[0] == '-' and value[1:].isdigit())):
        return True
    print('Ты ввёл не число! Попробуй ещё раз.')
    start()


# проверка второго значения диапазона на число и обоих значений на равенство
def is_valid_ranges(value1, value2):
    is_valid_range(value2)
    if value1 != value2:
        return True
    print('Ты ввел одинаковые числа. Я же говорил, что так играть мы не сможем!')
    start()


# запуск игры
def start():
    x = input('Введи первую границу диапазона: ')
    is_valid_range(x)
    y = input('Введи вторую границу диапазона: ')
    if is_valid_ranges(x, y):
        first_range, second_range = min(int(x), int(y)), max(int(x), int(y))
        game(first_range, second_range)


# ввод и проверка угадываемого числа
def enter_and_check_num(x, y):
    while True:
        num = input('Введи число: ')
        if not (num.isdigit() or (num[0] == '-' and num[1:].isdigit())):
            print('Значение должно быть числом!')
            continue
        entered_num = int(num)
        if not x <= entered_num <= y:
            print(f'Значение должно быть в диапазоне от {x} до {y}')
            continue
        return int(num)


# алгоритм игры
def game(min_range, max_range):
    phrases_first_try = ('Скажи честно, ты подглядывал?', 'Ты читер!', 'С первого раза? Так не бывает!')
    phrases_too_soon = ('Ого, так быстро!', 'Да ты волшебник! Ты угадал моё число',
                        'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!')
    phrases_guessed = ('Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)')
    phrases_too_much = ('Ох, слишком много! Попробуй еще раз', 'Многовато будет!', 'Ого-го, это слишком много!',
                        'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!', 'Холодно!')
    phrases_too_little = ('Ох, слишком мало! Попробуй еще раз', 'Маловато будет!', 'Эх, это слишком мало!',
                          'Мало!', 'Бери выше', 'Маловато!', 'Нужно большее число!', 'Холодно!')
    phrases_almost = ('Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок',
                      'Ты уже рядом', 'Ну же, почти', 'Теплее!')

    number = randint(min_range, max_range)
    print(f'Я загадал число от {min_range} до {max_range}. Попробуй угадать!\n')
    count = 1

    while number != (entered_num := enter_and_check_num(min_range, max_range)):
        if abs(entered_num - number) < 4:
            print(choice(phrases_almost))
        elif entered_num - number >= 5:
            print(choice(phrases_too_much))
        else:
            print(choice(phrases_too_little))
        count += 1

    else:
        if count == 1:
            print(f'{choice(phrases_first_try)}\n')
        elif 1 < count < 5:
            print(f'{choice(phrases_too_soon)}\n')
        else:
            print(f'{choice(phrases_guessed)}\n')
        time.sleep(1)
        print('Хочешь сыграть ещё разок?')
        ask_game()


print('Приветствую тебя в игре числовая угадайка! Давай я ознакомлю тебя с правилами игры!\n')
time.sleep(1)
print('Я загадаю число, а ты будешь его отгадывать.')
print('Диапазон чисел ты выберешь сам.')
print('Числа не должны равняться друг другу.\n')
time.sleep(1.5)
print('Не желаешь сыграть в игру?')
ask_game()
