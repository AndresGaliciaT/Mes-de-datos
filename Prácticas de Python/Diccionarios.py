## Creación de un diccionario

planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name')) 
print(planet['name']) # También se puede usar 

# Diferencias
wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError

## Modificación de valores de diccionario

planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

# Maneras de actualizar 

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

## Adición y eliminación de claves
planet['orbital period'] = 4333
planet.pop('orbital period')

## Tipos de data complejos
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')