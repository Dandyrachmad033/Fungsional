from re import I, S


def save_data(data,nama_file):
    p = open(nama_file,'w+')
    p.write(str(data))
    p.close()

def load_data(nama_file):
    p = open(nama_file,'r')
    data =p.read()
    p.close()
    return eval(data)

def awal():
    print('1. Login')
    print('2. Daftar Akun')
    pilih = int(input('Pilih: '))
    if pilih ==1:
        login()
    elif pilih == 2:
        daftar()
    else:
        print('Menu tidak Ada')

def daftar():
    regis = input("Masukkan Nama: ")
    regis1 = input("Masukkan username: ")
    regis2 = input("masukkan password: ")
    username = load_data("username.txt")    
    for x in username:
        
        if regis != x['akun'] or regis1 != x['user']:
            print("Nama bisa Dirpakai")
            username.append(dict(akun = regis,user =regis1,password = regis2,history = []))
            save_data(username,"username.txt")
        else:
            print('Nama sudah Terpakai')
            daftar()
        
    awal()   
        
def userkecil(nama):
    while 1<2:
        print('selamat Datang '+ nama+' :)')
        print('1. Pinjam buku')
        print('2. Tampilkan List Buku')
        print('3. Kembalikan Buku')
        print('4. keluar')
        pilih1 = int(input('Pilih: '))
        if pilih1 == 1:
            pinjambukuuser(nama)
        elif pilih1 ==2 :
            tampilbukuuser()
        elif pilih1 == 3:
            kembalibuku()
        elif pilih1 == 4:
            login()   
            
        else:
            print('lak salah berarti crot')
            continue
        
        
        
def superuser():
    while 1<2:
        
        print('\n1. Tambah Buku')
        print('2. Tampilkan list buku') 
        print('3. Update nama buku')
        print('4. Hapus Buku')
        print('5. Anggota')
        pilih = int(input('Pilih: '))
        if pilih == 1:
            tambahbukuadmin()
        elif pilih == 2:
            tampilbukuadmin()
        elif pilih == 3:
            update_buku()
        elif pilih == 4:
            hapus_buku() 
        elif pilih == 5:
            anggota()
        else:
            print('Menu Tidak Tersedia')    
            

def login():
    print('||LOGIN||')
    masuk = input('Username: ')
    masuk1 = input('Password: ')
    user = load_data('user.txt')
    username = load_data('username.txt')
    if masuk == user['user'] and masuk1 == user['user']:
        superuser()    
        
    for x in username:
        if masuk == x['user'] and masuk1 == x['password']:
            userkecil(x['akun'])


def tambahbukuadmin():
    tambah = input('Masukkan nama buku: ')
    data = load_data('buku.txt')
    data.append(dict( judul = tambah,stok = False,status = 'Tersedia'))
    save_data(data,'buku.txt')

def tampilbukuadmin():
    print('||List Buku||')
    print('================')
    data = load_data('buku.txt')
    for x in data:       
        print('judul: '+x['judul']+'  |'+ x['status'])
        print('================')
        
def update_buku():
    data = load_data('buku.txt')
    for x in data:
        print('Judul: '+ x['judul'])
    ganti = input('Masukkan nama buku: ')
    for i in data:
        if ganti == i['judul']:
            ganti1 = input('Nama baru: ')
            i['judul'] = ganti1
            save_data(data,'buku.txt')
            break
def anggota():
    while 1<2:
        print('1. tambah anggota')
        print('2. Tampilkan list anggota')
        print('3. update nama anggota')
        print('4. hapus anggota')
        print('5. Kembali')
        pilih = int(input('pilih: '))
        if pilih == 1:
            daftar()
        elif pilih == 2:
            p =0
            data = load_data('username.txt')
            for x in data:
                p+=1
                print(str(p) +' nama: '+ x['akun'])    
        elif pilih == 3:
            data = load_data('username.txt')
            for x in data:
                print('nama: '+ x['akun'])
            ganti = input('masukkan nama yang akan diubah: ')
            for i in data:
                if ganti == i['akun']:
                    baru = input('Masukkan nama baru: ')
                    i['akun'] = baru
                    save_data(data,'username.txt')
                    break
        elif pilih == 4:
            data = load_data('username.txt')
            for x in data:
                print('nama: '+ x['akun'])
            hilang = input('Masukkan nama anggota yang akan dihapus: ')
            for i in data:
                if hilang == i['akun']:
                    data.remove(i)
                    save_data(data,'username.txt')
                    break
        elif pilih == 5:
            superuser()
        else:
            print('Menu tidak ada')    


def pinjambukuuser(nama):
    pinjam = input('Masukkan Nama Buku: ')
    data = load_data('buku.txt')
    data_user = load_data('username.txt')
    data1 = [i for i in data if i['judul'] == pinjam]
    if data1:
        for x in data:
            if x['judul'] == pinjam:
                if x['stok'] == True:
                    print('Buku Sudah Dipinjam')
                else:
                    x['status'] = 'dipinjam'
                    x['stok'] = True
                    for i in data_user:
                        if i['akun'] == nama:
                            i['history'].append(pinjam)
                    print('Buku Berhasil dipinjam') 
                    save_data(data,'buku.txt')
                    save_data(data_user,'username.txt')
                    break   
    else:
        print("Buku Tidak Ada Atau Belum Tersedia")


def tampilbukuuser():
    print('||List Buku||')
    print('================')
    data = load_data('buku.txt')
    for x in data:
                
        print('judul: '+x['judul']+'  | '+ x['status'])
    print('================')

def kembalibuku():
    kembali = input('Masukkan nama Buku: ')
    data = load_data('buku.txt')
    for x in data:
        if x['judul'] == kembali:
            x['stok'] = False
            x['status'] = 'Tersedia'
            save_data(data,'buku.txt')
            print('Buku Berhasil dikembalikan')
            
def hapus_buku():
    data = load_data('buku.txt')
    p=1
    for i in data:
        print(str(p)+' judul: '+ i['judul']+'')
        p+=1
    pilih = input('Pilih: ')
    for x in data:
        if pilih == x['judul']:
            data.remove(x)
            save_data(data,'buku.txt')
            print('buku berhasil dihapus')
            break
        
def list_sekarang():
    data = load_data('username.txt')
    for x in data:
        x
    
    
    
    
awal()
