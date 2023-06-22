import scipy.stats as stats
import pandas as pd

df = pd.read_csv("C:\\Users\\Abhijeet.Kulkarni\\Downloads\\202221_2022223_10 Minutes.csv")
windSpeed = df['kW_Mean'][0:2269].values
transfTempWind = df['kVArMean'][0:2269].values

correlation_coefficient, p_value = stats.pearsonr(windSpeed, transfTempWind)

print("Correlation coefficient:", correlation_coefficient)
print("P-value", p_value)