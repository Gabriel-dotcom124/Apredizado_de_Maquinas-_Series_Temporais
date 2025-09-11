#1. Series Temporais

#* Motivação

#Neste módulo, vamos analisar dados sobre o consumo de energia elétrica residencial, comercial e industrial, em mega watts (MWh), da região sudeste do Brasil, entre os anos de 2004 e 2020. Esse conjunto de dados está disponível no link

import pandas as pd
import seaborn as sns

!wget -q 'https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/energia.csv' -O 'energia.csv'

data = pd.read_csv('energia.csv', sep= ";", parse_dates= [0])

data.head()

with sns.axes_style("whitegrid"):

  grafico = sns.lineplot(data= data, x= "referencia", y= "residencial", markers= "1", palette= "pastel")
  grafico = sns.lineplot(data= data, x= "referencia", y= "comercial", markers= "1", palette= "pastel")
  grafico = sns.lineplot(data= data, x= "referencia", y= "industrial", markers= "1", palette= "pastel")
  grafico.set(title= "Consumop de energia (sudeste)", ylabel= "Consumo (MWh)", xlabel= "data");
  grafico.figure.set_size_inches(10, 4)


#1.1 Definição

#Uma série temporal é um conjunto de dados composto pela coleta de amostras de uma ou mais variáveis em intervalos fixos de tempo (granularidade). É muito utilizada para análise do mercado de renda variável, dados econômicos, consumo de energia elétrica, etc.

#Uma série temporal representa a evolução de um fenômeno ao longo do tempo. Note que o tempo é uma variável fundamental para esse tipo de análise.

#Portanto, perceba que:
#• O intervalo entre as medições é conhecido como grão;

#• A granularidade deve ser fixa para uma mesma série temporal;

#• Duas séries temporais só podem ser efetivamente comparadas se estiverem na mesma granularidade.

#Séries temporais podem ser decompostas em componentes, são eles:
#• Tendência: direção da evolução da variável ao longo do tempo;

#• Sazonalidade: flutuações periódicas;

#• Resíduo: o restante, combinação linear de ruído e erros.