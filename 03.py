from cmath import sin, cos, sqrt

#def zadatak1():
   # from cmath import sin, cos, sqrt
  # x = 4.0 / 10.0 + 3.5 * 2
  #  print(x)
  #  y = 10 % 4 + 6 / 2
  #  print(y)
  #  c = abs(4 - 20 / 3) ** 3
  #  print(c)
 #   v = sqrt(4.5 - 5.0)+ 7 * 3
 #  print(v)
 #   b = 3 * 10 / 3 + 10 % 3
 #   print(b)



#zadatak1()

#def zadatak2():
  #  r = eval(input("r"))
  #  a = eval(input("a"))
 #   t = sqrt(r*cos(a)+cos(a)+r*sin(a)*sin(a))
 #  print(t)
 #   rezultat2 = (3 + 4)*5
 #   print(rezultat2)
 #   n = eval(input("n:"))
 #   rezultat3 = n*(n-1)/2
 #   print(rezultat3)
 #   y1 = eval(input("y1"))
 #   y2 = eval(input("y2"))
 #   x1 = eval(input("x1"))
 #   x2 = eval(input("x2"))
#    z = (y2-y1)/(x2-x1)
#    print(z)
#zadatak2()

#def zadatak5():
#    r = eval(input("r:"))
#   pi = 3.14
#    V =  4/3 * pi * r ** 3
#    print(V)
#    A = 4 * pi * r ** 2
#    print(A)
#zadatak5()

#def zadatak15():
#    def main():
#        x = 0
#        n = eval(input("Unesite n:"))
#        for i in range(1, n + 1):
#            x += i
#        print("Ukupan zbir iznosi: ", x)

#zadatak15()

#def zadatak17():
       # suma = 0
      #  n = eval(input("Unesite n:"))
     #   for i in range(1, n + 1):
    #        print("Unesite ", i, ". broj:")
   #         broj = eval(input())
  #          suma = suma + broj
 #       print("Ukupan zbir iznosi: ", suma)

#zadatak17()

#def zadatak6():
#    r = eval(input("Unesite precnik pice"))
#    A =4*3.14*r**2
#    price = r/A
#    print("Cena pice po kvadratnom cm je" ,price, "dinara")

#zadatak6()

#def zadatak7():
#    H = 1.0079
#    C = 12.011
#    Hel = eval(input("Unesite broj atoma vodonika"))
#    Car = eval(input("Unesite broj atoma karbona"))
#    n = H * Hel + C * Car
#    print("Masa molekula je",n,".")

#zadatak7()

#def zadatak8():
#    V = 340
#    S = eval(input("Uneti vremenski period od trenutka sevanja do trenutka zvuka(U sekundama)"))
#    M = V*S
#    print("Razdaljina je",M,"metara.")

#zadatak8()

#def zadatak9():
#    Kafa = 105
#    Kolicina = eval(input("Uneti količinu kafe u kg:"))
#    Dostava = Kafa*Kolicina + 15
#    print("Cena vase porudžbine je",Dostava,"dinara.")

#zadatak9()

#def zadatak10():
#    x1 = eval(input("x1:"))
#    x2 = eval(input("x2"))
#    y1 = eval(input("y1"))
#    y2 = eval(input("y2"))

#    m = (y1-y2)/(x2-x1)

#    print(m)
#zadatak10()

#def zadatak11():
#    x1 = eval(input("x1:"))
#    x2 = eval(input("x2"))
#    y1 = eval(input("y1"))
#    y2 = eval(input("y2"))

#    d = ((x2-x1)**2+(y2-y1)**2)**0.5
#    print(d)
#zadatak11()

#def zadatak12():
#    god = eval(input("Uneti zadatu godinu kao četvorocifreni broj"))
#    C = god/100
#    epakt =(8+C/4-C+((8*C+13)/25)+11*(god%19))%30
#   print(epakt)

#zadatak12()

#def zadatak13():
   # a = eval(input("Unesite dužinu stranice a:"))
  #  b = eval(input("Unesite duzinu stranice b:"))
  #  c = eval(input("Unesite duzinu stranice c:"))
 #   s = (a+b+c)/2
#    Povrsina = (s*(s-a)*(s-b)*(s-c))**0.5
#    print("Povrsina trougla je:",Povrsina,"cm")

#zadatak13()

# def zadatak14():
#    from math import sin
#    V = eval(input("Unesite Visinu koju treba dostici"))
#    ugao = eval(input("Unesite ugao za datu visinu")
#   d = V/sin(ugao)
#    print("duzina je",d,)
#zadatak14()

#def zadatak16():
  #  x = 0
  #  n = eval(input("Unesite n:"))
 #   for i in range(1, n + 1):
#        x += i ** 2

#    print("Ukupan zbir iznosi: ", x,)

#zadatak16()

#def zadatak17():
   # x=0
  #  n = eval(input("Unesite n:"))
 #   for i in range(1,n+1):
#        print("Unesite ",i,". broj:")
#        zbir = eval(input())
#        x+=zbir
#    print("Ukupan zbir iznosi: ", x)

#zadatak17()

def zadatak18():
    x = 0
    n = eval(input("Unesite n:"))
    for i in range(1,n+1):
        print("Unesite",i,"broj")
        broj = eval(input())
        x += broj/n
        print("Prosek je",x,)
zadatak18()