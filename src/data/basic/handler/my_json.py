import json
import os
from typing import cast, Type

from data.basic.generator import generate_people
from data.basic.model_dataclasses import Person, Airport, Car


def write_people(people: list[Person], path: str,
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump(
            [person.__dict__ for person in people],
            file, indent=2 if pretty else None)


def read_people(path: str, file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension)) as file:
        """
        return [
            Person(person["id"], person["name"],
                   person["age"], person["male"])
            for person in json.load(file)
        ]
        """

        def convert(d: dict) -> Person:
            return Person(**d)

        # return json.load(file, object_hook=lambda d: Person(convert))
        return json.load(file, object_hook=lambda d: Person(**d))


def read_cars(path: str, file_name: str = "cars", extension: str = ".json") -> list[Car]:
    file_name = file_name if file_name is not None else "cars"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "r") as file:
        return [Car(document["plate"], document["type"], int(document["year"]), bool(document["automatic"]))
                for document in json.load(file)]


def write_cars(cars: list[Car], path: str, file_name: str = "cars", extension: str = ".json", pretty=True) -> None:
    file_name = file_name if file_name is not None else "cars"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([car.__dict__ for car in cars], file, indent=2 if pretty else None)


def read_airports(path: str, file_name: str = "airports", extension: str = ".json") -> list[Airport]:
    file_name = file_name if file_name is not None else "airports"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "r") as file:
        return [Airport(doc["name"], doc["code"], doc["city"], doc["state"], doc["country"])
                for doc in json.load(file)]


def write_airports(airports: list[Airport], path: str, file_name: str = "airports", extension: str = ".json",
                   pretty=True) -> None:
    file_name = file_name if file_name is not None else "airports"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump([airport.__dict__ for airport in airports], file, indent=2 if pretty else None)


def read(entity_type: Type[object], path, file_name: str = None, extension: str = None) -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, extension=extension)
    elif entity_type == Car:
        return read_cars(path, file_name=file_name, extension=extension)
    elif entity_type == Airport:
        return read_airports(path, file_name=file_name, extension=extension)
    else:
        raise RuntimeError("Unknown type of entity")


def write(entities: list[object], path, file_name: str = None, extension: str = None, pretty=True) -> None:
    if isinstance(entities[0], Person):
        return write_people([cast(Person, e) for e in entities],
                            path, file_name=file_name,
                            extension=extension, pretty=pretty)
    elif isinstance(entities[0], Car):
        return write_cars([cast(Car, e) for e in entities],
                          path, file_name=file_name,
                          extension=extension, pretty=pretty)
    elif isinstance(entities[0], Airport):
        return write_airports([cast(Airport, e) for e in entities],
                              path, file_name=file_name,
                              extension=extension, pretty=pretty)
    else:
        raise RuntimeError("Unknown type of entity")

if __name__ == "__main__":
    people = generate_people(10)
    write_people(people, "D:/", pretty=False)
    for person in read_people("D:/"):
        print(person)
