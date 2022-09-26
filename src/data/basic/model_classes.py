class Person:
    id: str
    name: str
    age: int
    male: bool

    def __init__(self, id: str, name: str, age: int, male: bool = True) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.male = male

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Person) and self.id == o.id

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return "#{0}: {1} ({2}, {3})".format(self.id, self.name, self.age, self.male)

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented

        return self.id < o.id


class Car:
    plate: str
    type: str
    year: int
    automatic: bool

    def __init__(self, plate: str, type: str, year: int, automatic=True) -> None:
        self.plate = plate
        self.type = type
        self.year = year
        self.automatic = automatic

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Car) and self.plate == o.plate

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return "{0} ({1}, {2}): {3}".format(self.plate, self.type, self.year, self.automatic)

    def __hash__(self) -> int:
        return self.plate.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Car):
            return NotImplemented

        return self.plate < o.plate


class Airport:
    code: str
    name: str
    city: str
    state: str
    country: str

    def __init__(self, code: str, name: str, city: str, state: str, country: str) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.state = state
        self.country = country

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Airport) and self.code == o.code

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return "{code} ({name}): {city}, {state}, {country}".format(
            code=self.code, name=self.name, city=self.city,
            state=self.state, country=self.country)

    def __hash__(self) -> int:
        return self.code.__hash__()

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Airport):
            return NotImplemented

        return self.code < o.code
