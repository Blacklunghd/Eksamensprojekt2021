class Ansat:
    def __init__(
        self,
        initials,
        name,
        email,
        password,
        number,
    ):
        self.initials = initials
        self.name = name
        self.email = email
        self.password = password
        self.number = number

    def fil(self):
        self.file = "ansatte.txt"

    def registrerBruger(self):
        åbnFil = open(self.file, "a")
        tilføj_til_fil = f"{self.initials}:{self.name}:{self.email}:{hash(self.password)}:{self.number}\n"
        åbnFil.writelines(str(tilføj_til_fil))
        åbnFil.close()

    def eksisterendeBruger(self):
        with open(self.file, "r+") as f:
            gennemsøgFil = f.readlines()
            for line in gennemsøgFil:
                wordInLine = line.split(":")
                if str(self.initials) == wordInLine[0]:
                    return True
                if self.email == wordInLine[2]:
                    return True
            f.close()
            return False
