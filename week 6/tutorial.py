class Person:
    def __init__(self , name: str, surname: str, passport: str) -> None:
        self.name = name
        self.surname = surname
        self.passport = passport

    def __str__(self) -> str:
        return self.name + ", " + self.surname + ", " + str(self.passport)


class Worker(Person):
    def __init__(self , name: str, surname: str, passport: str, job: str) -> None:
        Person.__init__(self , name , surname , passport)
        self.job = job

    def __str__(self) -> str:
        return Person.__str__(self) + ", " + str(self.job)


class Athlete(Person):
    def __init__(self , name: str, surname: str, passport: str, sport: str) -> None:
        Person.__init__(self , name , surname , passport)
        self.sport = sport

    def __str__(self) -> str:
        return Person.__str__(self) + ", " + str(self.sport)

    def __eq__(self, worker: Worker) -> bool:
        return self.passport == worker.passport
