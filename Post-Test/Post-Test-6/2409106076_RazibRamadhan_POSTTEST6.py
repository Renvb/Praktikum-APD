import os

os.system('cls || clear')

data = { 'Brimstone' : { 'Agent' : 'Brimstone', 'Role' : 'Controller', 'Asal' : 'USA' },
        'Viper' : { 'Agent' : 'Viper', 'Role' : 'Controller', 'Asal' : 'USA' },
        'Omen' : { 'Agent' : 'Omen', 'Role' : 'Controller', 'Asal' : 'Unknown' }}

users = { 'admin' : { 'username' : 'admin', 'password' : 'admin123', 'level' : 'admin'},
        'user' : { 'username' : 'user', 'password' : 'user123', 'level' : 'user'},
        'a' : { 'username' : 'a', 'password' : 'a', 'level' : 'admin'},
        'u' : { 'username' : 'u', 'password' : 'u', 'level' : 'user'}}

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
            for i in users:
                if username == users[i]['username'] and password == users[i]['password']:
                    isLogin = True
                    level = users[i]['level']
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
        users[username] = { 'username' : username, 'password' : password, 'level' : 'user'}
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
            for num, (key, value) in enumerate(data.items()):
                print(f'Agent ke-{num+1}')
                print(f'Nama Agent: {value["Agent"]}')
                print(f'Role: {value["Role"]}')
                print(f'Asal: {value["Asal"]}')
                print("-"*50)
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "2":
            os.system('cls || clear')
            print("="*50)
            print("Tambah value agent".center(50))
            print("="*50)
            name = input("Masukkan nama agent: ")
            data[name] = { 'Agent' : name, 'Role' : input("Masukkan role: "), 'Asal' : input("Masukkan asal: ")}
            print("Data agent telah ditambahkan!")
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "3":
            os.system('cls || clear')
            print("="*50)
            print("Edit data agent".center(50))
            print("="*50)
            key = input("Masukkan nama agent yang ingin diedit: ")
            if key in data:
                name = input("Masukkan nama agent yang baru: ")
                data[key] = { 'Agent' : name, 'Role' : input("Masukkan role yang baru: "), 'Asal' : input("Masukkan asal yang baru: ")}
                data[name] = data.pop(key)
                print("Data agent telah diubah!")
            else:
                print("Data agent tidak ditemukan!")
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "4":
            os.system('cls || clear')
            print("="*50)
            print("Hapus data agent".center(50))
            print("="*50)
            key = input("Masukkan nama agent yang ingin dihapus: ")
            if key in data:
                del data[key]
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
            for num, (key, value) in enumerate(data.items()):
                print(f'Agent ke-{num+1}')
                print(f'Nama Agent: {value["Agent"]}')
                print(f'Role: {value["Role"]}')
                print(f'Asal: {value["Asal"]}')
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
