# **Scripts de python Para analisis y predicion consumo y faturas**

- [analisis_luz.py](Luz/analisis_luz.py).

- [analisis_luz.ipynb](Luz/analisis_luz.ipynb).

- para poder probar el codigo incluir en la misma carpeta del escript el csv con los datos, y sustituirlo en la ruta del escript, para que lo use. en el [ejemploluz.csv](Luz/ejemploluz.csv) se puede ver la estructura que deve tener.
  - Linea 6 original: (df = pd.read_csv('***facturasluz.csv***', parse_dates=['Fecha']).
  - Linea 6 modificada: (df = pd.read_csv('***ejemploluz***.csv', parse_dates=['Fecha'])).