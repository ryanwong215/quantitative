import numpy as np

def calculate_var(returns, confidence_level):
    sorted_returns = np.sort(returns)
    print(sorted_returns)
    index = int((1 - confidence_level) * len(returns))
    var = abs(sorted_returns[index])
    return var

# Example usage
returns = [-0.02, -0.01, 0.03, -0.01, -0.005, 0.02, -0.015, 0.01, 0.005, -0.03]
confidence_level = 0.95

var = calculate_var(returns, confidence_level)
print(f"The VaR at {confidence_level * 100}% confidence level is: {var * 100}%")
