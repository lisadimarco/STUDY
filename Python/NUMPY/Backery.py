import numpy as np

# Creiamo l'array con i dati della ricetta
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

recipes = np.genfromtxt('recipes.csv', delimiter=',')

eggs = recipes[:,2]

one_egg = recipes[(eggs == 1)]

cookies = recipes[2, :]

double_batch = cupcakes * 2

grocery_list = cookies + double_batch

print(grocery_list)
