import udprint
import nybruger
import sys
import nybruger

open("ansatte.txt", "a")


def opstart():
    print("Skal programmet vise dig filen, eller vil du tilføje en ansat?")
    valg = input(
        "Hvis du vælger 1, vil du kunne se en liste over ansatte, hvis 2, kan du tilføje en ny."
    )

    if valg == "1":
        print("Herved kommer en liste over ansatte")
        udprint.visFil()

    if valg == "2":
        print("Du kan nu tilføje en ny ansat.")
        nybruger.ny_bruger()


if __name__ == "__main__":
    opstart()
