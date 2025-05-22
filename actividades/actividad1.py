from mtf_core import mtf_algorithm

def run():
    config = [0, 1, 2, 3, 4]
    sequence = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    print("\n--- Ejecutando Actividad 1 ---\n")
    mtf_algorithm(config.copy(), sequence)