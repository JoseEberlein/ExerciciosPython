import math

class Model:

    def __init__ (self):
        pass

    def dois (self, num1):
        return num1 - 1

    def tres (self, num1, num2):
        return num1 * num2

    def quatro (self, num1, num2, num3):
        return num1 * 365 + num2 * 30 + num3

    def cinco(self, num1, num2, num3, num4):
        return num1, (num2 * 100)/100, (num3 * 100)/100, (num4 * 100)/100

    def seis (self, num1, num2):
        return ((num1 * num2)/100) * 100

    def sete (self, num1):
        return num1 + (num1 * 1.28) + (num1 * 1.45)

    def oito (self, num1, num2, num3):
        return (num1 + num2 + num3)/3

    def nove (self, num1,):
        if float(num1) < float(12):
            return num1 * 1.3

    def onze (self, num1, num2):
        if float(num2) <= float(1500):
           return num1 + (num2 * 0.03)
        elif float(num2) > float(1500):
           return num1 + (num2 - 1500) * 0.05 + 45

    def doze (self, num2, num3, num4):
        num5 = ((num2 - num3) + num4)
        if num5 < 0:
           return ("Saldo atual é: R${}\nSaldo é negativo." .format(num5))
        else:
           return ("Saldo atual é: R${}\nSaldo é positivo." .format(num5))

    def treze (self, num1):
        if (num1 > 0) & (num1 < 11):
            msg = ""
        for i in range(11):
            msg = msg + "\n{} * {} = {}".format(num1, i, num1 * i)
        return msg

    def quatorze (self, num1):
        for x in range ():
            return x

    def dezessete (self):
        soma = 0
        valor_intervalo = len(range(15, 101))

        for i in range(15, 101):
            soma += i
        media = soma / valor_intervalo

        print("media geral {}".format(media))






