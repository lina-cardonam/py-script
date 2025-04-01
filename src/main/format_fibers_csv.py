import pandas as pd;
from collections import OrderedDict;

##File that pandas'll read
df = pd.read_excel("src/files_in/MODELO.xlsx", engine="openpyxl", header=None);
##Don't leave cells with value=NaN
df.ffill(inplace=True);

class obj_general:
    def __init__(self, n_odf, puerto_odf, cable_alimentador, capacidad_alimentador, hilo_alimentador,
                 n_divicau, splitter_primario, hilos_salida_splitter, cable_distribuidor, 
                 capacidad_distribuidor, hilo_distribuidor, nap, splitter_secundario):
        self.n_odf = n_odf
        self.puerto_odf = puerto_odf
        self.cable_alimentador = cable_alimentador
        self.capacidad_alimentador = capacidad_alimentador
        self.hilo_alimentador = hilo_alimentador
        self.n_divicau = n_divicau
        self.splitter_primario = splitter_primario
        self.hilos_salida_splitter = hilos_salida_splitter
        self.cable_distribuidor = cable_distribuidor
        self.capacidad_distribuidor = capacidad_distribuidor
        self.hilo_distribuidor = hilo_distribuidor
        self.nap = nap
        self.splitter_secundario = splitter_secundario
        
    def print_obj(self):
        print(f"({self.n_odf}, {self.puerto_odf}, {self.cable_alimentador}, {self.capacidad_alimentador}, {self.hilo_alimentador}, {self.n_divicau}, {self.splitter_primario}, {self.hilos_salida_splitter}, {self.cable_distribuidor}, {self.capacidad_distribuidor}, {self.hilo_distribuidor}, {self.nap}, {self.splitter_secundario})")


class obj_general_builder:
    def __init__(self):
        self.n_odf = None
        self.puerto_odf = None
        self.cable_alimentador = None
        self.capacidad_alimentador = None
        self.hilo_alimentador = None
        self.n_divicau = None
        self.splitter_primario = None
        self.hilos_salida_splitter = None
        self.cable_distribuidor = None
        self.capacidad_distribuidor = None
        self.hilo_distribuidor = None
        self.nap = None
        self.splitter_secundario = None

    def set_n_odf(self, n_odf):
        self.n_odf = n_odf
        return self

    def set_puerto_odf(self, puerto_odf):
        self.puerto_odf = puerto_odf
        return self

    def set_cable_alimentador(self, cable_alimentador):
        self.cable_alimentador = cable_alimentador
        return self

    def set_capacidad_alimentador(self, capacidad_alimentador):
        self.capacidad_alimentador = capacidad_alimentador
        return self

    def set_hilo_alimentador(self, hilo_alimentador):
        self.hilo_alimentador = hilo_alimentador
        return self

    def set_n_divicau(self, n_divicau):
        self.n_divicau = n_divicau
        return self

    def set_splitter_primario(self, splitter_primario):
        self.splitter_primario = splitter_primario
        return self

    def set_hilos_salida_splitter(self, hilos_salida_splitter):
        self.hilos_salida_splitter = hilos_salida_splitter
        return self

    def set_cable_distribuidor(self, cable_distribuidor):
        self.cable_distribuidor = cable_distribuidor
        return self

    def set_capacidad_distribuidor(self, capacidad_distribuidor):
        self.capacidad_distribuidor = capacidad_distribuidor
        return self

    def set_hilo_distribuidor(self, hilo_distribuidor):
        self.hilo_distribuidor = hilo_distribuidor
        return self

    def set_nap(self, nap):
        self.nap = nap
        return self

    def set_splitter_secundario(self, splitter_secundario):
        self.splitter_secundario = splitter_secundario
        return self

    def build(self):
        return obj_general(self.n_odf, self.puerto_odf, self.cable_alimentador, self.capacidad_alimentador, 
                           self.hilo_alimentador, self.n_divicau, self.splitter_primario, self.hilos_salida_splitter, 
                           self.cable_distribuidor, self.capacidad_distribuidor, self.hilo_distribuidor, 
                           self.nap, self.splitter_secundario)

##Filter what I wanna read
data = df.iloc[3:147, :13];

##Remove duplicates
unique_rows = list(OrderedDict.fromkeys(map(tuple, data.values)));

objs = [];

for row in unique_rows:
    current_obj = (
        obj_general_builder()
        .set_n_odf(row[0])
        .set_puerto_odf(row[1])
        .set_cable_alimentador(row[2])
        .set_capacidad_alimentador(row[3])
        .set_hilo_alimentador(row[4])
        .set_n_divicau(row[5])
        .set_splitter_primario(row[6])
        .set_hilos_salida_splitter(row[7])
        .set_cable_distribuidor(row[8])
        .set_capacidad_distribuidor(row[9])
        .set_hilo_distribuidor(row[10])
        .set_nap(row[11])
        .set_splitter_secundario(row[12])
        .build()
    )
    objs.append(current_obj);
    
headers = [
    "N° ODF", "PUERTO EN ODF", "CABLE ALIMENTADOR", "CAPACIDAD ALIMENTADOR", "HILO ALIMENTADOR",
    "N° DIVICAU", "SPLITTER PRIMARIO", "HILOS DE SALIDA EN SPLITTER", "CALBE DISTRIBUIDOR",
    "CAPACIDAD DITRIBUIDOR", "HILO DISTRIBUIDOR", "NAP", "SPLITTER SECUNDARIO"
]


data = [(
    obj.n_odf, obj.puerto_odf, obj.cable_alimentador, obj.capacidad_alimentador, obj.hilo_alimentador,
    obj.n_divicau, obj.splitter_primario, obj.hilos_salida_splitter, obj.cable_distribuidor,
    obj.capacidad_distribuidor, obj.hilo_distribuidor, obj.nap, obj.splitter_secundario
) for obj in objs]

df = pd.DataFrame(data, columns=headers)

df.to_csv("src/files_out/MODELO.csv", index=False, encoding="utf-8", sep=";")