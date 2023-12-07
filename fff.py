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




    def age_up(self, event_date):
        self.age = event_date.year - self.birth_year
        if self.age >= 65 and random.random() < 0.05:
            print(f"К сожалению, {self.name} умер от старости.")
            return True
        return False

    def earn_money(self, amount):
        self.money += amount

    def random_event(self, last_event_date):
        current_year = datetime.datetime.now().year
        last_event_date = datetime.datetime(last_event_date.year, last_event_date.month, last_event_date.day)
        event_date = max(last_event_date, datetime.datetime(2011, 1, 1)) + datetime.timedelta(
            days=random.randint(1, 365 * 10))

        while event_date.year <= 2010:
            event_date = max(last_event_date, datetime.datetime(2011, 1, 1)) + datetime.timedelta(
                days=random.randint(1, 365 * 10))

        events = [
            "Вы нашли сокровище!",
            "Вас ограбили, у вас украли деньги.",
            "Вы выиграли лотерею!",
            "Вы потратили деньги на дорогую медицинскую процедуру."
        ]

        while True:
            event = random.choice(events)
            if event_date != last_event_date:
                break

        age_at_event = event_date.year - self.birth_year

        print(f"{event_date.strftime('%Y-%m-%d')} | Budget: {self.money} || age {age_at_event} |{event}")

        if "сокровище" in event:
            self.earn_money(10000)
        elif "ограбили" in event:
            self.earn_money(-500)
        elif "лотерею" in event:
            self.earn_money(2000)
        elif "медицинскую процедуру" in event:
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
    print("O.K., ", name, ", THIS IS YOUR NEW LIFE!")
    print(places, "ON ",month_number_to_name[birth_month],  " ", birth_day," ,",birth_year,", ", name," IS BORN.")
    print(wealth_status, "ON", month_number_to_name[ushel_month],  " ", ushel_day," ,",ushel_year,", ", "YOU")
    print("LEAVE HOME WITH $", leave_budet)
    while character.money < goal_money:
        last_event_date = character.random_event(last_event_date)  # Передаем последнюю дату события
        if character.age >= 65: # проверка смерти героя
            print(f"К сожалению, {character.name} умер от старости.")
            break

    if character.money >= goal_money:
        print(f"Поздравляем, {character.name} заработал миллион!")
    else:
        print(f"{character.name} не достиг миллиона и умер.")

if __name__ == "__main__":
    play_game()
