def emocromo(glucosio, emoglobina, colesterolo):
    # Creare una lista per memorizzare le misurazioni
    misurazioni = []
    # Aggiungere le misurazioni alla lista
    misurazioni.append({'glucosio': glucosio, 'emoglobina': emoglobina, 'colesterolo': colesterolo})
    return misurazioni

def print_emocromo(misurazioni):
    # Iterare su ogni misurazione nella lista
    for misurazione in misurazioni:
        print(f'Glucosio: {misurazione["glucosio"]}, Emoglobina: {misurazione["emoglobina"]}, Colesterolo: {misurazione["colesterolo"]}')

def total_emocromo(misurazioni):
    # Calcolare il totale dei valori di glucosio, emoglobina e colesterolo
    total_glucosio = sum(misurazione['glucosio'] for misurazione in misurazioni)
    total_emoglobina = sum(misurazione['emoglobina'] for misurazione in misurazioni)
    total_colesterolo = sum(misurazione['colesterolo'] for misurazione in misurazioni)
    return total_glucosio, total_emoglobina, total_colesterolo

def filter_emocromo_by_value(misurazioni, key, value):
    # Filtrare le misurazioni in base a una chiave specifica e un valore
    return list(filter(lambda misurazione: misurazione[key] == value, misurazioni))

def main():
    misurazioni = []
    while True:
        print('\nEmocromo Tracker')
        print('1. Aggiungi una misurazione')
        print('2. Visualizza tutte le misurazioni')
        print('3. Mostra i totali delle misurazioni')
        print('4. Filtra misurazioni per valore')
        print('5. Esci')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            glucosio = float(input('Enter glucosio: '))
            emoglobina = float(input('Enter emoglobina: '))
            colesterolo = float(input('Enter colesterolo: '))
            misurazioni.extend(emocromo(glucosio, emoglobina, colesterolo))
            print('Misurazione aggiunta.')

        elif choice == '2':
            print('\nTutte le Misurazioni:')
            print_emocromo(misurazioni)
    
        elif choice == '3':
            total_glucosio, total_emoglobina, total_colesterolo = total_emocromo(misurazioni)
            print(f'\nTotale Glucosio: {total_glucosio}')
            print(f'Totale Emoglobina: {total_emoglobina}')
            print(f'Totale Colesterolo: {total_colesterolo}')
    
        elif choice == '4':
            key = input('Enter the key to filter by (glucosio, emoglobina, colesterolo): ')
            value = float(input(f'Enter the value for {key}: '))
            filtered_misurazioni = filter_emocromo_by_value(misurazioni, key, value)
            print(f'\nMisurazioni per {key} = {value}:')
            print_emocromo(filtered_misurazioni)
    
        elif choice == '5':
            print('Exiting the program.')
            break
        
        else:
            print('Invalid choice, please try again.')

# Esegui la funzione main se il file è eseguito direttamente
if __name__ == "__main__":
    main()
