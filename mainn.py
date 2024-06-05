class conversor_temperatura:
    def __init__(self):
        pass

    def celsiusParaFahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheitParaCelsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    
def menu_principal():
    print("\n*calculadora de conversão de temperatura*")
    print("1. Converter celsius para fahrenheint")
    print("2. Converter fahrenheint Celsius")
    print("3. Sair")

    option = input("Digite a opção desejada: ")
    return option

def exit():
    print("Encerramento programado...")

conversor = conversor_temperatura()

while True:
    escolha = menu_principal()
    
    if escolha == '1':
        celsius = float(input("Digite o valor em celsius: "))
        fahrenheint = conversor.celsiusParaFahrenheit(celsius)
        print(f"{celsius} celsius é igual a {fahrenheint} fahrenheint.")
    elif escolha == '2':
        fahrenheint = float(input("Digite o valor em fahrenheint: "))
        celsius = conversor.fahrenheitParaCelsius(fahrenheint)
        print(f"{fahrenheint} fahrenheint é igual a {celsius} celsius.")
    elif escolha == '3':
        exit()
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
  