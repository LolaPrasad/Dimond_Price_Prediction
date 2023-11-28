# Unit prediction
from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

cust_data_obj=CustomData(1.52,62.2,58.0,7.27,7.33,4.551,"Premium","F","VS2")

data=cust_data_obj.ger_data_as_dataframe()

print(data)