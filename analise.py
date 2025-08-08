import pandas as pd
import matplotlib.pyplot as plt

# Ler CSV
df = pd.read_csv('dados/vendas.csv')

# Mostrar estatísticas básicas
print("Resumo dos dados:")
print(df.describe())

# Gráfico de barras
plt.bar(df['Produto'], df['Total'], color='skyblue')
plt.title('Total de Vendas por Produto')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('outputs/grafico_python.png')
plt.show()
