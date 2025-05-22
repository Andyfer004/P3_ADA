from mtf_core import mtf_algorithm

def run():
    config = [0, 1, 2, 3, 4]
    sequence = [0] * 20
    print("\n--- Ejecutando Actividad 3 (Mejor Caso) ---\n")
    mtf_algorithm(config.copy(), sequence)