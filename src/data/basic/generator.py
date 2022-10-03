import random

from faker import Faker
from faker_airtravel import AirTravelProvider

from data.basic.model_classes import Person, Car, Airport


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


from faker_vehicle import VehicleProvider


def generate_cars(n: int,
                  automatic_ratio: float = 0.2,
                  locale: str = "hu_HU",
                  unique: bool = False,
                  min_year: int = 1950,
                  max_year: int = 2022) -> list[Car]:
    assert n >= 1
    assert 0 <= automatic_ratio <= 1
    assert min_year >= 1950
    assert min_year <= max_year <= 2022

    fake_plate = Faker(locale)
    fake_plate.add_provider(VehicleProvider)

    fake_type = Faker(locale)
    fake_type.add_provider(VehicleProvider)

    if unique:
        fake_plate = fake_plate.unique

    cars = []
    for i in range(n):
        car = Car(
            fake_plate.license_plate(),
            fake_type.vehicle_make(),
            random.randint(min_year, max_year),
            random.random() < automatic_ratio
        )
        cars.append(car)
    return cars


def generate_airports(n: int, country: str = None,
                      city: str = None,
                      unique: bool = False,
                      attempts: int = None) -> list[Airport]:
    fake = Faker()
    fake.add_provider(AirTravelProvider)

    airports = []
    for i in range(n if attempts is None else attempts):
        values = fake.airport_object()
        airport = Airport(
            values["icao"],
            values["airport"],
            values["city"],
            values["state"],
            values["country"]
        )

        if len(airports) == n:
            break
        if unique and airport in airports:
            continue
        if country is not None and airport.country != country:
            continue
        if city is not None and airport.city != city:
            continue

        airports.append(airport)
    return airports


if __name__ == "__main__":
    cars = generate_cars(10, unique=True)
    for car in cars:
        print(car)

    print("===")
    airports = generate_airports(3, country="Germany",
                                 unique=True, attempts=4)
    for airport in airports:
        print(airport)

    """
    d = dict()
    d["alma"] = "apple"
    d["alma"] = "manzana"
    d["banán"] = "banana"

    d["alma"]
    """
