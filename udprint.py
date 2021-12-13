tekstfilen = "ansatte.txt"


def visFil():
    with open(tekstfilen) as f:
        læsFil = f.readlines()
    for linje in læsFil:
        wordInLine = linje.split(":")
        print(
            f"Initials: {wordInLine[0]}\nName: {wordInLine[1]}\nEmail: {wordInLine[2]}\nPassword: {wordInLine[3]}\nNumber: {wordInLine[4]}"
        )
        print("Venligst konsulter med direktionen, i forhold til dit adgangsnummer.")
