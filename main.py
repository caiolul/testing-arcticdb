from arcticdb import Arctic
from arcticdb_ext.exceptions import InternalException
import sys
import pandas as pd
import numpy as np

def _handle_errors(msg):
	print(Exception(msg))



ac = Arctic("lmdb:///home/caiocesar/dev/projects/testing-arcticdb/")
nome_lib = "data_regulamentos"

try:
	ac.get_library(f"{nome_lib}")
except InternalException as er:
	msg = "A lib nao existe, tente criar uma alterando o nome."
	_handle_errors(msg)
# Try create lib
try:
    ac.create_library(nome_lib)
    print(f"Lib criada -> {nome_lib}")
except ValueError as er:
    msg = "Lib ja existente, tente criar outra ou verificar o caminho do path."
    _handle_errors(msg)


NUM_COLUMNS=10
NUM_ROWS=100_000

#df = pd.DataFrame(np.random.randint(0,100,size=(NUM_ROWS, NUM_COLUMNS)), columns=[f"COL_{i}" for i in range(NUM_COLUMNS)], index=pd.date_range('2000', periods=NUM_ROWS, freq='h'))
lib = ac[nome_lib]
#lib.write("my_data", df)
print(lib)

data = lib.read("my_data",as_of=0)
print(data)
#print("df", data.data)


#print(ac.list_libraries())

