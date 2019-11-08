#KEUNTUNGAN SELAMA 8 BULAN
sum=0
MODAL=100000000
R=0
LABA = [int(0), int(0), int(MODAL)*.1, int(MODAL)*.1, int(MODAL)*.5, int(MODAL)*.5, int(MODAL)*.5, int(MODAL)*.2]

for i in LABA:
    sum = sum+i
    R+=1

    print("LABA BULAN KE ",R,"  sebesar ",i,)
print("TOTAL LABA 8 BULAN SEBESAR: ",sum)
