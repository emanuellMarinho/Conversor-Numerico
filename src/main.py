class Base:
    def __init__(self):
        self.select_conversion()

    def convert_bin(self):
        decimal = int(input("Digite o número decimal: "))
        binary = ""

        while decimal > 0:
            resto = decimal % 2
            binary = str(resto) + binary
            decimal = decimal // 2

        print("Resultado em binário:", binary)

    def convert_octal(self):
        decimal = int(input("Digite o número decimal: "))
        octal = ""

        while decimal > 0:
            resto = decimal % 8
            octal = str(resto) + octal
            decimal = decimal // 8

        print("Resultado em octal:", octal)

    def convert_hex(self):
        decimal = int(input("Digite o número decimal: "))
        hexa_digits = "0123456789ABCDEF"
        hexa = ""

        while decimal > 0:
            resto = decimal % 16
            hexa = hexa_digits[resto] + hexa
            decimal = decimal // 16

        print("Resultado em hexadecimal:", hexa)

    def select_conversion(self):
        while True:
            try:
                choice = int(input('''
                Escolha uma das bases para conversão:
                [ 1 ] converter para BINÁRIO
                [ 2 ] converter para OCTAL
                [ 3 ] converter para HEXADECIMAL
                [ 0 ] Sair
                '''))

                if choice == 0:
                    break

                if choice == 1:
                    self.convert_bin()
                elif choice == 2:
                    self.convert_octal()
                elif choice == 3:
                    self.convert_hex()
                else:
                    print("Opção inválida")

            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

# Exemplo de uso
base = Base()
