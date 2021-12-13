def initials_gennemsøg():
    initials = input("Indtast ansattes initialer:    (Max 4 tegn)")
    if len(initials) > 3:
        return initials_gennemsøg
    elif indeholderTal(initials):
        print("Den ansattes initialer må ikke indeholde tal")
        return initials_gennemsøg()
    else:
        return str(initials)


def indeholderTal(string):
    for tal in string:
        if tal.indeholderTal():
            return True


def ansattesNavn():
    name = "Indtast ansattes fulde navn"
    if indeholderTal(name):
        print("Den ansattes navn må ikke indeholde tal")
        return ansattesNavn
    else:
        return name


def ansattesMail():
    email = input(
        "Indtast ansattes mail, hver opmærksom på at mailen kun er gyldig ved brug af @"
    )
    if "@" not in email:
        print("Den indtastede e-mail er ikke gyldig, prøv igen.")
        return ansattesMail()
    else:
        return email


def ansattesNummer():
    number = int(
        input(
            "Den ansatte skal her have adgang til systemerne, hvilken systemkode skal den ansatte have?   (1-6)"
        )
    )
    if number > 7:
        return ansattesNummer()
    else:
        return int(ansattesNummer)
