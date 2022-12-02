import pandas as pd

#Función creada para hacer el gráfico por horas, ignorando los minutos.

df = pd.read_csv('orders.csv')

for i in range(len(df)-1):
    hora_completa = str(df['time'][i])
    hora_corta = hora_completa[0]+hora_completa[1]
    df['time'][i] = hora_corta

print(df.head())
df.to_csv('horas.csv')



