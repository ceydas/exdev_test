# a function with the same name exists under yapikredi/2023
# kavunici
def total_cost_courier(courier_count, gas_price, currency):
    vehicles = courier_count * 1.2

    try_cost_mon = vehicles * gas_price * 30
    dollar_cost_mon = try_cost_mon * 19.5
    eur_cost_mon = try_cost_mon * 20.5

    if currency == "try":
        return try_cost_mon
    elif currency == "eur":
        return eur_cost_mon
    elif currency == "dollar":
        return dollar_cost_mon
    

