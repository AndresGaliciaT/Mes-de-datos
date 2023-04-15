def rocket_parts():
    print("payload, propellant, structure")

# Exigencia de argumento 
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
print (distance_from_earth("Moon"))

print (distance_from_earth("Saturn"))