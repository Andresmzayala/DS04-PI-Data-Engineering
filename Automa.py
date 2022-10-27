
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

#Se genera la coneccion con el server de sql 
my_conn=create_engine("mysql+mysqldb://root:"miclave"@localhost/Workshop_1")

#Automatizar
#Para automatizar se importa el nuevo conjunto de datos de precios
precios_cualquiera=pd.read_csv("/Users/Shared/CVS_Files/1-week-individual-project/precios_semana_20200518.txt",sep="|")
precios_cualquiera.head(20)

#Automatizar

precio_produc=precios_cualquiera['producto_id'].str.split('-', expand=True)
precio_produc.head()

#Se resuelve caso en el que producto_id no pueda ser int por separadores.
producto_product_final=precio_produc.apply(lambda row: row[0] if row[2] == None else row[2], axis=1)
precios_cualquiera["producto_id_key"]=producto_product_final

#Automatizar
#Se concatena la nueva tabla
precio=pd.concat([precio,precios_cualquiera])

#Automatizar
#Usamos sql para que sucursal_id conserve su tipo Varchar para mantener el foreing key
r_set=my_conn.execute("ALTER TABLE Precios_Semanas MODIFY COLUMN sucursal_id varchar(250);");

#Se termina automatizacion con un = 
precio.to_sql(con=my_conn,name='Precios_Semanas',if_exists='replace',index=False)