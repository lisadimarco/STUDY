import pandas as pd

# Carica i dati dai file CSV
visits = pd.read_csv('visits.csv', parse_dates=[1])  # Carica i dati delle visite e converte la colonna 1 in datetime
cart = pd.read_csv('cart.csv', parse_dates=[1])      # Carica i dati del carrello e converte la colonna 1 in datetime
checkout = pd.read_csv('checkout.csv', parse_dates=[1])  # Carica i dati del checkout e converte la colonna 1 in datetime
purchase = pd.read_csv('purchase.csv', parse_dates=[1])  # Carica i dati degli acquisti e converte la colonna 1 in datetime

# Stampa le prime righe per verificare i dati
print(visits.head(5))  # Mostra le prime 5 righe dei dati delle visite
print(cart.head(5))    # Mostra le prime 5 righe dei dati del carrello
print(checkout.head(5))  # Mostra le prime 5 righe dei dati del checkout
print(purchase.head(5))  # Mostra le prime 5 righe dei dati degli acquisti

# Unisci i dati delle visite e del carrello
visits_cart = pd.merge(visits, cart, how='left')  # Unisce visits e cart su una chiave comune (user_id di default)
print("Numero di righe dopo merge visits e cart:", len(visits_cart))  # Stampa il numero di righe dopo il merge

# Calcola la percentuale di utenti che NON hanno aggiunto al carrello
percentage_no_cart = float(visits_cart[visits_cart.cart_time.isnull()].shape[0]) / len(visits_cart)
print(f"Percentuale di utenti che NON hanno aggiunto al carrello: {(1 - percentage_no_cart) * 100:.2f}%")

# Unisci i dati del carrello e del checkout
cart_checkout = pd.merge(cart, checkout, how='left')  # Unisce cart e checkout su una chiave comune
print("Numero di righe dopo merge cart e checkout:", len(cart_checkout))  # Stampa il numero di righe dopo il merge

# Calcola la percentuale di utenti che NON hanno proceduto al checkout
percentage_no_checkout = float(cart_checkout[cart_checkout.checkout_time.isnull()].shape[0]) / len(cart_checkout)
print(f"Percentuale di utenti che NON hanno proceduto al checkout: {(1 - percentage_no_checkout) * 100:.2f}%")

# Unisci i dati del checkout e degli acquisti
checkout_purchase = pd.merge(checkout, purchase, how='left')  # Unisce checkout e purchase su una chiave comune
print("Numero di righe dopo merge checkout e purchase:", len(checkout_purchase))  # Stampa il numero di righe dopo il merge

# Unisci i dati di cart_checkout e visits
merged_data = pd.merge(cart_checkout, visits, how='left')  # Unisce cart_checkout e visits su una chiave comune
# Unisci i dati risultanti con purchase
all_data = pd.merge(merged_data, purchase, how='left')  # Unisce merged_data e purchase su una chiave comune
print(all_data.head(10))  # Stampa le prime 10 righe del DataFrame finale

# Calcola la percentuale di utenti che hanno effettuato il checkout ma NON hanno acquistato
percentage_no_purchase = float(checkout_purchase[checkout_purchase.purchase_time.isnull()].shape[0]) / len(checkout_purchase)
print(f"Percentuale di utenti che hanno effettuato il checkout ma NON hanno acquistato: {percentage_no_purchase * 100:.2f}%")

# Calcola le percentuali di abbandono per ogni passaggio del funnel

# 1. Visite → Aggiunta al carrello
percentage_no_cart = float(visits_cart[visits_cart.cart_time.isnull()].shape[0]) / len(visits_cart)
abbandono_visite_carrello = percentage_no_cart * 100  # Percentuale di utenti che non hanno aggiunto al carrello

# 2. Aggiunta al carrello → Checkout
percentage_no_checkout = float(cart_checkout[cart_checkout.checkout_time.isnull()].shape[0]) / len(cart_checkout)
abbandono_carrello_checkout = percentage_no_checkout * 100  # Percentuale di utenti che non hanno proceduto al checkout

# 3. Checkout → Acquisto
percentage_no_purchase = float(checkout_purchase[checkout_purchase.purchase_time.isnull()].shape[0]) / len(checkout_purchase)
abbandono_checkout_acquisto = percentage_no_purchase * 100  # Percentuale di utenti che non hanno completato l'acquisto

# Stampa le percentuali di abbandono
print(f"Abbandono Visite → Carrello: {abbandono_visite_carrello:.2f}%")
print(f"Abbandono Carrello → Checkout: {abbandono_carrello_checkout:.2f}%")
print(f"Abbandono Checkout → Acquisto: {abbandono_checkout_acquisto:.2f}%")

# Identifica il passaggio più debole (quello con la percentuale di abbandono più alta)
abbandoni = {
    "Visite → Carrello": abbandono_visite_carrello,
    "Carrello → Checkout": abbandono_carrello_checkout,
    "Checkout → Acquisto": abbandono_checkout_acquisto
}

passaggio_piu_debole = max(abbandoni, key=abbandoni.get)  # Trova il passaggio con il tasso di abbandono più alto
print(f"Il passaggio più debole è: {passaggio_piu_debole} con un tasso di abbandono del {abbandoni[passaggio_piu_debole]:.2f}%")

# Calcola il tempo medio tra la visita e l'acquisto
all_data['average_time'] = all_data.purchase_time - all_data.visit_time  # Crea una nuova colonna con la differenza di tempo
print(all_data)  # Stampa il DataFrame con la nuova colonna
print(all_data['average_time'].mean())  # Stampa il tempo medio tra visita e acquisto
