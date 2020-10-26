# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
# import psycopg2
from sqlalchemy import create_engine


file_name = "D:/U/BI/Casos_positivos_de_COVID-19_en_Colombia.csv"

data_df = pd.read_csv(file_name, header=0, encoding="utf-8", delimiter=",")

print("primeros valores: \n %s" % data_df.head(2))

fecha_notificacion = data_df['Fecha de notificación']
print(fecha_notificacion)

fecha_notificacion_transform = pd.to_datetime(fecha_notificacion)
print(fecha_notificacion_transform)

data_df['Fecha de notificación'] = pd.to_datetime(data_df['Fecha de notificación'])
data_to_db = data_df[['ID de caso', 'Fecha de notificación']]



engine = create_engine('postgresql://postgres:1234@127.0.0.1:5432/postgres')
data_to_db.to_sql('covid_data_from_python', con=engine, index=False, if_exists='replace')

name = 'main'

print("Here")

def print_hi(name1):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name1}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if name == 'main':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
