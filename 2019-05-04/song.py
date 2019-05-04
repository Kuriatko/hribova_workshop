"""
song.py 
Načti si data ze souboru „song.txt“.
Data si rozděl po odstavcích (zalomení řádku „\n“) a vypiš je spolu s číslem řádku.
O jakou písničku se jedná?
"""


with open("song.txt") as f:
	read_data = f.read()
f.closed

print(read_data)

"""
ako data rozparsovat podla enteru
a kam ich potom ulozit (budeme chciet cislvoat riadky)
"""
"""
radky = []
radky = read_data.split('\n')
print(radky)

for i in range(0, len(radky)):
	print(i, radky[i])
"""

radky = []
radky = read_data.split('\n')
vystup = ""

for i in range(0, len(radky)):
	vystup = vystup + str (i + 1) + "\t" + radky[i] + "\n"

f = open("song2.txt", "w")
f.write(vystup)
f.closed

