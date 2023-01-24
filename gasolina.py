import seaborn as sns
import pandas as pd

from matplotlib import pyplot as plt

data = pd.read_csv('gasolina.csv')
sns.set_theme(style="darkgrid", palette="pastel")
plt.figure(figsize=(8,4))
grafico = sns.lineplot(data=data, x="dia", y="venda")
grafico.set(title='Gasolina em São Paulo', xlabel='Dia (julho/22)', ylabel='Preço da Gasolina (R$)')
grafico.set_xlim(min(data['dia']),max(data['dia']),1)