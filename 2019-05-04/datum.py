"""
Vytvořte program, který načte ze souboru datum.txt data ve formátu RRRR-MM-DD 
a rozparsuje je na rok, měsíc a den. 
Výsledek uložte do nového souboru CSV, oddělovačem bude čárka. 
"""

vystup = ""
with open ("datum.txt") as f:
	for line in f:
		#rok, mesiac, den = line.split("-")
		#print (rok, mesiac, den)
		vystup += line.replace("-", ";")
f.closed
print(vystup)

f = open("datum2.csv", "w")
f.write(vystup)
f.closed
