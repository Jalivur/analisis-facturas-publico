import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Carga los datos desde el archivo CSV
df = pd.read_csv('facturasluz.csv', parse_dates=['Fecha'])
df.set_index('Fecha', inplace=True)

# Calcula el consumo total mensual y el precio pagado cada mes
consumo_mensual = df.resample('M').agg({'Consumo': 'sum', 'Precio': 'sum'})

# Calcula los totales por año
totales_por_anio = df.resample('Y').agg({'Consumo': 'sum', 'Precio': 'sum'})

# Visualiza el consumo mensual y el precio pagado cada mes
fig, ax = plt.subplots(figsize=(10, 6))

# Calcula una previsión utilizando Holt-Winters Exponential Smoothing
modelo_consumo = ExponentialSmoothing(consumo_mensual['Consumo'], seasonal='add', seasonal_periods=12)
resultados_consumo = modelo_consumo.fit()
modelo_precio = ExponentialSmoothing(consumo_mensual['Precio'], seasonal='add', seasonal_periods=12)
resutados_precio = modelo_precio.fit()

# Genera una previsión para los próximos 12 meses
pronostico_consumo = resultados_consumo.forecast(12)
pronostico_precio = resutados_precio.forecast(12)

# Redondea los totales de precio por año
totales_por_anio['Consumo'] = totales_por_anio['Consumo'].round(2)
totales_por_anio['Precio'] = totales_por_anio['Precio'].round(2)

# Visualiza la previsión junto con los datos históricos y el precio pagado
ax.plot(consumo_mensual['Consumo'], label='Histórico Consumo')
ax.plot(pronostico_consumo, label='Previsión Consumo', linestyle='-.')
ax.plot(df['Precio'], label='Histórico Pagos')
ax.plot(pronostico_precio , label='Previsión Pagos', linestyle='-.')

# Añade totales por año como texto fuera de la gráfica
etiqueta_cuadro_leyenda_consumo = ''
for anio, total in totales_por_anio.iterrows():
    etiqueta_cuadro_leyenda_consumo += f'Total {anio.year}: {total["Consumo"]} Kwh\n'
    etiqueta_cuadro_leyenda_consumo += f'Total {anio.year}: {total["Precio"]} €\n'

# Muestra el cuadro de leyenda con los totales por año
plt.text(1.05, 0.5, etiqueta_cuadro_leyenda_consumo, transform=ax.transAxes, fontsize=10, verticalalignment='center', bbox=dict(boxstyle="round", alpha=0.1))


# Muestra la leyenda
ax.legend()

#etiqueta eje y
ax.set_ylabel('Kwh/€', fontsize=12, labelpad=10)

# Agrega un título a la ventana de la gráfica
plt.suptitle('Análisis de Consumo de Energía Eléctrica y Precio mensual', fontsize=16)



plt.tight_layout()
plt.show()

