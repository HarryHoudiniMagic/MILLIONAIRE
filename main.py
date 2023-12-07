import random
import datetime
def print_millionaire_intro():
    print(f"{'MILLIONAIRE':^40}")
    print(f"{'CREATIVE CQHPUTING':^40}")
    print(f"{'MORRISTOWN, NEW JERSEY':^40}")
    print("\n" * 3)
    # MILLIONAIRE BY CRAIG GUNNETT
    name = input("THIS IS THE GAME OF 'MILLIONAIRE'.  ALL YOU MUST DO IS\n"
                 "TYPE IN YOUR NAME AND ANSWER SOME QUESTIONS.  THE\n"
                 "DECISIONS YOU MAKE WILL DETERMINE HOW MUCH MONEY YOU\n"
                 "MAKE.  AT THE TIME OF YOUR DEATH, YOUR LIFE WILL BE\n"
                 "RATED BY THE AMOUNT OF MONEY YOU MADE THROUGHOUT\n"
                 "YOUR LIFE.  IF YOU HAVE MADE $1,000,000 , YOU WILL BE\n"
                 "A MILLIONAIRE AND WIN THE GAME.  NAME PLEASE: ")
    return name



def generate_random_birthday():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    birth_month = random.choice(months)
    birth_day = random.randint(1, 28)
    birth_year = random.randint(1980, 1985)  # Предполагаем, что возраст персонажа варьируется от 18 до 35 лет
    return f"{birth_month} {birth_day}, {birth_year}"
def generate_birthplace():
    places = ["ON A BIG FARM", "IN A SMALL TOWN"]
    return random.choice(places)

def generate_parents_wealth():
    wealth_status = ["YOUR PARENTS ARE VERY RICH.", "YOUR PARENTS ARE VERY POOR."]
    return random.choice(wealth_status)


def generate_additional_phrase():
    years = random.randint(1998, 2006)  # Предполагаем, что это год ухода из дома, возраст от 18 до 26 лет
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    departure_month = random.choice(months)

    # Создаем объект datetime с датой ухода из дома
    departure_date = datetime.datetime(years, months.index(departure_month) + 1, random.randint(1, 28))
    formatted_date = departure_date.strftime("%b %d, %Y")
    return formatted_date

def generate_random_date(previous_date=None):
    if previous_date:
        # If there is a previous date, increase it by one day
        next_date = previous_date + datetime.timedelta(days=1)
    else:
        # Otherwise, generate a random date
        min_year = 2008
        current_year = 2100
        available_years = list(range(min_year, current_year))

        # Choose a random year from the available range
        random_year = random.choice(available_years)

        # Choose a random month and day
        random_month = random.randint(1, 12)
        random_day = random.randint(1, 28)  # Let's assume 28 days for simplicity

        # Create a datetime object and format the date
        next_date = datetime.datetime(random_year, random_month, random_day)

    # Format the datetime object as a string
    formatted_date = next_date.strftime("%b %d, %Y")
    return formatted_date

def calculate_age(birth_date, formatted_date1):
    birth_datetime = datetime.datetime.strptime(birth_date, "%b %d, %Y")
    formatted_datetime = datetime.datetime.strptime(formatted_date1, "%b %d, %Y")

    age = formatted_datetime.year - birth_datetime.year
    return age

def get_new_job():
    job_options = {
        1: ("TEACHER", 170000, 40000),
        2: ("LAWYER", 800000, 200000),
        3: ("COMPUTER PROGRAMMER", 200000, 50000),
        4: ("BUS DRIVER", 160000, 20000),
        5: ("FOOTBALL PLAYER", 900000, 100000)
    }

    job_number = random.randint(1, 5)

    job_title, base_income, income_variation = job_options[job_number]

    annual_income = base_income + random.randint(0, income_variation) - 10000
    adjusted_income = annual_income - 10000 + random.randint(14000, 26000)

    print(f"YOU GOT A NEW JOB AS A {job_title}. YOU EARN ${annual_income} A YEAR.")
    random_percentage = round(annual_income * random.uniform(0.09, 0.13))
    adjusted_expenses = adjusted_income - random_percentage
    print(f"YOU ADJUST YOUR EXPENSES TO ${adjusted_expenses} A YEAR.")
    return adjusted_expenses

#переменные
def random_event():
    # Выбираем случайную функцию из списка event_functions
    selected_function = random.choice(event_functions)

    # Вызываем выбранную функцию и возвращаем ее результат
    return selected_function()

def gamble_in_vegas(budget):
    bet_amount = int(input("Сколько вы хотите поставить в казино? Введите сумму: "))

    if bet_amount <= 0:
        print("Некорректная сумма для ставки. Попробуйте еще раз.")
        return 0

    print(f"Вы поставили {bet_amount} долларов в казино.")

    # Определение выигрыша или проигрыша случайным образом
    if random.random() > 0.7:
        won_amount = random.randint(0, 2 * bet_amount)
        print(f"Поздравляем, вы выиграли {won_amount} долларов!")
        return won_amount + budget
    else:
        lost_amount = random.randint(0, bet_amount)
        print(f"К сожалению, вы проиграли {lost_amount} долларов.")
        return budget-lost_amount


def buy_coin_offer(budget):
    print("Вам предлагают монету, которая, как утверждают, стоит 100 000 долларов.")
    decision = input("Вы хотите её купить? (Y/N): ").upper()

    if decision == "Y":
        coin_value = random.randint(1, 200000)  # Случайная оценка монеты в пределах до 200 000 долларов
        print(f"Вы купили монету! Её реальная стоимость: {coin_value} долларов.")
        return coin_value + budget
    else:
        print("Вы решили не покупать монету.")
        return 0


def grandfather_legacy(budget):
    dedostavil = random.randint(50000, 200000)  # Сумма наследства от дедушки
    pohorny = random.randint(5000, 20000)  # Затраты на похороны

    print("Ваш дедушка Гровер умер. (Ой!)")
    print(f"Он оставил вам ${dedostavil}, но затраты на похороны составили ${pohorny}.")

    return dedostavil - pohorny + budget
def get_raise(budget):
    R6 = random.randint(1000, 5000)  # Сумма повышения зарплаты

    print(f"Вас повысили на {R6}$.")
    new_salary = random.randint(30000, 80000)  # Новая зарплата после повышения
    print(f"Теперь ваша зарплата составляет {new_salary}$.")

    return new_salary + budget
def stock_market(budget):
    print("#           STOCK NAME         PRICE   SHARES OWNED")
    # Предположим, что у вас есть некоторые переменные, отражающие статус вашего портфеля акций
    # S = [0, 150, 200, 300, 250, 20, 30, 40, 50, 0]
    # Добавлю заглушку для S, чтобы функция была валидной
    S = [0, 150, 200, 300, 250, 20, 30, 40, 50, 0]

    print(f"1 IBM (INCREDIBLY BAD MACHINES)     {S[1]}        {S[5]}")
    print(f"2 USS (USELESS & STINKY STEEL)      {S[2]}        {S[6]}")
    print(f"3 NCR (NO CASH RETURN)              {S[3]}        {S[7]}")
    print(f"4 TWA (TOTAL WRECK AIRLINES)        {S[4]}        {S[8]}")

    # Предположим, что S[9] представляет флаг, показывающий, что были изменения в портфеле акций
    if S[9] == 1:
        return budget  # Если нет изменений, вернуть текущий бюджет

    # Здесь идет логика покупки/продажи акций и изменения бюджета в соответствии с этими действиями
    while True:
        print("DO YOU BUY, SELL ($100 FEE), OR NOT (B,S, OR N)")
        Z = input().upper()

        if Z == "S":
            sell_stock(S)
        elif Z == "N":
            if sum(S[5:9]) > 0:
                return budget
            else:
                print("Вы не владеете акциями.")
        elif Z == "B":
            buy_stock(S)
        else:
            print("Некорректный ввод. Попробуйте снова.")


def sell_stock(S):
    print("STOCK # AND QUANTITY")
    S2, S5 = map(int, input().split())

    if random.random() < 0.5:
        if S5 <= S[3 + S2]:
            S[3 + S2] -= S5
            S[4 + S2] += S5
            M = random.randint(100, 500)
            print(f"Вы продали {S5} акций за {M}$.")
        else:
            print("Недостаточно акций для продажи.")
    else:
        print("Продажа акций не удалась.")


def buy_stock(S, budget):
    print("STOCK # AND QUANTITY")
    S3, S0 = map(int, input().split())

    # Предположим, что цены акций для разных типов акций хранятся в списке S_prices
    # S_prices = [0, 150, 200, 300, 250]
    S_prices = [0, 150, 200, 300, 250]  # Пример цен на акции

    # Проверяем, достаточно ли средств на бюджете для покупки указанного количества акций
    total_cost = S_prices[S3] * S0
    if total_cost <= budget:
        S[4 + S3] += S0  # Увеличиваем количество акций соответствующего типа
        budget -= total_cost  # Уменьшаем бюджет на стоимость покупки акций
        print(f"Вы приобрели {S0} акций за {total_cost}$.")
    else:
        print("Недостаточно средств для покупки указанного количества акций.")

    return budget

import random

def natural_disaster(budget):
    disaster_type = random.choice(["tornado", "airplane crash"])

    if disaster_type == "tornado":
        print("СРОЧНЫЕ НОВОСТИ!!!")
        print(f"ТОРНАДО ПОПАЛО В ДОМ {A}")
    else:
        print(f"САМОЛЕТ УПАЛ В ДОМ {A}")

    D8 = random.randint(1, 50000)
    budget -= D8
    print(f"ПРИЧИНЁННЫЕ УЩЕРБЫ ОЦЕНЕНЫ В ${D8}")

    return budget


def car_accident(budget):
    print("У ВАС ПРОИЗОШЛО ДТП!")

    M3 = random.randint(1000, 3000)  # Затраты на медицину после аварии
    Q7 = random.randint(100, 500)  # Затраты на ремонт после аварии

    print(f"ЗАТРАТЫ НА МЕДИЦИНУ: ${M3}")
    print(f"СТОИМОСТЬ РЕМОНТА: ${Q7}")

    budget = budget - M3 - Q7
    return budget

def boss_event(budget):
    event = random.randint(1, 3)  # Генерация случайного события

    if event == 1:
        # Уменьшение зарплаты
        decrease_amount = random.randint(1000, 3000)
        budget -= decrease_amount
        print(f"ВАМ УМЕНЬШИЛИ ЗАРПЛАТУ НА ${decrease_amount}.")
    elif event == 2:
        # Увольнение
        new_salary = 0
        budget *= random.uniform(0.5, 0.8)
        print("ВАС УВОЛИЛИ!")
        budget = new_salary
    else:
        # Повышение зарплаты
        increase_amount = random.randint(2000, 5000)
        budget += increase_amount
        print(f"ВАМ ПОВЫСИЛИ ЗАРПЛАТУ НА ${increase_amount}.")

    return budget


def vacation_event(budget):
    vacation_cost = random.randint(1000, 3000)

    print("ДОКТОР ПОСОВЕТОВАЛ ВАМ ВЗЯТЬ ОТПУСК.")
    choice = input(f"ПОЕХАТЬ В ОТПУСК ЗА ${vacation_cost}? (Y/N): ").upper()

    if choice == 'Y':
        if budget >= vacation_cost:
            budget -= vacation_cost
            print(f"ВЫ ПОЕХАЛИ В ОТПУСК ЗА ${vacation_cost}.")
        else:
            print("У ВАС НЕДОСТАТОЧНО ДЕНЕГ ДЛЯ ОТПУСКА.")
    elif choice == 'N':
        print("ВЫ РЕШИЛИ НЕ ПОЕХАТЬ В ОТПУСК.")
    else:
        print("НЕКОРРЕКТНЫЙ ВВОД. ПОЖАЛУЙСТА, ВВЕДИТЕ Y (ДА) ИЛИ N (НЕТ).")

    return budget


def stock_market_crash(budget):
    crash_rate = random.uniform(0.1, 0.5)
    loss = int(crash_rate * budget)

    print(f"ФОНДОВЫЙ РЫНОК ОПУСТИЛСЯ НА {crash_rate * 100}%!")
    print(f"ВАШИ АКЦИИ ПОТЕРЯЛИ ${loss} В ОБЩЕЙ СТОИМОСТИ.")

    return budget - loss


def offer_another_job(budget):
    E2 = random.randint(14000, 26000)

    print(f"ВАМ ПРЕДЛОЖИЛИ НОВУЮ РАБОТУ ЗА ${E2} В ГОД.")
    choice = input("ХОТИТЕ ЛИ ВЫ РАБОТАТЬ НА ДВУХ РАБОТАХ? (Y/N): ").upper()

    if choice == "Y":
        print("ВЫ РЕШИЛИ РАБОТАТЬ НА ДВУХ РАБОТАХ!")
        return budget + E2
        print()
    else:
        print("ВЫ РЕШИЛИ НЕ РАБОТАТЬ НА ДВУХ РАБОТАХ.")
        print()


event_functions = [
    gamble_in_vegas, buy_coin_offer, grandfather_legacy, get_raise,
    stock_market, natural_disaster, car_accident, offer_another_job,
    boss_event, vacation_event, stock_market_crash
]


random_birthday = generate_random_birthday()
random_birthplace = generate_birthplace()
random_parents_wealth = generate_parents_wealth()
namep = print_millionaire_intro()
random_leave = generate_additional_phrase()
budget = 0
leave_budet = random.randint(400, 15000)
random_date = generate_random_date()
hp = calculate_age(random_birthday, random_date)
previous_date = None
# Пример использования функции
new_budget = get_new_job()
print(f"New budget after adjusting expenses: ${new_budget}")
print("\n" * 1)
print("O.K., ", namep, ", THIS IS YOUR NEW LIFE!")
print(random_birthplace, "ON ", random_birthday, namep, "IS BORN.")
print(random_parents_wealth, "ON", random_leave, "YOU")
budget += leave_budet
print("LEAVE HOME WITH $", budget)

    # Пример использования функции
new_income = get_new_job()
budget += new_income
print(random_date)
print(hp)
previous_date = random_date
random_date = generate_random_date()
hp = calculate_age(random_birthday,random_date)
print(random_date)
print(hp)
previous_date = random_date
random_date = generate_random_date()
hp = calculate_age(random_birthday,random_date)
print(random_date)
print(hp)


def check_age_until_65_with_events(start_date, birth_date, budget):
    current_date = start_date
    age = calculate_age(birth_date, current_date)

    while age < 65:
        print(f"Текущая дата: {current_date}, Возраст: {age} лет")
        current_date = generate_random_date(current_date)
        age = calculate_age(birth_date, current_date)

        # Вызов случайного события при каждой новой дате
        #budget = random_event(budget)

    print("Персонаж достиг 65 лет!")
    return current_date, age, budget

check_age_until_65_with_events(previous_date, random_birthday,budget)