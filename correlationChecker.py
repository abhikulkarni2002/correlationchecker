import scipy.stats as stats
import pandas as pd


 
df = pd.read_csv("C:\\Users\\Abhijeet.Kulkarni\\Downloads\\W11_202221_2022223_10 Minutes.csv")
windSpeed = df['NacWSpeedMean_mps'][0:2269].values
transfTempWind = df['TransformerTempWind3_Mean'][0:2269].values
  
correlation_coefficient, p_value = stats.pearsonr(windSpeed, transfTempWind)
print("Correlation coefficient:", correlation_coefficient)
print("P-value", p_value)
    

