kendaraan = ["namakendaraan","jeniskendaraan","cckendaraan","warnakendaraan","rodakendaraan"]
kendaraan.append ("hargakendaraan")
kendaraan.append ("tipekendaraan")
kendaraan.insert (2, "merekkendaraan")
print(kendaraan)


menghitung = input ("anda ingin menghitung luas bangun datar apa?")
match menghitung:
    case "1":
        sisi=int(input("masukan nilai sisi"))
        luas=sisi*sisi
        print(luas)
    case "2":
        jari_jari= int(input("masukan nilai jari jari"))
        luas=3.14*jari_jari*jari_jari
        print(luas)
    case "3":
        alas= int(input("masukan nilai alas"))
        tinggi= int(input("masukan nilai tinggi"))
        luas=0.5*alas*tinggi
        print(luas)
    case _:
        print("pilihan tidak tersedia")
      

    

