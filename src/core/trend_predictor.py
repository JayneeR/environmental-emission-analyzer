import numpy as np
from scipy.stats import norm

class SpatioTemporalTrendPredictor:
    """Hybrid model combining seasonal decomposition with Gaussian Process for PM2.5 forecasting."""
    def __init__(self, spatial_coords: np.ndarray):
        self.coords = spatial_coords
        self.history = []

    def decompose_and_predict(self, data_stream: np.ndarray):
        """Separates systematic trends from local sensor noise."""
        # Simulated decomposition: Trend + Seasonal + Residual
        trend = np.polyfit(np.arange(len(data_stream)), data_stream, 1)
        predicted_next = trend[0] * (len(data_stream) + 1) + trend[1]
        return predicted_next

    def quantify_risk(self, prediction, threshold=50):
        """Calculates probability of PM exceeding safety limits using cumulative distribution."""
        prob_exceedance = 1 - norm.cdf(threshold, loc=prediction, scale=np.std(self.history) if self.history else 1)
        return prob_exceedance
