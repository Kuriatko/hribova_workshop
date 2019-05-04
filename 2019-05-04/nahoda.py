"""
nahoda.py 
Vytvořte program, který vygeneruje HTML soubor 
obsahující tabulku 10 ⨉ 10 s náhodnými čísly. 
Rozšíření: pohrajte si s CSS a zaručte, že obsahující 
číslo dělitelné 10 budou podbarveny kontrastní barvou.
"""
"""

import random

seznam = []
vystup = "<table cellspacing=0 cellpadding = 10 border=25><tr>"

for i in range (1, 101):
	seznam.append(random.randint(1, 11))
	vystup +="<td>" + str(seznam [i - 1]) + "</td>" + "\n"
	if (i % 10 == 0) and (i != 100):
		vystup +="</tr>" + "\n" "<tr>"

vystup +="</tr></table>"
print(vystup)

f = open("nahoda.html", "w")
f.write(vystup)
f.closed
#print(seznam)
#print("počet prvkov: ", len(seznam))

"""
import random

seznam = []
vystup = "<table cellspacing=0 cellpadding = 10 border=1><tr>"

for i in range (1, 101):
	cislo = random.randint(1, 10)
	seznam.append(cislo)
	vystup += "<td width=100"
	if (cislo % 2 == 0):
		vystup += " bgcolor=red"
	vystup +=">" + str(cislo) + "</td>" + "\n"
	if (i % 10 == 0) and (i != 100):
		vystup +="</tr>" + "\n" "<tr>"

vystup +="</tr></table>"
print(vystup)

f = open("nahoda.html", "w")
f.write(vystup)
f.closed