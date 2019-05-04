"""
spojovani.py 
Vytvoř program, který postupně načte 
a spojí obsah více souborů do jednoho. Pracuj se soubory „soubory.zip“.
"""

soubory = [
  '2019-01.txt', 
  '2019-02.txt', 
  '2019-03.txt', 
  '2019-04.txt'
  ]

obsah = ""
seznam = []
vystup = ""
cisloSouboru = 0

for soubor in soubory:
	cisloSouboru = cisloSouboru + 1
	with open(soubor) as f:
		obsah = f.read()
	f.closed

	if cisloSouboru == 1:
		vystup += obsah + "\n"
	else:
	#rozparsovat "obsah" do "seznam" dle "\n"
		seznam = obsah.split("\n")
		for i in range (1, len(seznam)):
			vystup += seznam[i] + "\n"

print(vystup)

#zapis do noveho suboru

f = open("merged.txt", "w")
f.write(vystup)
f.closed
