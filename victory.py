import random
# Функция обработки ответов
def check_answer(answer,real_answer):
    dict_num2month = {1: 'Января', 2: 'Февраля', 3: 'Марта', 4: 'Апреля', 5: 'Мая', 6: 'Июня', 7: 'Июля', 8: 'Августа',
                      9: 'Сентября', 10: 'Октября', 11: 'Ноября', 12: 'Декабря'}
    dict_num2day = {6: 'Шестое', 11: 'Одинадцатое', 7: 'Седьмое', 20: 'Двадцатое', 9: 'Девятое', 21: 'Двадцать первое',
                    15: 'Пятнадцатое', 19: 'Девятнадцатое', 22: 'Двадцать второе', 10: 'Десятое'}
    answer = answer.strip().split('.')
    real_answer = real_answer.strip().split('.')
    try:
        if ((int(answer[0]) == int(real_answer[0])) and  (int(answer[1]) == int(real_answer[1])) and (int(answer[2]) == int(real_answer[2]))):
            return True, None
        else:
            return False, f'Верный ответ: {dict_num2day[int(real_answer[0])]} {dict_num2month[int(real_answer[1])]} {real_answer[2]} года'
    except:
        return False, f'Верный ответ: {dict_num2day[int(real_answer[0])]} {dict_num2month[int(real_answer[1])]} {real_answer[2]} года'

# Логика викторины
def start_game(dict_ans_wrt):
    continue_play = True
    is_right = False
    max_prise = 5
    while continue_play == True:
        prise = 0
        for i in dict_ans_wrt:
            user_answer = input(f'Назовите дату рождения следующего писателя (в формате XX.XX.XXXX): {i} ')
            is_right, message = check_answer(user_answer,dict_ans_wrt[i])

            prise += 1 if is_right else print(message)

        print(f'Правильных ответов: {prise}')
        print(f'Ошибок: {max_prise-prise}')
        print(f'Процент верных ответов: {(prise/max_prise)*100}%')
        print(f'Процент неверных ответов: {(max_prise-prise)*100/max_prise}%')
        if input('Хотите сыграть ещё раз? ( Y/N )') == 'N':
            continue_play = False

def start():
    answers = ['06.06.1799','11.11.1821' ,'20.03.1809','09.10.1828','07.09.1870','21.06.1948','15.10.1814','19.07.1893','22.11.1801','10.12.1821']
    writers = ['Пушкин'    ,'Достоевский','Гоголь'    ,'Толстой'   ,'Куприн'    ,'Сапковский','Лермонтов' ,'Маяковский','Даль'      ,'Некрасов']


    # Создаём словарь с рандомными вопросами
    set_of_questions = random.sample(list(range(10)),5)
    dict_ans_wrt = {}
    for i in set_of_questions:
        dict_ans_wrt[writers[i]] = answers[i]

    # Запускаем игру со сгенерированными вопросами
    start_game(dict_ans_wrt)