# primera version
import pandas as pd
import numpy as np

class HuellaCarbonoApp:
    def __init__(self):
        self.combustibles = {
            "Gas Natural": {"emision_CO2": 2.03, "costo": 1.5},
            "Diesel": {"emision_CO2": 2.68, "costo": 2.0},
            "Gasolina": {"emision_CO2": 2.31, "costo": 1.8}
        }
        self.normativas = {"ISO 14064": "Estándar de huella de carbono", "GHG Protocol": "Protocolo de gases de efecto invernadero"}
    
    def calcular_huella(self, combustible, consumo):
        if combustible in self.combustibles:
            return consumo * self.combustibles[combustible]["emision_CO2"]
        else:
            return "Combustible no registrado"
    
    def comparar_combustibles(self, consumo):
        resultados = {}
        for combustible, datos in self.combustibles.items():
            huella = consumo * datos["emision_CO2"]
            costo_total = consumo * datos["costo"]
            resultados[combustible] = {"Huella CO2": huella, "Costo Total": costo_total}
        return pd.DataFrame(resultados).T
    
    def mostrar_normativas(self):
        return self.normativas
    
if __name__ == "__main__":
    app = HuellaCarbonoApp()
    consumo = float(input("Ingrese el consumo en unidades: "))
    print("\nComparación de Combustibles")
    print(app.comparar_combustibles(consumo))
    print("\nNormativas Disponibles")
    print(app.mostrar_normativas())
