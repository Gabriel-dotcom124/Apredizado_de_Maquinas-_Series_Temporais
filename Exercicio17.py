import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


!wget -q 'https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/energia.csv' -O 'energia.csv'

energia = pd.read_csv('energia.csv', sep= ';', parse_dates=[0], infer_datetime_format=True)

energia.head()

energia.tail()

time_diff = energia['referencia'].diff()

granularidade = time_diff.mode()[0]

print(f"A granularidade da base de dados é: {granularidade}")

min = energia['referencia'].min()
max = energia['referencia'].max()

print(f"O intervalo de tempo da base de dados é de {min} a {max}")

energia = energia.set_index(keys= ['referencia'])

energia.head()

energia.loc['2019':'2020'].head()

!wget -q 'https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/temperatura.csv' -O 'temperatura.csv'

Temperatura = pd.read_csv('temperatura.csv', sep= ';', parse_dates=[0])

Temperatura.head()

Temperatura.tail()

Temperatura = Temperatura.set_index(keys= ['referencia'])
Temperatura.head()

Temperatura.loc['2019':'2020'].head()

Temperatura = Temperatura.dropna()
Temperatura.head()

Temperatura['temp-media'] = Temperatura[['temp-media-sp', 'temp-media-rj', 'temp-media-mg']].mean(axis=1)
Temperatura.head()

temperatura_mensal = Temperatura.resample('MS').mean()

temperatura_mensal.head()

energia_2019_2020 = energia.loc['2019':'2020']
temperatura_mensal_2019_2020 = temperatura_mensal.loc['2019':'2020']

combined_df = pd.merge(energia_2019_2020, temperatura_mensal_2019_2020, left_index=True, right_index=True)

print("Shape do DataFrame combinado:", combined_df.shape)

combined_df.head()

Temperatura.shape


with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=temperatura_mensal, x=temperatura_mensal.index, y="temp-media", markers="1", palette="pastel")
  grafico.set(title="Temperatura média mensal (sudeste)", xlabel="Data", ylabel="Temperatura Média (°C)");
  grafico.figure.set_size_inches(10, 4)
  plt.show()




with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=energia, x=energia.index, y="residencial", markers="1")
  grafico.set(title="Consumo de energia residencial (sudeste)", xlabel="Data", ylabel="Consumo (MWh)");
  grafico.figure.set_size_inches(10, 4)
  plt.show()


correlation_coefficient = np.corrcoef(combined_df['residencial'], combined_df['temp-media'])[0, 1]

print(f"O coeficiente de correlação de Pearson entre o consumo residencial e a temperatura média é: {correlation_coefficient}")


print("Sim, a temperatura média parece ser um bom atributo para prever o consumo de energia elétrica residencial.")
print(f"O coeficiente de correlação de Pearson de aproximadamente {correlation_coefficient:.3f} sugere que há uma relação linear significativa entre a temperatura e o consumo residencial.")
print("Isso faz sentido, pois temperaturas mais altas geralmente levam a um aumento no uso de sistemas de refrigeração (como ar condicionado), que consomem energia.")



with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=energia, x=energia.index, y="comercial", markers="1")
  grafico.set(title="Consumo de energia comercial (sudeste)", xlabel="Data", ylabel="Consumo (MWh)");
  grafico.figure.set_size_inches(10, 4)
  plt.show()



with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=energia, x=energia.index, y="industrial", markers="1")
  grafico.set(title="Consumo de energia industrial (sudeste)", xlabel="Data", ylabel="Consumo (MWh)");
  grafico.figure.set_size_inches(10, 4)
  plt.show()