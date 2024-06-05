class conversor_temperatura:
    def __init__(self):
        pass

    def  celsiusParaFahrenheit (self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    def fahrenheitParaCelsius (self, celsius):
        return (celsius * 9/5) + 32