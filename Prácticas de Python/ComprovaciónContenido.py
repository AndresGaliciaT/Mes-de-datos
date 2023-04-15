## Para extraer la temperatura media en Marte
#Método 1
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':') # .split
print(parts)

#Método 2
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric(): # .isnumeric
        print(item)
# si el valor es negativo isnumeric no funciona

print("-60".startswith('-')) # con .startswith(): para saber si es negativo el valor