import codecademylib3
import numpy as np
import matplotlib.pyplot as plt  # Importa matplotlib correttamente


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print(total_ceballos)

percentage_ceballos = float(total_ceballos / len(survey_responses))
print(percentage_ceballos)

possible_surveys = np.random.binomial(len(survey_responses), 0.54, size=10000) / len(survey_responses)
print(possible_surveys)

plt.hist(possible_surveys, range=(0,1), bins = 20)
plt.show()

possible_surveys_lenght = float(len(possible_surveys))
incorrect_predictions=len(possible_surveys[possible_surveys<0.5])

ceballos_loss_surveys = incorrect_predictions / possible_surveys_lenght
print(ceballos_loss_surveys)

# Genera una distribuzione binomiale con 7.000 intervistati
large_survey = np.random.binomial(7000, 0.54, size=10000) / 7000
print(large_survey)

plt.hist(large_survey, range=(0,1), bins = 20)
plt.show()

incorrect_predictions=len(large_survey[large_survey<0.5])
ceballos_loss_new = incorrect_predictions/7000
print(ceballos_loss_new)
