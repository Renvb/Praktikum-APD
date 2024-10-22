import os
import functions as func

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
    func.showmenu()
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
        while True:
            os.system('cls || clear')
            print("="*50)
            print("Register user baru".center(50))
            print("="*50)
            username = input("Masukkan username: ").strip()
            password = input("Masukkan password: ").strip()
            if username == "" or password == "":
                print("\nUsername dan password tidak boleh kosong!")
                input("\nKlik enter untuk melanjutkan...")
            elif username in users:
                print("\nUsername sudah ada, tidak dapat register!")
                input("\nKlik enter untuk melanjutkan...")
            else:
                users[username] = { 'username' : username, 'password' : password, 'level' : 'user'}
                print("\nBerhasil register!")
                break
        input("\nKlik enter untuk melanjutkan...")

    elif pilihan == "3":
        break
    else:
        print("\nPilihan tidak tersedia!")
        input("\nKlik enter untuk melanjutkan...")

if level == "admin" and isLogin == True:
    while level == "admin" and isLogin == True:
        os.system('cls || clear')
        func.showmenu("admin")
        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            os.system('cls || clear')
            func.showdata(data)
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "2":
            os.system('cls || clear')
            func.showdata(data)
            func.createdata(data)
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "3":
            os.system('cls || clear')
            func.showdata(data)
            func.editdata(data)
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "4":
            os.system('cls || clear')
            func.showdata(data)
            func.deletedata(data)
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "5":
            break
        else:
            print("\nPilihan tidak tersedia!")
            input("\nKlik enter untuk melanjutkan...")

if level == "user" and isLogin == True:
    while level == "user" and isLogin == True:
        os.system('cls || clear')
        func.showmenu("user")
        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            os.system('cls || clear')
            func.showdata(data)
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
