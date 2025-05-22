from mtf_core import mtf_algorithm

def run():
    config = [0, 1, 2, 3, 4]
    sequence_2s = [2] * 20
    sequence_3s = [3] * 20
    print("\n--- Ejecutando Actividad 5 - Solo 2s ---\n")
    mtf_algorithm(config.copy(), sequence_2s)
    print("\n--- Ejecutando Actividad 5 - Solo 3s ---\n")
    mtf_algorithm(config.copy(), sequence_3s)