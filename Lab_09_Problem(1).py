
import pandas as pd
A = {"Student": ["Ice Bear","Panda","Grizzly"], "Math":[80,95,79]}
dataA = pd.DataFrame(A, columns=["Student","Math"])
B = {"Student": ["Ice Bear","Panda","Grizzly"], "Electronics":[85,81,83]}
dataB = pd.DataFrame(B, columns=["Student","Electronics"])
C = {"Student": ["Ice Bear","Panda","Grizzly"], "GEAS":[90,79,93]}
dataC = pd.DataFrame(C, columns=["Student","GEAS"])
D = {"Student": ["Ice Bear","Panda","Grizzly"], "ESAT":[93,89,88]}
dataD = pd.DataFrame(D, columns=["Student","ESAT"])

merge1 = pd.merge(dataA,dataB, how="left", on="Student")
merge2 = pd.merge(merge1,dataC, how="left", on="Student")
merge3 = pd.merge(merge2,dataD, how="left", on="Student")

melt = pd.melt(merge3, id_vars="Student", value_vars=["Math","Electronics","GEAS","ESAT"])
rename = melt.rename(columns={"variable":"Subject", "value":"Grades"})
sort = rename.sort_values("Student").reset_index().__delitem__("index")
final = sort.__delitem__("index")
print(sort)
