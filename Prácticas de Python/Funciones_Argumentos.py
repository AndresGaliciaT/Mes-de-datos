#  La sintaxis para usar argumentos de variable es agregar un asterisco único como prefijo (*) antes del nombre del argumento
def variable_length(*args):
    print(args)

variable_length("one", "two")


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
print(sequence_time(4, 14, 18))
    