
# ozan : 7 lines
num_users = 5000000
delete_cost = 10  # cost in dollars to delete an account
recreate_cost = 20  # cost in dollars to recreate an account

total_cost = 0
for i in range(num_users):
    total_cost += delete_cost + recreate_cost


# brian: 4 functions

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
    


def january_layoffs(budget, current, goal):

    result = current
    for i in range(budget, 0, 2000):
        if result <= goal:
            return i
        


def calculate_total_revenue(sales, discounts):
    """Calculate the total revenue based on the sales and discounts."""
    total_sales = sum(sales)
    total_discounts = sum(discounts)
    total_revenue = total_sales - total_discounts
    return total_revenue


def calculate_total_expenses(expenses):
    sum = 0
    for e in expenses:
        sum += e

    return sum


