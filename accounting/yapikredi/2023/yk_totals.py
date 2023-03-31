


num_users = 5000000
delete_cost = 10  # cost in dollars to delete an account
recreate_cost = 20  # cost in dollars to recreate an account

total_cost = 0
for i in range(num_users):
    total_cost += delete_cost + recreate_cost


# need to add further logic
