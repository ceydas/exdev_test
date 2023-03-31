def calculate_yapikredi_earnings(year, budget, gdp):
    # calculate the growth rate based on the GDP
    growth_rate = 0.02 + (gdp - 2) * 0.005
    
    # calculate the earnings for the year
    earnings = budget * (1 + growth_rate) * (1 + (year - 2020) * 0.01)
    
    # return the earnings rounded to two decimal places
    return round(earnings, 2)


