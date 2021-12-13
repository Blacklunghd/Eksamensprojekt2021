from ansat import Ansat
import gennemsøg


def ny_bruger():
    ansat = Ansat(
        initials=gennemsøg.initials_gennemsøg(),
        name=input("indtast venligst den ansattes navn:  "),
        email=gennemsøg.email_gennemsøg(),
        number=gennemsøg.number_gennemsøg(),
    )
    Ansat.registrerBruger()
