def main():
    print("Ovaj program računa vrednost")
    print("sa investicijom unetom od strane korisnika")

    principal = eval(input("Uneti početan ulog"))
    apr = eval(input("Uneki godisnju ratu"))
    year = eval(input("Uneti period u godinama"))
    inflation = eval(input("Uneti stopu inflacije"))

    for i in range(year):
        principal = principal * (1 + apr)
        principal = principal / (1 + inflation)
    if year == 1:
        print("Vrednost u jednoj godini je:", principal)
    else:
        print("Vrednost u", year, "godina je", principal)

main()

