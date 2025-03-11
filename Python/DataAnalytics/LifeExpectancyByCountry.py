import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

life_expectancy = data["Life Expectancy"]
gdp = data["GDP"]

# Calcolo dei quartili della speranza di vita
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
median_gdp = np.quantile(gdp, 0.5)

low_gdp = data[data['GDP']<=median_gdp]
high_gdp = data[data['GDP']>median_gdp]

low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])

high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'], [0.25, 0.5, 0.75])

print(low_gdp_quartiles)
print(high_gdp_quartiles)
# Creazione della figura con due assi
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # 1 riga, 2 colonne

# Primo istogramma: Life Expectancy
ax1.hist(life_expectancy, bins=20, color='blue', edgecolor='black')
ax1.set_title("Distribuzione della Speranza di Vita")
ax1.set_xlabel("Speranza di Vita")
ax1.set_ylabel("Frequenza")

# Secondo istogramma: GDP
ax2.hist(gdp, bins=20, color='green', edgecolor='black')
ax2.set_title("Distribuzione del PIL")
ax2.set_xlabel("PIL")
ax2.set_ylabel("Frequenza")

#Creazione istogramma
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()
