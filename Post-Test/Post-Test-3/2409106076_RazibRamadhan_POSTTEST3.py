beratMg = float(input("Masukkan berat badan (mg): "))
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