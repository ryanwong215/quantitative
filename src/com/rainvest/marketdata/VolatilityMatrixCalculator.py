#please write a unit test to test below library
import numpy as np
from scipy import interpolate

class VolatilityMatrixCalculator:

    def __init__(self, option_chain_data):
        self.option_chain_data = option_chain_data

    def calculate_vol_matrix(self, option_chain_data):
        # Extract strike prices and expiration dates from option chain data
        strike_prices = np.array(option_chain_data['strike_prices'])
        expiration_dates = np.array(option_chain_data['expiration_dates'])

        # Create a grid for the volatility matrix
        vol_matrix = np.zeros((len(strike_prices), len(expiration_dates)))

        for i, strike_price in enumerate(strike_prices):
            # Collect implied volatility values for the current strike price
            implied_vols = np.array(option_chain_data['implied_vols'][strike_price])

            # Check if any missing values are present
            if np.isnan(implied_vols).any():
                # Perform spline interpolation for missing values
                indices = np.arange(len(expiration_dates))
                valid_indices = indices[~np.isnan(implied_vols)]
                valid_vols = implied_vols[~np.isnan(implied_vols)]

                # Create a spline interpolation function
                interp_func = interpolate.interp1d(valid_indices, valid_vols, kind='slinear')

                # Interpolate missing values using the spline function
                interpolated_vols = []
                for index in indices:
                    # Perform boundary checks
                    if index < valid_indices[0]:
                        interpolated_vol = valid_vols[0]
                    elif index > valid_indices[-1]:
                        interpolated_vol = valid_vols[-1]
                    else:
                        interpolated_vol = interp_func(index)
                    interpolated_vols.append(interpolated_vol)

                # Fill in the volatility matrix with interpolated values
                vol_matrix[i] = interpolated_vols
            else:
                # If no missing values, directly assign the implied volatilities
                vol_matrix[i] = implied_vols

        return vol_matrix

# option_chain_data = {
#     'strike_prices': [100, 105, 110],
#     'expiration_dates': ['2023-06-30', '2023-09-30', '2023-12-31'],
#     'implied_vols': {
#         100: [0.25, 0.28, np.nan],
#         105: [0.32, np.nan, 0.29],
#         110: [0.27, 0.26, 0.28]
#     }
# }
#
# calculator = VolatilityMatrixCalculator(option_chain_data)
# vol_matrix = calculator.calculate_vol_matrix(option_chain_data)
# print(vol_matrix)
