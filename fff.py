import random
import datetime

class Character:
    def __init__(self, name, birth_year, birth_month, birth_day, ushel_year, ushel_month, ushel_day, places, wealth_status, leave_budet):
        self.name = name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.age = datetime.datetime.now().year - birth_year
        self.money = 0
        self.ushel_year = ushel_year
        self.ushel_month = ushel_month
        self.ushel_day = ushel_day
        self.places = places
        self.wealth_status = wealth_status

    def get_new_job(self):
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
        print (adjusted_expenses, adjusted_income, random_percentage)
        # Увеличиваем self.money на доход от новой работы
        self.money += annual_income

        print(f"YOU ADJUST YOUR EXPENSES TO ${adjusted_expenses} A YEAR.")
        return adjusted_expenses

    def age_up(self, event_date):
        self.age = event_date.year - self.birth_year
        if self.age >= 65 and random.random() < 0.5:
            print(f"К сожалению, {self.name} умер от старости.")
            return True
        return False

    def earn_money(self, amount):
        self.money += amount

    def coin(self):
        print("YOU ARE OFFERED A COIN SUPPOSEDLY WORTH $100,000.")
        otvet = input("DO YOU BUY IT? (Y/N): ")

        if otvet.upper() == "Y":
            coin_value = random.randint(1, 200000)  # Генерация случайной стоимости монеты от 1 до 200000
            print(f"The coin's value is: ${coin_value}")
            print(f"YOU NOW HAVE {self.money}")
            if coin_value < 100000:
                lost_money = 100000 - coin_value
                self.earn_money(-lost_money)
                return (f"YOU LOST ${lost_money}.")

            else:
                earned_money = coin_value - 100000
                self.earn_money(earned_money)
                return (f"YOU EARNED ${earned_money}.")
        else:
            return "You chose not to buy the coin."

    def vaction(self):
        otvet1 = input("THE DOCTOR SAYS YOU NEED A VACATION.  DO YOU GO: ")

        if otvet1.upper() == "Y":
            VACATION_value = random.randint(1, 3000)  # Генерация случайной стоимости монеты от 1 до 200000
            print(f"GOOD, THE VACATION COSTS ${VACATION_value}")
            self.earn_money(-abs(VACATION_value))
            print(f"YOU NOW HAVE {self.money}")
        else:
            return 0
    def granny(self):
        nasl = abs(random.randint(7000, 40000))
        pohorony = abs(random.randint(10000, 42000))
        print("YOUR GRANDFATHER GROVERS JUST DIED. (OH!)  HE LEFT")
        print(f"YOU $ {nasl}, BUT FUNERAL EXPENSES ARE ${pohorony}")
        dohod = nasl - pohorony
        self.earn_money(dohod)

    def gamble(self):
        while True:
            try:
                bet = float(input("YOU GO TO LAS VEGAS TO GAMBLE. HOW MUCH DO YOU BET? "))
                if bet <= 0:
                    return 0

                chance = random.random()  # случайное число от 0 до 1

                if chance > 0.7:
                    loss_amount = -int(random.random() * bet)
                    print(f"HA! HA! YOU LOST ${abs(loss_amount)}")
                    self.earn_money(abs(loss_amount) * -1 )
                    return abs(loss_amount)
                else:
                    win_amount = int((random.random() + random.random()) * bet)
                    print(f"YOU WON ${win_amount}")
                    self.earn_money(abs(win_amount))
                    return abs(win_amount)
            except ValueError:
                print("Please enter a valid number.")

    def ill(self):
        ill = ["A HEART ATTACK", "LEUKEMIA", "CANCER"]
        illness = random.choice(ill)
        print(f"OH! YOU JUST GOT {illness}")
        if illness == "A HEART ATTACK":
            self.earn_money(abs(random.randint(3000, 5000)) * -1)
        elif illness == "CANCER":
            self.earn_money(abs(random.randint(50000, 150000)) * -1)
        elif illness == "LEUKEMIA":
            print(f"OH NO! {self.name} has been diagnosed with LEUKEMIA. The game ends.")
            return "LEUKEMIA"
    def generation(self):
        tamm = [abs(random.randint(1980, 50001)), abs(random.randint(1980, 20001))]
        return random.choice(tamm)

    def random_event(self, last_event_date):
        current_year = datetime.datetime.now().year
        last_event_date = datetime.datetime(last_event_date.year, last_event_date.month, last_event_date.day)
        event_date = max(last_event_date, datetime.datetime(2011, 1, 1)) + datetime.timedelta(
            days=random.randint(1, 365 * 10))

        while event_date.year <= 2010:
            event_date = max(last_event_date, datetime.datetime(2011, 1, 1)) + datetime.timedelta(
                days=random.randint(1, 365 * 10))

        events = [
            #"Вы нашли сокровище!",
            #"A TORNADO HAS JUST HIT THE HOME OF ",
            #"YOU JUST HAD A CAR ACCIDENT!  MEDICAL COSTS",
            #"Вы потратили деньги на дорогую медицинскую процедуру.",
            #"YOU GO TO LAS VEGAS TO GAMBLE. HOW MUCH DO YOU BET?",
            #"YOU ARE OFFERED A COIN SUPPOSEDLY WORTH $100,000.",
            #"THE DOCTOR SAYS YOU NEED A VACATION.  DO YOU GO",
            #"YOUR HOME HAS BEEN ROBBED OF GOODS WORTH",
            #"AN AIRPLANE HAS JUST CRASHED INTO THE HOME OF ",
            #"YOUR GRANDFATHER GROVERS JUST DIED. (OH!)  HE LEFT"
            "OH! YOU JUST GOT "
        ]


        while True:
            event = random.choice(events)
            if event_date != last_event_date:
                break

        age_at_event = event_date.year - self.birth_year

        print(f"{event_date.strftime('%Y-%m-%d')} | Budget: {self.money} || age {age_at_event} |{event}")

        if "GROVERS" in event:
            self.granny()
        elif "OH!" in event:
            self.ill()
        elif "VEGAS" in event:
            self.gamble()
        elif "COIN" in event:
            self.coin()
        elif "VACATION" in event:
            self.vaction()
        elif "TORNADO" in event:
            t = self.generation()
            print(f"A TORNADO HAS JUST HIT THE HOME OF $ {t}")
            self.earn_money(t * -1)
            print(f"YOU NOW HAVE $ {self.money}")
        elif "AIRPLANE" in event:
            t = self.generation()
            print(f"AN AIRPLANE HAS JUST CRASHED INTO THE HOME OF $ {t}")
            self.earn_money(t * -1)
            print(f"YOU NOW HAVE $ {self.money}")
        elif "ROBBED" in event:
            t = self.generation()
            print(f"YOUR HOME HAS BEEN ROBBED OF GOODS WORTH $ {t}")
            self.earn_money(t * -1)
            print(f"YOU NOW HAVE $  {self.money}")
        elif "CAR" in event:
            t = abs(random.randint(1000, 3000))
            print(f"YOU JUST HAD A CAR ACCIDENT!  MEDICAL COSTS $ {t}")
            self.earn_money(t * -1)
        elif "" in event:
            self.earn_money(-3000)

        if event_date.year != self.birth_year:
            self.age = age_at_event
        return event_date


def generate_random_date():
    birth_year = random.randint(1980, 1990)
    birth_month = random.choice(range(1, 13))  # Выбираем месяц от 1 до 12
    birth_day = random.randint(1, 28)  # Предполагаем, что максимальное количество дней в месяце - 28

    return birth_year, birth_month, birth_day,

def history():
    ushel_year = random.randint(2006, 2010)  # Выбираем год рождения от 1980 до 2005
    ushel_month = random.choice(range(1, 13))  # Выбираем месяц от 1 до 12
    ushel_day = random.randint(1, 28)
    places = ["ON A BIG FARM", "IN A SMALL TOWN"]
    wealth_status = ["YOUR PARENTS ARE VERY RICH.", "YOUR PARENTS ARE VERY POOR."]
    leave_budet = random.randint(400, 10000)
    return ushel_year, ushel_month, ushel_day, random.choice(places), random.choice(wealth_status), leave_budet

def dead(character):
    print(f"К сожалению, {character.name} умер.")
    return True


def play_game():
    print(f"{'MILLIONAIRE':^40}")
    print(f"{'CREATIVE CQHPUTING':^40}")
    print(f"{'MORRISTOWN, NEW JERSEY':^40}")
    print("\n" * 3)
    name = input("THIS IS THE GAME OF 'MILLIONAIRE'.  ALL YOU MUST DO IS\n"
                 "TYPE IN YOUR NAME AND ANSWER SOME QUESTIONS.  THE\n"
                 "DECISIONS YOU MAKE WILL DETERMINE HOW MUCH MONEY YOU\n"
                 "MAKE.  AT THE TIME OF YOUR DEATH, YOUR LIFE WILL BE\n"
                 "RATED BY THE AMOUNT OF MONEY YOU MADE THROUGHOUT\n"
                 "YOUR LIFE.  IF YOU HAVE MADE $1,000,000 , YOU WILL BE\n"
                 "A MILLIONAIRE AND WIN THE GAME.  NAME PLEASE: ")
    birth_year, birth_month, birth_day = generate_random_date()
    ushel_year, ushel_month,ushel_day, places, wealth_status, leave_budet =history()
    character = Character(name, birth_year, birth_month, birth_day, ushel_year, ushel_month,ushel_day, places, wealth_status, leave_budet)
    month_number_to_name = {
        1: 'JAN',
        2: 'FEB',
        3: 'MAR',
        4: 'APR',
        5: 'MAY',
        6: 'JUN',
        7: 'JUL',
        8: 'AUG',
        9: 'SEP',
        10: 'OCT',
        11: 'NOV',
        12: 'DEC'
    }
    goal_money = 1000000
    last_event_date = datetime.date(character.birth_year, character.birth_month, character.birth_day)
    print(f"New budget after adjusting expenses: $")
    print("\n" * 1)
    print("O.K., ", name,", THIS IS YOUR NEW LIFE!")
    print(places, "ON ",month_number_to_name[birth_month],  " ", birth_day," ,",birth_year,", ", name," IS BORN.")
    print(wealth_status, "ON", month_number_to_name[ushel_month],  " ", ushel_day," ,",ushel_year,", ", "YOU")
    print("LEAVE HOME WITH $", leave_budet)
    adjusted_expenses = character.get_new_job()


    while character.money < goal_money:
        last_event_date = character.random_event(last_event_date)  # Передаем последнюю дату события
        illness_status = character.ill()
        if character.age >= 100: # проверка смерти героя
            print(f"К сожалению, {character.name} умер от старости.")
            break
        elif illness_status == "LEUKEMIA":
            print(f"К сожалению, {character.name} умер от 8====D.")
            break
        elif illness_status == "HEART ATTACK" and character.age >= 70:
            print(f"AGE OF , {character.age} ."
                  f"YOU HAD $ {character.money}")


    if character.money >= goal_money:
        print(f"Поздравляем, {character.name} заработал миллион!")
    else:
        print(f"{character.name} не достиг миллиона и умер.")

if __name__ == "__main__":
    play_game()
