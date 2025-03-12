import datetime
import random

def get_order_test_data():
    random_date= datetime.date.today() + datetime.timedelta(days=random.randint(3,50))
    return{
        'name': random.choice(['Алиса','Драко','Кеша']),
        'surname': random.choice(['Малфой','Ельцин','Пупкин']),
        'address': f'г.Москва, ул.Восточная {random.randint(1,80)} кв.{random.randint(1,15)}',
        'station':random.choice(["Царицыно", "Сокол", "Лубянка"]),
        'phone': "+79"+ "".join([str(random.randint(0,9)) for _ in range (9)]),
        'data':"%02d.%02d.%04d" % (random_date.day, random_date.month, random_date.year),
        'duration': random.choice ([
            "сутки",
            "двое суток",
            "трое суток",
            "четверо суток",
            "пятеро суток",
            "шестеро суток",
            "семеро суток"
        ]),
        'color': random.choice(['black','grey']),
        'comment': "Хочу на море"

    }