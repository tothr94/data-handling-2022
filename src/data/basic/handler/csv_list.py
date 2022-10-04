import csv

from data.basic.generator import generate_people
from data.basic.model_dataclasses import Person

def write_people(people: list[Person],
                 path: str) -> None:

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        for person in people:
            writer.writerow([
                person.id,  person.name,
                person.age, person.male
            ])

if __name__ == "__main__":
    people = generate_people(10)
    write_people(people, r"D:/people.csv")