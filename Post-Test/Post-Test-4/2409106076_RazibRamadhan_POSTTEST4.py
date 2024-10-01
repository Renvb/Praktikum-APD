username = "Razib"
password = "76"
gagal = 0
login = False

print("Selamat datang di program kalkulator BMI")
print("Silahkan login untuk melanjutkan\n")

while gagal < 3:
    inputUsername = input("Masukkan username: ")
    inputPassword = input("Masukkan password: ")
    if inputUsername == username and inputPassword == password:
        print("Login Berhasil!")
        if gagal > 0:
            print(f"Login gagal sebanyak {gagal} kali")
        login = True
        gagal = 0
        break
    else:
        print("Username atau password salah\n")
        gagal += 1

    if gagal == 3:
        print("Anda telah gagal login sebanyak 3 kali, program ini akan ditutup")
        break
    
while login == True:
    beratMg = float(input(" \nMasukkan berat badan (mg): "))
    tinggiKm = float(input("Masukkan tinggi badan (km): "))


    beratKg = beratMg / 1000000
    tinggiMeter = tinggiKm * 1000
    tinggiCm = tinggiKm * 100000

    bmi = beratKg / (tinggiMeter ** 2)

    if bmi < 18.5:
        kategori = "Berat Badan Kurang (Underweight)"
    elif bmi < 24.9:
        kategori = "Berat Badan Normal"
    elif bmi < 29.9:
        kategori = "Berat Badan Berlebih (Overweight)"
    else:
        kategori = "Obesitas"

    print(f"""\nBerat Anda: {beratKg} kg
Tinggi Anda: {tinggiCm} cm
BMI Anda adalah {bmi:.2f} dan Anda termasuk: {kategori}""")
    lanjut = input("\nApakah anda ingin keluar dari program ini? (ya/tidak) ")
    if lanjut == "ya":
        print("Terima kasih!")
        break
    elif lanjut == "tidak":
        continue
    else:
        print("Input tidak valid, program ini akan ditutup")
        break

