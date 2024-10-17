"""
    4. How to structure this small program :)

Problem statement:
What the program needs to do (requirements):
    1. Sort the cities
    2. Display the list of cities
    4. Add a city from the console
    5. Add a number of random cities to the list (the number is read from the console)
    6. Quit
"""

def create_city(name: str, population: int, country: str, continent: str):
    # City represented as a Python list
    # return [name, population, country, continent]

    # City represented as a Python dict
    # dict is a key-to-value mapping where keys are unique

def get_name(city) -> str:
    # for the list representation
    # return city[0]
    # for the dict representation
    return city["name"]

def get_population(city) -> int:
    # for the list representation
    # for the dict representation

def get_country(city) -> str:
    # for the list representation
    # for the dict representation
    return city["country"]

def get_continent(city) -> str:
    # for the list representation
    # for the dict representation
    return city["continent"]

def to_str(city) -> str:

# --- Functions that implement program requirements

# --- User interface functions

def add_city(city_list: list) -> None:
    name = input("City name =")
    while True:
        try:
            pop = int(input("City population ="))
            break # If we get to this point, it means there was no error. Try it!
        except ValueError:
        print("Population must be an integer")
    country = input("Country =")
    continent = input("Continent =")

    # TODO What to do with duplicate cities?
    new_city = create_city(name, pop, country, continent)
    city_list.append(new_city)


def display_all_cities(city_list: list) -> None:
    for city in city_list:
        print(to_str(city))


def start():
    # NOTE We don't want to start with an empty list, so let's add something

    # This is where we keep all the cities
    # It's not a global variable
    cities_list = []


    while True:
        print("1. Display the list of cities")
        print("0. Quit")

        command = input(">").strip()

        if command == "1":
            # We want to add a function for each requirement
            # This makes the main loop easier to understand
            display_all_cities(cities_list)
        elif command == "2":
        elif command == "0":
            break
        else:


start()

# print(to_str(my_city))