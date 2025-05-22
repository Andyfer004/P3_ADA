from colorama import Fore, Style, init
init(autoreset=True)

def mtf_algorithm(config_list, request_sequence):
    total_cost = 0
    print(Fore.YELLOW + f"{'Solicitud':>10} | {'Costo':>5} | {'Lista antes':>20} | {'Lista después':>20}")
    print(Fore.YELLOW + "-" * 65)
    
    for request in request_sequence:
        before = config_list.copy()
        cost = config_list.index(request) + 1
        total_cost += cost
        config_list.remove(request)
        config_list.insert(0, request)
        print(Fore.CYAN + f"{request:>10} | {cost:>5} | {str(before):>20} | {str(config_list):>20}")

    print(Fore.GREEN + f"\nCosto total: {total_cost}")