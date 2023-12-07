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




    def age_up(self):
        self.age += 1
        if self.age >= 65 and random.random() < 0.05:
            print(f"К сожалению, {self.name} умер от старости.")
            return True
        return False

    def earn_money(self, amount):
        self.money += amount

    def random_event(self, last_event_date):
        event_date = last_event_date + datetime.timedelta(days=random.randint(1, 365*10))  # Генерируем новую дату события
        events = [
            "Вы нашли сокровище!",
            "Вас ограбили, у вас украли деньги.",
            "Вы выиграли лотерею!",
            "Вы потратили деньги на дорогую медицинскую процедуру."
        ]

        while True:
            event = random.choice(events)
            if event_date != last_event_date:  # Проверяем, что новая дата события отличается от предыдущей
                break

        print(f"{event_date}: {event}")
        if "сокровище" in event:
            self.earn_money(10000)
        elif "ограбили" in event:
            self.earn_money(-500)
        elif "лотерею" in event:
            self.earn_money(2000)
        elif "медицинскую процедуру" in event:
            self.earn_money(-3000)

        # При наступлении нового события увеличиваем возраст на один год
        if event_date.year != self.birth_year:
            self.age_up()
            #print(f"Возраст {self.name}: {self.age}")
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
    name = input("Введите имя персонажа: ")
    birth_year, birth_month, birth_day = generate_random_date()
    ushel_year, ushel_month,ushel_day, places, wealth_status, leave_budet =history()
    character = Character(name, birth_year, birth_month, birth_day, ushel_year, ushel_month,ushel_day, places, wealth_status, leave_budet)
    goal_money = 1000000
    #print(birth_year,  places ,leave_budet)
    last_event_date = datetime.date(character.birth_year, character.birth_month, character.birth_day)

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
