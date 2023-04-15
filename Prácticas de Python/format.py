mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage)) # Los marcadores de format son {}

## f-strings

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth") # f-strings


# round(100/6, 1) 
# Resultado: 16.7
 
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth") 

subject = "interesting facts about the moon"
print (f"{subject.title()}")