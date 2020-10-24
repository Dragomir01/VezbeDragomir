def main():
    print("Konverter u Celzijus iz Fahrenhaita")
    fahrenheit = eval(input("Unesite vašu temperaturu u Fahrenhajtu:"))
    celsius = (fahrenheit - 32)*5/9
    print("Temperatura je",celsius,"stepeni.")

main()