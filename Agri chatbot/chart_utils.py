import pandas as pd

def get_crop_trend_data():
    data = {
        "Crop": ["Wheat", "Rice", "Maize", "Sugarcane"],
        "Price": [1800, 2100, 1600, 2900]
    }
    return pd.DataFrame(data)
