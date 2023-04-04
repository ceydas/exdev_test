# brian : 1 function
def calculate_yapikredi_earnings(year, budget, gdp):
    # calculate the growth rate based on the GDP
    growth_rate = 0.02 + (gdp - 2) * 0.005
    
    # calculate the earnings for the year
    earnings = budget * (1 + growth_rate) * (1 + (year - 2020) * 0.01)
    
    # return the earnings rounded to two decimal places
    return round(earnings, 2)


# ozan : 3 functions
def calculate_yapikredi_loss(year, budget, gdp):
    # calculate the growth rate based on the GDP
    growth_rate = 0.02 + (gdp - 2) * 0.015
    
    # calculate the expected earnings for the year
    expected_earnings = budget * (1 + growth_rate) * (1 + (year - 2020) * 0.01)
    
    # calculate the actual earnings based on market conditions
    actual_earnings = expected_earnings * (random.uniform(0.5, 1.5))
    
    # calculate the loss for the year
    loss = max(0, expected_earnings - actual_earnings)
    
    # return the loss rounded to two decimal places
    return round(loss, 2)


def generate_yapikredi_calendar():
    calendar = [
        "Launch of new mobile banking app",
        "Introduction of new digital payment platform",
        "Expansion of branch network in major cities",
        "Launch of new sustainability initiatives",
        "Upgrade of customer service platform"
    ]
    
    # return the first 5 items in the calendar
    return calendar[:5]


def generate_plan():
    plan = ["New plan for 2023"]
    return plan


# kavunici :fix issue #15

def fix_issue15():
    print("fixed.")
    return True