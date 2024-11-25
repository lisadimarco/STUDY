def arithmetic_arranger(problems, display_answers=False):
    # Verifica del numero massimo di problemi
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Inizializzazione delle righe
    top_row = []
    bottom_row = []
    lines = []
    results = []
    
    # Elaborazione di ogni problema
    for problem in problems:
        # Separazione degli elementi del problema
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid format.'

        num1, operator, num2 = parts

        # Controllo dell'operatore
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Controllo che i numeri contengano solo cifre
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        # Controllo della lunghezza massima dei numeri
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calcolo della larghezza necessaria per allineare i numeri
        width = max(len(num1), len(num2)) + 2
        top_row.append(num1.rjust(width))
        bottom_row.append(operator + ' ' + num2.rjust(width - 2))
        lines.append('-' * width)

        # Calcolo del risultato (se richiesto)
        if display_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(width))

    # Creazione del risultato
    arranged_problems = '    '.join(top_row) + '\n'
    arranged_problems += '    '.join(bottom_row) + '\n'
    arranged_problems += '    '.join(lines)
    if display_answers:
        arranged_problems += '\n' + '    '.join(results)
    
    return arranged_problems

# Esempi di utilizzo
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
