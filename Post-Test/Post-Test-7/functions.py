def showmenu(level=" "):
    print("="*50)
    print("Selamat datang di program Biodata Agent Valorant!".center(50))
    print("Silahkan pilih menu di bawah ini".center(50))
    print("="*50)
    if level == "admin":
        print("[1] Lihat data agent")
        print("[2] Tambah data agent")
        print("[3] Edit data agent")
        print("[4] Hapus data agent")
        print("[5] Keluar Program")
    elif level == "user":
        print("[1] Lihat data agent")
        print("[2] Keluar Program")
    else:
        print("[1] Login")
        print("[2] Register")
        print("[3] Keluar Program")



# def showdata(data):
#     print("="*50)
#     print("Daftar data agent".center(50))
#     print("="*50)
#     print("-"*50)
#     for num, (value) in enumerate(data.values()):
#         print(f'Agent ke-{num+1}')
#         print(f'Nama Agent: {value["Agent"]}')
#         print(f'Role: {value["Role"]}')
#         print(f'Asal: {value["Asal"]}')
#         print("-"*50)

def showdata(data, index=0):
    if index == 0:
        print("="*50)
        print("Daftar data agent".center(50))
        print("="*50)
        print("-"*50)
    
    if index == len(data):
        return
    
    key = list(data.keys())[index]
    value = data[key]
    
    print(f'Agent ke-{index+1}')
    print(f'Nama Agent: {value["Agent"]}')
    print(f'Role: {value["Role"]}')
    print(f'Asal: {value["Asal"]}')
    print("-"*50)

    showdata(data, index + 1)


def createdata(data):
    while True:
        name = input("\nMasukkan nama agent yang ingin ditambahkan: ").strip().capitalize()
        if name in data:
            print("Data agent sudah ada, tidak bisa ditambahkan!")
        else:
            role = input("Masukkan role: ").strip().capitalize()
            asal = input("Masukkan asal: ").strip().capitalize()
            if name == "" or role == "" or asal == "":
                print("\nData tidak boleh ada yang kosong!")
            else:
                data[name] = { 'Agent' : name, 'Role' : role, 'Asal' : asal}
                print("Data agent telah ditambahkan!")
                return data
            
def editdata(data):
    while True:
        key = input("\nMasukkan nama agent yang ingin diedit: ").strip().capitalize()
        if key in data:
            while True:
                name = input("Masukkan nama agent yang baru: ").strip().capitalize()
                role = input("Masukkan role yang baru: ").strip().capitalize()
                asal = input("Masukkan asal yang baru: ").strip().capitalize()
                if name == "" or role == "" or asal == "":
                    print("\nData tidak boleh ada yang kosong!")
                else:
                    data[key] = { 'Agent' : name, 'Role' : role, 'Asal' : asal}
                    data[name] = data.pop(key)
                    print("\nData agent telah diubah!")
                    return data
        else:
            print("Data agent tidak ditemukan!")

def deletedata(data):
    while True:
        key = input("\nMasukkan nama agent yang ingin dihapus: ").strip().capitalize()
        if key in data:
            del data[key]
            print("Data agent telah dihapus!")
            return data
        else:
            print("Data agent tidak ditemukan!")