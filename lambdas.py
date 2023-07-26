people = [
    {"name": "Paul", "age": 25},
    {"name": "Rory", "age": 21},
    {"name": "Caitlin", "age": 23},
]

people.sort(key=lambda person: person['age'])

for person in people:
    print(f"{person['name']}: {person['age']}")


def call(func):
    func()


def add(x, y):
    return x + y


call(lambda: add(2, 3))


