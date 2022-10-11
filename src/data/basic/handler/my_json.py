import json
import os

from data.basic.generator import generate_people
from data.basic.model_dataclasses import Person


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
        return [
            Person(person["id"], person["name"],
                   person["age"], person["male"])
            for person in json.load(file)
        ]


if __name__ == "__main__":
    people = generate_people(10)
    write_people(people, "D:/", pretty=False)
    for person in read_people("D:/"):
        print(person)
