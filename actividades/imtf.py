from colorama import Fore, Style, init
init(autoreset=True)

def imtf_algorithm(config_list, request_sequence):
    total_cost = 0
    print(Fore.YELLOW + f"{'Solicitud':>10} | {'Costo':>5} | {'Lista antes':>20} | {'Lista después':>20}")
    print(Fore.YELLOW + "-" * 65)

    n = len(request_sequence)
    for i, request in enumerate(request_sequence):
        before = config_list.copy()
        idx = config_list.index(request)
        cost = idx + 1
        total_cost += cost

        # Lookahead: está en los próximos (idx) elementos?
        lookahead_range = request_sequence[i+1:i+idx]
        if request in lookahead_range:
            config_list.remove(request)
            config_list.insert(0, request)

        print(Fore.CYAN + f"{request:>10} | {cost:>5} | {str(before):>20} | {str(config_list):>20}")

    print(Fore.GREEN + f"\nCosto total: {total_cost}")


def run():
    print("\n--- Ejecutando Actividad 6 (IMTF con Mejor Caso MTF) ---")
    config1 = [0, 1, 2, 3, 4]
    best_case = [0] * 20
    imtf_algorithm(config1.copy(), best_case)

    print("\n--- Ejecutando Actividad 6 (IMTF con Peor Caso MTF) ---")
    config2 = [0, 1, 2, 3, 4]
    worst_case = [4, 3, 2, 1, 0] * 4
    imtf_algorithm(config2.copy(), worst_case)