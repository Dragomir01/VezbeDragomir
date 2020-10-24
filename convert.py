# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

print ("Ovaj program konvertuje Celzijus u Fahrenhajt.")

def main():
    celsius = eval(input("Kolika je temperatura u Celzijusu? "))
    fahrenheit = 9/5 * celsius + 32
    print("Temperatura je", fahrenheit, "stepeni fahrenhajta.")

main()
