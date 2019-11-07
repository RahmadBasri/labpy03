#MENENTUKAN BILANGAN TERBESAR
#0 UNTUK BERHENTI

MAXIMUM = 0
B = 1
while B !=0:

    B = int(input("Masukkan bilangan = "))
    if B > MAXIMUM:
         MAXIMUM = B
    if B == 0:
        break
print("Bilangan terbesar adalah:", MAXIMUM)
