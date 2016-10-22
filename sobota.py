print('Hello, Django girls!')
if not 3>2:
	print("to dziala!")
else:
	print("nie")

def hej(name):
	if name=="kasia":
		print("hej kasia")
	elif name=="ania":
		print("hej ania")
	else:
		print("nieznajoma")

def hej(imie):
	print("hej "+ imie+"!")
dziewczyny=["ania", "kasia", "ula", "magda"]
for imie in dziewczyny:
	hej(imie)
	print("kolejna dziewczyna")
