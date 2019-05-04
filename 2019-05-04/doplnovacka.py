"""
doplnovacka.py 
Moje kamarádka učí soukromě němčinu. Potřebuje pro klienty 
připravit texty, které se časem naučí nazpaměň (jedná se o
právní předpisy). Proto jim připravuje stále stejný text,
ve kterém vynechá nejprve každé 5. slovo, později každé 4.
slovo atd., až se text naučí zpaměti. Výstupem bude nový soubor.
Pracujte se souborem lorem.py.
Vytvořte pro ni program, jehož vstupem bude textový soubor 
a informace, kolikátý znak se má zaměnit.
"""

with open("song.txt") as f:
	text = f.read()
f.closed
#print(text)

text = text.replace("\n", "# ")

seznam = []
seznam = text.split(" ")
#print(seznam)
vysledok = []
interpunkcia = ".,?!-\""

for i in range(0, len(seznam)):
	slovo = seznam[i]
	slovoUpravene = ""
	if((i + 1) % 5 == 0):
		for pismeno in slovo:
			if pismeno not in interpunkcia:
				slovoUpravene += "*"
			else:
				slovoUpravene += pismeno

		vysledok.append(slovoUpravene)
	else:
		vysledok.append(slovo)
s = " ".join(vysledok)
s = s.replace("#", "\n")
print(s)