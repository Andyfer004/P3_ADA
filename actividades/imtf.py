def imtf_algorithm(config_list, request_sequence):
    total_cost = 0
    print(f"{'Solicitud':>10} | {'Costo':>5} | {'Lista antes':>20} | {'Lista después':>20}")
    print("-" * 65)
    n = len(request_sequence)

    for i, request in enumerate(request_sequence):
        before = config_list.copy()
        idx = config_list.index(request)
        cost = idx + 1
        total_cost += cost
        lookahead_window = request_sequence[i+1:i+cost]
        if request in lookahead_window:
            config_list.remove(request)
            config_list.insert(0, request)
        print(f"{request:>10} | {cost:>5} | {str(before):>20} | {str(config_list):>20}")

    print("\nCosto total:", total_cost)
    return total_cost

def run():
    print("\n--- Ejecutando Actividad 6 (IMTF con Mejor Caso MTF) ---")
    config1 = [0, 1, 2, 3, 4]
    best_case = [0] * 20
    imtf_algorithm(config1.copy(), best_case)

    print("\n--- Ejecutando Actividad 6 (IMTF con Peor Caso MTF) ---")
    config2 = [0, 1, 2, 3, 4]
    worst_case = [4, 3, 2, 1, 0] * 4
    imtf_algorithm(config2.copy(), worst_case)