# def aku_fungsi():
#     print("Hello World")

# aku_fungsi()

# def tambah(a, b):
#     hasil = a + b
#     print(hasil)

# tambah(10, 2)

# def tambah(a, b):
#     hasil = a + b
#     return hasil

# tambahan = tambah(2, 4) + tambah(4, 6)
# print(tambahan)

# def pilihan(opsi):
#     match opsi:
#         case "1":
#             print(1)
#             return
#         case "2":
#             print(2)
#             return

#     print(3)

# pilihan(2)

# def cetak(nama, nim, *matkul):
#     print(nama, nim, list(matkul))

# cetak("Fathir", 41, "Kalkulus", "Fisika Dasar")

# var = 2,4,5
# var1, var2, var3 = var

# print(var)
# print(var1, var2, var3)

# membuat variabel global
Nama = "Informatika"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# membuat variabel lokal
def info():
    Nama = "Teknik Elektro"
    Mata_Kuliah = "Pengantar Teknik ELektro"
# mengakses variabel lokal
    print("Prodi:", Nama)
    print("Mata Kuliah:", Mata_Kuliah)
# memanggil fungsi info
info()
# mengakses variabel global
print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)