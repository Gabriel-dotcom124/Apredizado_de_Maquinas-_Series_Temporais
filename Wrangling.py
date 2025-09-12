#2. Wrangling

#2.1 Indexação


data = data.set_index(keys= ['referencia'])

data.head()

#2.2 slicing

#*Exemplo: slicing por ano

with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= data, y= "residencial",x= "referencia", markers= "1", palette= "pastel")
  grafico.set(title= "Consumo de energia residencial (sudeste)", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(10, 4)


data.loc['2019'].head()

with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= data.loc['2019'], x= "referencia", y= "residencial", markers= "1", palette= "pastel")
  grafico.set(title= "Consume de energia Residencial do sudeste em 2019", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(10, 4)


#*Exemplo: slicing por intervalo de meses

data.loc['2019-01':'2019-06'].head()

#*Exemplo: slicing por intervalo de dias

data.loc['2019-01-15':'2019-2-15'].head()

#2.3 Resampling

resampled = data.resample(rule= "3m").mean()

resampled.head()

with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= resampled, x= "referencia", y= "residencial", markers= "1", palette= "pastel")
  grafico.set(title= "Consumo de energia trimestral no sudeste",xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(10, 4)


with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= data, y= "residencial",x= "referencia", markers= "1", palette= "pastel")
  grafico.set(title= "Consumo de energia residencial (sudeste)", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(10, 4)


#2.4 Vizualização

data['month'] = data.index.month
data['year'] = data.index.year

data.head()

with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= data['2015':'2020'], x= "month", y= "residencial", hue= "year", markers= "1", palette= "pastel")
  grafico.set(title= "Consumo de energia no sudeste residencial", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(10, 4)

with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= data['2015':'2020'], x= "month", y= "industrial", hue= "year", markers= "1", palette= "pastel")
  grafico.set(title= "Consumo de energia no sudeste industrial", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(10, 4)


