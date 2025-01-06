def check(score):
    if score < 50:
        print("fail")
    else:
        print("pass")

score = int(input("Enter a score: "))
count = 0
scores_list = []

while score >= 0:
    check(score)
    scores_list.append(score)  # Aggiungi il punteggio alla lista
    count += 1
    score = int(input("Enter a score: "))

# Calcolo della media
if scores_list:  # Controlla che la lista non sia vuota
    average = sum(scores_list) / len(scores_list)
    print(f'Count: {count}')
    print(f'Average: {average:.2f}')
else:
    print("No valid scores entered.")
