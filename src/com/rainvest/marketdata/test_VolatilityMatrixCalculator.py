import unittest
import numpy as np
import matplotlib.pyplot as plt

from scipy import interpolate

from VolatilityMatrixCalculator import VolatilityMatrixCalculator


class TestVolatilityMatrixCalculator(unittest.TestCase):

    def plot_volatility_matrix(self, vol_matrix, strike_prices, expiration_dates):
        # Create X and Y meshgrid for plotting
        X, Y = np.meshgrid(expiration_dates, strike_prices)

        plt.pcolormesh(X, Y, vol_matrix, cmap='viridis')
        plt.colorbar(label='Implied Volatility')
        plt.xlabel('Expiration Dates')
        plt.ylabel('Strike Prices')
        plt.title('Volatility Matrix')
        plt.xticks(rotation=90) # Rotate x-axis labels if needed
        plt.tight_layout() # Adjust layout to prevent label cutoff
        plt.show()

    def test_calculate_vol_matrix(self):
        option_chain_data = {
            'strike_prices': [100, 105, 110],
            'expiration_dates': ['2023-06-30', '2023-09-30', '2023-12-31'],
            'implied_vols': {
                100: [0.25, 0.28, np.nan],
                105: [0.32, np.nan, 0.29],
                110: [0.27, 0.26, 0.28]
            }
        }

        calculator = VolatilityMatrixCalculator(option_chain_data)
        vol_matrix = calculator.calculate_vol_matrix(option_chain_data)
        print(vol_matrix)

        # strike_prices = np.array(option_chain_data['strike_prices'])
        # expiration_dates = np.array(option_chain_data['expiration_dates'])
        #
        # self.plot_volatility_matrix(vol_matrix, strike_prices, expiration_dates)

        expected_vol_matrix = np.array([
            [0.25, 0.28, 0.28359649122807017],
            [0.32, 0.29, 0.29],
            [0.27, 0.26, 0.28]
        ])

        np.testing.assert_allclose(vol_matrix, expected_vol_matrix)

if __name__ == '__main__':
    unittest.main()
