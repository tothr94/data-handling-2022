from typing import Type, cast
import os
import csv

from data.basic.model_dataclasses import Person, Car, Airport


def read_people(path: str, file_name: str = "people", extension: str = ".csv", delimiter: str = ";") -> list[Person]:
    file_name = file_name if file_name is not None else "people"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Person(row["id"], row["name"], int(row["age"]), bool(row["male"])) for row in rows]


def write_people(people: list[Person], path: str, file_name: str = "people.csv",
                 extension: str = ".csv", heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "people"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "male"], delimiter=delimiter)
        if heading:
            writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)


def read_cars(path: str, file_name: str = "cars", extension: str = ".csv", delimiter: str = ";") -> list[Car]:
    file_name = file_name if file_name is not None else "cars"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Car(row["plate"], row["type"], int(row["year"]), bool(row["automatic"])) for row in rows]


def write_cars(cars: list[Car], path: str, file_name: str = "cars", extension: str = ".csv",
               heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "cars"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["plate", "type", "year", "automatic"], delimiter=delimiter)
        if heading:
            writer.writeheader()
        for car in cars:
            writer.writerow(car.__dict__)


def read_airports(path: str, file_name: str = "airports", extension: str = ".csv",
                  delimiter: str = ";") -> list[Airport]:
    file_name = file_name if file_name is not None else "airports"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows = csv.DictReader(file, delimiter=delimiter)
        return [Airport(row["code"], row["name"], row["city"], row["state"], row["country"]) for row in rows]


def write_airports(airports: list[Airport], path: str, file_name: str = "airports", extension: str = ".csv",
                   heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "airports"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "code", "city", "state", "country"], delimiter=delimiter)
        if heading:
            writer.writeheader()
        for airport in airports:
            writer.writerow(airport.__dict__)


def read(entity_type: Type[object], path: str, file_name: str = None, delimiter: str = ";") -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Car:
        return read_cars(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Airport:
        return read_airports(path, file_name=file_name, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")


def write(entities: list[object], path: str, file_name: str = None, extension: str = None,
          heading: bool = True, delimiter: str = ";") -> None:
    if isinstance(entities[0], Person):
        return write_people([cast(Person, e) for e in entities], path, file_name=file_name, extension=extension,
                            heading=heading, delimiter=delimiter)
    elif isinstance(entities[0], Car):
        return write_cars([cast(Car, e) for e in entities], path, file_name=file_name, extension=extension,
                          heading=heading, delimiter=delimiter)
    elif isinstance(entities[0], Airport):
        return write_airports([cast(Airport, e) for e in entities], path, file_name=file_name, extension=extension,
                              heading=heading, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")
