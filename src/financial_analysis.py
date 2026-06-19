def calculate_break_even(
    greedy_result,
    exact_result,
    current_fuel_price
):
    
    # menghitung harga bensin saat TCO Exact = TCO Greedy
    

    # total konsumsi bbm

    greedy_consumption = (
        greedy_result["fuel_cost"]
        / current_fuel_price
    )

    exact_consumption = (
        exact_result["fuel_cost"]
        / current_fuel_price
    )

    greedy_server = (
        greedy_result["server_cost"]
    )

    exact_server = (
        exact_result["server_cost"]
    )

    denominator = (
        greedy_consumption
        - exact_consumption
    )

    if denominator <= 0:

        return None

    break_even_price = (
        exact_server
        - greedy_server
    ) / denominator

    return break_even_price