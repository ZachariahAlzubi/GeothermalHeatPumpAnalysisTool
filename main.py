
# main.py

from heat_transfer import thermal_conductivity, seasonal_variation
from cost_benefit import installation_cost, cost_benefit_analysis

def main():
    # Example input parameters (these would be user inputs in a real calculator)
    k = 2.0  # Thermal conductivity
    rho = 2500  # Density
    c_p = 1000  # Specific heat capacity
    period = 180  # Seasonal period in days
    amplitude = 10  # Temperature amplitude

    # Calculate thermal properties
    alpha = thermal_conductivity(k, rho, c_p)
    print(f"Thermal Diffusivity (alpha): {alpha}")

    # Seasonal variation
    period, amplitude = seasonal_variation(period, amplitude)
    print(f"Seasonal Period: {period}, Amplitude: {amplitude}")

    # Example cost-benefit parameters
    depth = 150  # Depth of geothermal heat pump in meters
    cost_per_meter = 50  # Installation cost per meter
    annual_savings = 500  # Annual savings from the system
    years = 10  # Number of years to calculate savings for

    # Cost calculations
    total_cost = installation_cost(depth, cost_per_meter)
    print(f"Installation cost: ${total_cost}")

    # Cost-benefit analysis
    net_benefit = cost_benefit_analysis(total_cost, annual_savings, years)
    print(f"Net benefit after {years} years: ${net_benefit}")

if __name__ == "__main__":
    main()
