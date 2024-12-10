class Catena:
    def __init__(self, type_, regione_variable, regione_constante):
        """
        Rappresenta una catena di un anticorpo.
        
        :param type_: Tipo di catena ("leggera" o "pesante").
        :param region_variable: Regione variabile della catena (estremità N-terminale).
        :param region_constant: Regione costante della catena.
        """
        self.type = type_
        self.regione_variable = regione_variable
        self.regione_constante = regione_constante

class Anticorpo:
    def __init__(self, light_chain_type):
        """
        Rappresenta un anticorpo con struttura ad Y.
        
        :param light_chain_type: Tipo di catena leggera ("lambda" o "kappa").
        """
        # Creazione delle catene leggere
        self.light_chain_1 = Catena("leggera", "variabile", "costante")
        self.light_chain_2 = Catena("leggera", "variabile", "costante")
        
        # Creazione delle catene pesanti
        self.heavy_chain_1 = Catena("pesante", "variabile", "costante")
        self.heavy_chain_2 = Catena("pesante", "variabile", "costante")
        
        # Memorizzazione del tipo di catene leggere
        self.light_chain_type = light_chain_type

    def describe_structure(self):
        """Descrive la struttura dell'anticorpo."""
        return {
            "Fab": [
                {"light_chain": self.light_chain_1.type, "heavy_chain": self.heavy_chain_1.type},
                {"light_chain": self.light_chain_2.type, "heavy_chain": self.heavy_chain_2.type},
            ],
            "Fc": {
                "heavy_chains": [self.heavy_chain_1.type, self.heavy_chain_2.type]
            }
        }

# Creazione di un anticorpo con catene leggere di tipo kappa
antibody = Anticorpo(light_chain_type="kappa")

# Descrizione della struttura
structure = anticorpo.describe_structure()
print("Struttura dell'anticorpo:", structure)
