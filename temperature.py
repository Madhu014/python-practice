#Create a Temprature class. Make two methods :
#convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temperature:
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 1.8) + 32
        print(fahrenheit, "F")

    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) / 1.8
        print(celsius, "C")
values=Temperature()
values.convertFahrenheit(25)
values.convertCelsius(57)