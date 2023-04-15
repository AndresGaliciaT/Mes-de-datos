
#>>> heading = "temperatures and facts about the moon"
#>>> heading.title() # .title
#'Temperatures And Facts About The Moon' #Se imprime así

## División de cadena
#>>> temperatures = """Daylight: 260 F
#... Nighttime: -280 F"""
#>>> temperatures .split() # .split
#['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']

##Búsqueda en cadena
#>>> "Moon" in "This text will describe facts and challenges with space travel"
#False
#>>> "Moon" in "This text will describe facts about the Moon" # in
#True

## Buscar posición de una palabra 
#>>> temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
#... while Mars has -28 Celsius."""
#>>> temperatures.find("Moon") # .find
#-1

## Buscar contenido 
#>>> temperatures.count("Mars")
#1
#>>> temperatures.count("Moon") # .count
#0

## Buscar contenido sin distinción de mayusculas y minusculas 
#>>> "The Moon And The Earth".lower()
#'the moon and the earth' # .lower

