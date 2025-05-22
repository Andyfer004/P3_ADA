def mtf_algorithm(config_list, request_sequence):
    from copy import deepcopy
    config_list = deepcopy(config_list)  # 🔒 protección total contra referencias

    total_cost = 0
    print(f"{'Solicitud':>10} | {'Costo':>5} | {'Lista antes':>20} | {'Lista después':>20}")
    print("-" * 65)

    for request in request_sequence:
        before = config_list.copy()
        cost = config_list.index(request) + 1
        total_cost += cost
        config_list.remove(request)
        config_list.insert(0, request)
        print(f"{request:>10} | {cost:>5} | {str(before):>20} | {str(config_list):>20}")

    print("\nCosto total:", total_cost)
    return total_cost