import random
from faker import Faker
from faker_airtravel import AirTravelProvider
from faker_vehicle import VehicleProvider

from model_dataclasses import Car, Airport, Person


def generate_people(n: int, male_ratio: float = 0.5, locale: str = "en_US",
                    unique: bool = False, min_age: int = 0, max_age: int = 100) -> list[Person]:
    assert n > 0
    assert 0 < male_ratio < 1
    assert 0 <= min_age <= max_age

    fake = Faker(locale)
    people = []
    for i in range(n):
        male = random.random() < male_ratio
        generator = fake if not unique else fake.unique
        people.append(Person(
            "P-" + (str(i).zfill(6)),
            generator.name_male() if male else generator.name_female(),
            random.randint(min_age, max_age),
            male))

    return people
