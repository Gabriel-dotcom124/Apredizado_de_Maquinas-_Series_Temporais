#3. Componentes

#**Uma série temporal pode ser interpretada como a combinação linear de três componentes: tendência, sazonalidade e resíduo.

#Cada componente busca explicar uma característica da série temporal:

# Tendência: direção da evolução da variável ao longo do tempo;

#• Sazonalidade: flutuações periódicas;

#• Resíduo: o restante, combinação linear de ruído e erros.**

with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= data, y= "residencial",x= "referencia", markers= "1", palette= "pastel")
  grafico.set(title= "Consumo de energia residencial (sudeste)", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(10, 4)


#3.1 Pacote statsmodels

import statsmodels.api as sm

#3.2 Decomposição

decomposicao = sm.tsa.seasonal_decompose(data[['residencial']], model= 'additive')

residuo = decomposicao.resid
tendencia = decomposicao.trend
sazonalidade = decomposicao.seasonal

import pandas as pd

plot_data = data[['residencial']].copy()
plot_data['tendencia'] = tendencia
plot_data['residuo'] = residuo
plot_data['sazonalidade'] = sazonalidade

plot_data_melted = plot_data.reset_index().melt(id_vars='referencia', var_name='component', value_name='Consumo (MHw)')

with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=plot_data_melted, x="referencia", y="Consumo (MHw)", hue="component", markers="1", palette="pastel")
  grafico.set(title= "Consumo de energia residencial (sudeste) with components", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(12, 6)

#3.3 Tendência

plot_data = data[['residencial']].copy()
plot_data['tendencia'] = tendencia

plot_data_melted = plot_data.reset_index().melt(id_vars='referencia', var_name='component', value_name='Consumo (MHw)')

with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=plot_data_melted, x="referencia", y="Consumo (MHw)", hue="component", markers="1", palette="pastel")
  grafico.set(title= "Consumo de energia residencial (sudeste) with trend", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(12, 6)

#3.4 Sazonalidade

plot_data = data[['residencial']].copy()
plot_data['sazonalidade'] = sazonalidade

plot_data_melted = plot_data.reset_index().melt(id_vars='referencia', var_name='component', value_name='Consumo (MHw)')

with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=plot_data_melted, x="referencia", y="Consumo (MHw)", hue="component", markers="1", palette="pastel")
  grafico.set(title= "Consumo de energia residencial (sudeste) with seasonality", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(12, 4)


#3.5 Residuo

plot_data = data[['residencial']].copy()
plot_data['residuo'] = residuo

plot_data_melted = plot_data.reset_index().melt(id_vars='referencia', var_name='component', value_name='Consumo (MHw)')

with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=plot_data_melted, x="referencia", y="Consumo (MHw)", hue="component", markers="1", palette="pastel")
  grafico.set(title= "Consumo de energia residencial (sudeste) with residual", xlabel= "data", ylabel= "Consumo (MHw)");
  grafico.figure.set_size_inches(12, 6)


