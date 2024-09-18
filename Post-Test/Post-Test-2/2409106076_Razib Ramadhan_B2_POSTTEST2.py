barang = input("Masukkan nama barang: ")
harga = float(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))
diskon = float(76)

print("Diskon dalam persen:", diskon)

totalSebelumDiskon = jumlah * harga
totalDiskon = (diskon / 100) * totalSebelumDiskon
totalBayar = totalSebelumDiskon - totalDiskon
sisaBagi = int(diskon) % 3

print(f"\nAnda membeli {jumlah} {barang} dengan harga satuan {int(harga)}, "
    f"total sebelum diskon adalah {int(totalSebelumDiskon)}, "
    f"total diskon adalah {int(totalDiskon)}, "
    f"dan total yang harus dibayar adalah {int(totalBayar)}.")
print(f"{int(diskon)} dibagi dengan 3 sisanya {sisaBagi}.")