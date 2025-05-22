from mtf_core import mtf_algorithm

def run():
    config = [0, 1, 2, 3, 4]
    sequence = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    print("\n--- Ejecutando Actividad 2 ---\n")
    mtf_algorithm(config.copy(), sequence)