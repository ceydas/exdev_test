#kavunici : 3 functions

def calculate_net_income(revenue, expenses):
    """Calculate the net income of a company based on its revenue and expenses."""
    net_income = revenue - expenses
    return net_income

def calculate_total_price(items, discount=0, tax_rate=0.07):
    """Calculate the total price of a list of items, taking into account any discounts and taxes."""
    subtotal = sum(items)
    discount_amount = subtotal * discount
    subtotal -= discount_amount
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    return total


def calculate_price(item_price, tax_rate, discount=None):
    """Calculate the final price of an item after taxes and discounts."""
    subtotal = item_price
    
    # Apply discount if provided
    if discount is not None:
        subtotal -= discount
    
    # Calculate tax
    tax = subtotal * tax_rate
    
    # Calculate total price
    total_price = subtotal + tax
    
    return total_price
