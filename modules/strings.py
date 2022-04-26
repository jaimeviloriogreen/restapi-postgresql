# Make string with coma (" , ")
def stringWithComa(values):
    result = ""
    for value in values:
        result += value + ","
    return result.rstrip(",")