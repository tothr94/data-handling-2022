import typing
import os
import csv

from data.basic.model_dataclasses import Person, Car, Airport


def read_people(path: str, file_name: str = "people.csv", heading: bool = True, delimiter: str = ";") -> list[Person]:
    with open(os.path.join(path, file_name if file_name is not None else "people.csv"), "r") as file:
        rows = csv.reader(file, heading=heading, delimiter=delimiter)
        return [Person(row[0], row[1], int(row[2]), bool(row[3])) for row in rows]


def write_people(people: list[Person], path: str, file_name: str = "people.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "people.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for person in people:
            writer.writerow([person.id, person.name, person.age, person.male])


def read_cars(path: str, file_name: str = "cars.csv", delimiter: str = ";") -> list[Car]:
    with open(os.path.join(path, file_name if file_name is not None else "cars.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [Car(row[0], row[1], int(row[2]), bool(row[3])) for row in rows]


def write_cars(cars: list[Car], path: str, file_name: str = "cars.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "cars.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for car in cars:
            writer.writerow([car.plate, car.type, car.year, car.automatic])


def read_airports(path: str, file_name: str = "airports.csv", delimiter: str = ";") -> list[Airport]:
    with open(os.path.join(path, file_name if file_name is not None else "airports.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [Airport(row[0], row[1], row[2], row[3], row[4]) for row in rows]


def write_airports(airports: list[Airport], path: str, file_name: str = "airports.csv", delimiter: str = ";") -> None:
    with open(os.path.join(path, file_name if file_name is not None else "airports.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for airport in airports:
            writer.writerow([airport.code, airport.name, airport.city, airport.state, airport.country])


def read(entity_type: typing.Type[object], path: str, file_name: str = None, delimiter: str = ";") -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Car:
        return read_cars(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Airport:
        return read_airports(path, file_name=file_name, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")


def write(entities: list[object], path: str, file_name: str = None, delimiter: str = ";") -> None:
    if isinstance(entities[0], Person):
        return write_people([typing.cast(Person, e) for e in entities], path, file_name=file_name, delimiter=delimiter)
    elif isinstance(entities[0], Car):
        return write_cars([typing.cast(Car, e) for e in entities], path, file_name=file_name, delimiter=delimiter)
    elif isinstance(entities[0], Airport):
        return write_airports([typing.cast(Airport, e) for e in entities], path, file_name=file_name,
                              delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")
