from Model import Model

class Control:

    def __init__(self):
        self.opcao = -1
        self.modelo = Model()

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2

    def getNum3(self):
        return self.num3

    def getNum4(self):
        return self.num4

    def getNum5(self):
        return self.num5

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def setNum1(self, num1):
        self.num1 = num1

    def setNum2(self, num2):
        self.num2 = num2

    def setNum3(self, num3):
        self.num3 = num3

    def setNum4(self, num4):
        self.num4 = num4

    def setNum5(self, num5):
        self.num5 = num5

    def coletar2(self):
        print("Informe um numero: ")
        self.setNum1(float(input()))


    def coletar3(self):
        print("Informe a base: ")
        self.setNum1(float(input()))

        print("Informe a altura: ")
        self.setNum2(float(input()))

    def coletar4(self):
        print("Informe sua idade em anos: ")
        self.setNum1(float(input()))

        print("Informe quantos meses: ")
        self.setNum2(float(input()))

        print("Informe os dias: ")
        self.setNum3(float(input()))

    def coletar5(self):
        print("Informe o numero total de eleitores: ")
        self.setNum1(float(input()))

        print("Informe o numero total de votos brancos: ")
        self.setNum2(float(input()))

        print("Informe o numero total de votos nulos: ")
        self.setNum3(float(input()))

        print("Informe o numero total de votos validos: ")
        self.setNum4(float(input()))

    def coletar6(self):
        print("Informe o valor do salario: ")
        self.setNum1(float(input()))

        print("Informe o percentual de ajuste: ")
        self.setNum2(float(input()))

    def coletar7(self):
        print("Informe o valor do custo de fabrica do carro: ")
        self.setNum1(float(input()))

    def coletar8(self):
        print("Informe a primeira nota: ")
        self.setNum1(float(input()))

        print("Informe a segunda nota: ")
        self.setNum2(float(input()))

        print("Informe a terceira nota: ")
        self.setNum3(float(input()))

    def coletar9(self):
        print("Informe a quantidade de maça: ")
        self.setNum1(float(input()))

    def coletar11(self):
        print("Informe o salario atual: ")
        self.setNum1(float(input()))

        print("Informe o valor total das vendas: ")
        self.setNum2(float(input()))

    def coletar12(self):
        print("Informe o numero da conta: ")
        self.setNum1(float(input()))

        print("Informe o saldo da conta: ")
        self.setNum2(float(input()))

        print("Informe o debito da conta: ")
        self.setNum3(float(input()))

        print("Informe o credito da conta: ")
        self.setNum4(float(input()))

    def coletar13(self):
        print("Informe um numero: ")
        self.setNum1(float(input()))

    def coletar14(self):
        print("o resultado é: ")

    def coletar17(self):
        print("o resultado é: ")

    def menu(self):
        print("\nEscolha uma das opções abaixo: " +
              "\n0. Sair" +
              "\n1. Ex1" +
              "\n2. Ex2" +
              "\n3. Ex3" +
              "\n4. Ex4" +
              "\n5. Ex5" +
              "\n6. Ex6" +
              "\n7. Ex7" +
              "\n8. Ex8" +
              "\n9. Ex9" +
              "\n11. Ex11" +
              "\n12. Ex12" +
              "\n13. Ex13" +
              "\n14. Ex14" +
              "\n17. Ex17")
        self.setOpcao(int(input()))

    def operacao(self):
        while (self.getOpcao != 0):
            self.menu()  # Mostrar a lista de dados na tela
            if self.getOpcao() == 0:
                print("Obrigado!")
                break

            elif self.getOpcao() == 2:
                self.coletar2()
                print("O numero antecessor é: {}".format(self.modelo.dois(self.getNum1())))

            elif self.getOpcao() == 3:
                self.coletar3()
                print("A area do triangulo é: {}".format(self.modelo.tres(self.getNum1(), self.getNum2())))

            elif self.getOpcao() == 4:
                self.coletar4()
                print("Sua idade em dias é: {}".format(self.modelo.quatro(self.getNum1(), self.getNum2(), self.getNum3())))

            elif self.getOpcao() == 5:
                self.coletar5()
                print("O percentual é: {}".format(self.modelo.cinco(self.getNum1(), self.getNum2(), self.getNum3(), self.getNum4())))

            elif self.getOpcao() == 6:
                self.coletar6()
                print("O novo salario é: {}".format(self.modelo.seis(self.getNum1(), self.getNum2())))

            elif self.getOpcao() == 7:
                self.coletar7()
                print("O custo final é: {}".format(self.modelo.sete(self.getNum1())))

            elif self.getOpcao() == 8:
                self.coletar8()
                print("A media artimetica é: {}".format(self.modelo.oito(self.getNum1(), self.getNum2(), self.getNum3())))

            elif self.getOpcao() == 9:
                self.coletar9()
                print("O valor total da compra é: {}".format(self.modelo.nove(self.getNum1())))

            elif self.getOpcao() == 11:
                self.coletar11()
                print("O valor total do salario é: {}".format(self.modelo.onze(self.getNum1(), self.getNum2())))

            elif self.getOpcao() == 12:
                self.coletar12()
                print("{}".format(self.modelo.doze(self.getNum1(), self.getNum2(), self.getNum3(), self.getNum4())))

            elif self.getOpcao() == 13:
                self.coletar13()
                print("{}".format(self.modelo.treze(self.getNum1())))

            elif self.getOpcao() == 14:
                self.coletar14()
                print("{}".format(self.modelo.quatorze(self.getNum1())))

            elif self.getOpcao() == 17:
                self.coletar17()
                print("{}".format(self.modelo.dezessete()))

            else:
                print("Opção invalida!")
