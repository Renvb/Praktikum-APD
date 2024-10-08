import os

os.system('cls || clear')

data = [['Brimstone', 'Controller', 'USA'], ['Viper', 'Controller', 'USA'], ['Omen', 'Controller', 'Unknown']]
users = [['admin', 'admin123', 'admin'], ['user', 'user123', 'user'], ['a', 'a', 'admin'], ['u', 'u', 'user']]
isLogin = False
level = " "
kesempatan = 3

while isLogin == False and kesempatan > 0:
    os.system('cls || clear')
    print("="*50)
    print("Selamat datang di program Biodata Agent Valorant!".center(50))
    print("Silahkan pilih menu di bawah ini".center(50))
    print("="*50)
    print("[1] Login")
    print("[2] Register")
    print("[3] Keluar Program")
    pilihan = input("\nMasukkan pilihan: ")

    if pilihan == "1":
        while kesempatan > 0:
            os.system('cls || clear')
            print("="*50)
            print("Login".center(50))
            print("="*50)
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            for i in range(len(users)):
                if username == users[i][0] and password == users[i][1]:
                    isLogin = True
                    level = users[i][2]
                    break
            if isLogin == True:
                print("\nBerhasil login!")
                input("\nKlik enter untuk melanjutkan...")
                break
            else:
                print("\nUsername atau password salah!")
                kesempatan -= 1
                print(f"\nKesempatan login tersisa {kesempatan} kali lagi!")
                input("\nKlik enter untuk melanjutkan...")

    elif pilihan == "2":
        os.system('cls || clear')
        print("="*50)
        print("Register user baru".center(50))
        print("="*50)
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        users.append([username, password, 'user'])
        print("\nBerhasil register!")
        input("\nKlik enter untuk melanjutkan...")

    elif pilihan == "3":
        break
    else:
        print("\nPilihan tidak tersedia!")
        input("\nKlik enter untuk melanjutkan...")

if level == "admin" and isLogin == True:
    while level == "admin" and isLogin == True:
        os.system('cls || clear')
        print("="*50)
        print("Selamat datang di program Biodata Agent Valorant!".center(50))
        print("Silahkan pilih menu di bawah ini".center(50))
        print("="*50)
        print("[1] Lihat data agent")
        print("[2] Tambah data agent")
        print("[3] Edit data agent")
        print("[4] Hapus data agent")
        print("[5] Keluar Program")
        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            os.system('cls || clear')
            print("="*50)
            print("Daftar data agent".center(50))
            print("="*50)
            print("-"*50)
            for i in data:
                print(f'Agent ke-{data.index(i)+1}')
                print(f'Nama Agent: {i[0]}')
                print(f'Role: {i[1]}')
                print(f'Asal: {i[2]}')
                print("-"*50)
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "2":
            os.system('cls || clear')
            print("="*50)
            print("Tambah data agent".center(50))
            print("="*50)
            data.append([input("Masukkan nama agent: "), input("Masukkan role: "), input("Masukkan asal: ")])
            print("Data agent telah ditambahkan!")
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "3":
            os.system('cls || clear')
            print("="*50)
            print("Edit data agent".center(50))
            print("="*50)
            value = input("Masukkan nama agent yang ingin diubah: ")
            index = next((i for i, sublist in enumerate(data) if sublist[0] == value), -1)
            if index != -1:
                data[index] = [input("Masukkan nama agent yang baru: "), input("Masukkan role yang baru: "), input("Masukkan asal yang baru: ")]
                print("Data agent telah diubah!")
            else:
                print("Data agent tidak ditemukan!")
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "4":
            os.system('cls || clear')
            print("="*50)
            print("Hapus data agent".center(50))
            print("="*50)
            value = input("Masukkan nama agent yang ingin dihapus: ")
            index = next((i for i, sublist in enumerate(data) if sublist[0] == value), -1)
            if index != -1:
                del data[index]
                print("Data agent telah dihapus!")
            else:
                print("Data agent tidak ditemukan!")
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "5":
            break
        else:
            print("\nPilihan tidak tersedia!")
            input("\nKlik enter untuk melanjutkan...")

if level == "user" and isLogin == True:
    while level == "user" and isLogin == True:
        os.system('cls || clear')
        print("="*50)
        print("Selamat datang di program Biodata Agent Valorant!".center(50))
        print("Silahkan pilih menu di bawah ini".center(50))
        print("="*50)
        print("[1] Lihat data agent")
        print("[2] Keluar Program")
        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            os.system('cls || clear')
            print("="*50)
            print("Daftar data agent".center(50))
            print("="*50)
            print("-"*50)
            for i in data:
                print(f'Agent ke-{data.index(i)+1}')
                print(f'Nama Agent: {i[0]}')
                print(f'Role: {i[1]}')
                print(f'Asal: {i[2]}')
                print("-"*50)
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "2":
            break
        else:
            print("\nPilihan tidak tersedia!")
            input("\nKlik enter untuk melanjutkan...")

if kesempatan == 0:
    os.system("cls || clear")
    print("Kesempatan login sudah habis! Keluar dari program!")
    input("\nKlik enter untuk keluar...")

os.system('cls || clear')
print("="*50)
print("Program Selesai!".center(50))
print("="*50)
