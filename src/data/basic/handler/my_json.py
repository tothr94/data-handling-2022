import json

from data.basic.generator import generate_people
from data.basic.model_dataclasses import Person


def write_people(people: list[Person], path: str) -> None:
    with open(path, "w") as file:
        json.dump(people, file)

if __name__ == "__main__":
    people = generate_people(10)
    write_people(people, "D:/people.json")
