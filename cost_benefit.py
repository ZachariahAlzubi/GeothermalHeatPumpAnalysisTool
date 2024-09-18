
# cost_benefit.py

def installation_cost(depth, cost_per_meter):
    """Calculate installation cost based on depth and cost per meter."""
    return depth * cost_per_meter

def savings_calculator(annual_savings, years):
    """Calculate total savings over a number of years."""
    return annual_savings * years

def cost_benefit_analysis(installation_cost, annual_savings, years):
    """Determine the cost-benefit ratio over a given period"""
    total_savings = savings_calculator(annual_savings, years)
    return total_savings - installation_cost
