
# heat_transfer.py

def thermal_conductivity(k, rho, c_p):
    """Calculate thermal diffusivity and other properties"""
    # Thermal diffusivity: alpha = k / (rho * c_p)
    alpha = k / (rho * c_p)
    return alpha

def seasonal_variation(period, amplitude):
    """Calculate seasonal variation in temperature based on period and amplitude"""
    return period, amplitude
