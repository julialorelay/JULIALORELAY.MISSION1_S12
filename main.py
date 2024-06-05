class conversor_medidas:
    def __init__(self):
        pass

    def centimetrosParaMetros(self, metros):
        return metros / 100
    
    def metrosParaCentimetros(self, centimetros):
        return centimetros * 100

def menu_principal():
    print("\n*calculadora de conversão de unidades*")
    print("1. Converter centimetros para metros")
    print("2. Converter metros para centmetros")
    print("3. Sair")

    option = input("Digite a opção desejada: ")
    return option

def exit():
    print("Encerramento programado...")

conversor = conversor_medidas()

while True:
    escolha = menu_principal()
    
    if escolha == '1':
        metros = float(input("Digite o valor em metros: "))
        centimetros = conversor.metrosParaCentimetros(metros)
        print(f"{metros} metros é igual a {centimetros} centímetros.")
    elif escolha == '2':
        centimetros = float(input("Digite o valor em centímetros: "))
        metros = conversor.centimetrosParaMetros(centimetros)
        print(f"{centimetros} centímetros é igual a {metros} metros.")
    elif escolha == '3':
        exit()
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")