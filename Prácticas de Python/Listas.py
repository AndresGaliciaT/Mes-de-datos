planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Determinación de la longitud de una lista
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Incorporación de valores a listas
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Quitar el último elemento de una lista
planets.pop()  # Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

# Capturar un elemento individual en una lista
print("The first planet is", planets[0])

# índices negativos
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Búsqueda de un valor en una lista
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")