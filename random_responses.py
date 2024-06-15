import random


def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "I don't get you, please write it correctly?",
        "I'm sorry, I didn't quite understand that.",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]