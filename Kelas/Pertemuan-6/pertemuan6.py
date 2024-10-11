# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}

# daftar_buku["novel 1"] = "Senyum pertama di pagi hari Airin"
# daftar_buku[1] = "Matahari"
# print(daftar_buku)


# daftar_buku = dict(Buku1 = "Harry Potter", Buku2 = "Percy Jackson", Buku3 = "Twillight")
# print(daftar_buku)

# print(daftar_buku["Buku2"])
# print(daftar_buku.get("Buku2"))

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# for i in Nilai:
#     print(i)

# for i, j in Nilai.items():
    # print(f"Nilai dari {i} itu valuenya adalah: {j}")

# Nilai["Struktur Data"] = 90
# Nilai.update({"Struktur Data" : 90})
# print(Nilai)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# cache = Nilai.pop("B. Indonesia")
# print(Nilai)
# print(cache)

# del Nilai["B. Inggris"]
# print(Nilai)

# Nilai.clear()
# print(Nilai)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# print(len(Nilai))

# daftar_nilai = Nilai.copy()
# print(daftar_nilai)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# nilai = {"Matematika" : 90, "Fisika" : 80, "Biologi" : 80, "Kimia" : 70}
# total = 0
# ratarata = 0
# for i in nilai.values():
#     total += i
# print(total)

# ratarata = total / len(nilai)
# print(ratarata)

