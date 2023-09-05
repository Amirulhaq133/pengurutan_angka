bilangan = []
x = int(input("berapa banyak angka yang ingin anda masukan:  "))
for i in range (x) :
    angka = int (input("masukan angka: "))
    bilangan.append(angka)
print ("Angka sebelum diurutkan: ",bilangan)
bilangan.sort()
print("angka sesudah diururtkan", bilangan)