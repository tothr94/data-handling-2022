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
            "O-" + (str(i).zfill(6)),
            generator.name_male() if male else generator.name_female(),
            random.randint(min_age, max_age),
            male))

    return people


def generate_cars(n: int, automatic_ratio: float = 0.2, locale: str = "hu_HU", unique: bool = False,
                  min_year: int = 1950, max_year: int = 2021) -> list[Car]:
    assert n > 0
    assert 0 < automatic_ratio < 1
    assert 1950 <= min_year
    assert min_year <= max_year <= 2021

    fake_plate = Faker(locale)
    fake_plate.add_provider(VehicleProvider)
    if unique:
        fake_plate = fake_plate.unique
    fake_type = Faker()
    fake_type.add_provider(VehicleProvider)

    cars = []
    for i in range(n):
        automatic = random.random() < automatic_ratio
        cars.append(Car(
            fake_plate.license_plate(),
            fake_type.vehicle_make(),
            random.randint(min_year, max_year),
            automatic))

    return cars


def generate_airports(n: int, country: str = None, city: str = None,
                      unique: bool = False, attempts: int = None) -> list[Airport]:
    assert n > 0
    assert attempts is None or attempts >= n

    fake = Faker()
    fake.add_provider(AirTravelProvider)

    airports = []
    for i in range(n if attempts is None else attempts):
        values = fake.airport_object()

        actual = Airport(
            values["icao"],
            values["airport"],
            values["city"],
            values["state"],
            values["country"])

        if len(actual.code) == 0:
            continue
        if country is not None and country != actual.country:
            continue
        if city is not None and city != actual.city:
            continue
        if unique and actual in airports:
            continue

        airports.append(actual)

    return airports
