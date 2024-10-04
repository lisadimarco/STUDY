def calcola_bmi(peso, altezza):
    return peso / (altezza ** 2)

def interpreta_bmi(bmi):
    if bmi < 18.5:
        return "Sottopeso"
    elif bmi < 25:
        return "Normopeso"
    elif bmi < 30:
        return "Sovrappeso"
    else:
        return "Obesità"

# Esempio d'uso
peso = 70
altezza = 1.75
bmi = calcola_bmi(peso, altezza)
print(f"BMI: {bmi:.1f} - {interpreta_bmi(bmi)}")
