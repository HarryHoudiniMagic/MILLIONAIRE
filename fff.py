import random
import datetime

class Character:
    def __init__(self, name, birth_year, birth_month, birth_day):
        self.name = name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.age = datetime.datetime.now().year - birth_year
        self.money = 1000

    def age_up(self):
        self.age += 1
        if self.age >= 65 and random.random() < 0.3:
            print(f"К сожалению, {self.name} умер от старости.")
            return True
        return False

    def earn_money(self, amount):
        self.money += amount

    def random_event(self):
        events = [
            "Вы нашли сокровище!",
            "Вас ограбили, у вас украли деньги.",
            "Вы выиграли лотерею!",
            "Вы потратили деньги на дорогую медицинскую процедуру."
        ]
        event = random.choice(events)
        print(f"Сегодня {datetime.date.today()}: {event}")
        if "сокровище" in event:
            self.earn_money(10000)
        elif "ограбили" in event:
            self.earn_money(-500)
        elif "лотерею" in event:
            self.earn_money(2000)
        elif "медицинскую процедуру" in event:
            self.earn_money(-3000)

def generate_random_date():
    birth_year = random.randint(1980, 2005)  # Выбираем год рождения от 1980 до 2005
    birth_month = random.choice(range(1, 13))  # Выбираем месяц от 1 до 12
    birth_day = random.randint(1, 28)  # Предполагаем, что максимальное количество дней в месяце - 28
    return birth_year, birth_month, birth_day

def play_game():
    name = input("Введите имя персонажа: ")
    birth_year, birth_month, birth_day = generate_random_date()
    character = Character(name, birth_year, birth_month, birth_day)
    goal_money = 1000000

    while character.money < goal_money:
        if character.age_up():
            break
        character.random_event()

    if character.money >= goal_money:
        print(f"Поздравляем, {character.name} заработал миллион!")
    else:
        print(f"{character.name} не достиг миллиона и умер.")

if __name__ == "__main__":
    play_game()
