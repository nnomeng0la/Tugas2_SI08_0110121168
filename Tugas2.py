from os import read, system
from time import sleep
import random, string
def clear():
    ### Fungsi untuk menghapus (Clear), ketika sebuah menu/fitur selesai dilakukan atau ketika memilih pilihan yang tidak ada di dalam menu ###
    print("Enter back to MENU")
    a = input()
    _ = system('cls')
def menu():
    ### Fungsi untuk menampilkan menu awal NF LIBRARY ###
    print(
    """***** SELAMAT DATANG DI NF LIBRARY *****
    MENU:
    [1] Tambah Anggota Baru
    [2] Tambah Buku Baru
    [3] Pinjam Buku
    [4] Kembalikan Buku
    [5] Lihat Data Peminjaman
    [6] Lihat Data Anggota
    [7] Lihat Data Buku
    [8] Keluar""")
    
def Pendaftaran_Anggota_Baru(Kode, Nama, Tipe_Keanggotaan): ### Fungsi untuk penadftaran anggota ###
    myfile = open("anggota.txt", 'a+')
    myfile.write(Kode +","+Nama+","+Tipe_Keanggotaan+"\n") ### Menambahkan inputan Kode, Nama, dan Tipe Keanggotaan ke dalam file anggota.txt ###
    myfile.close()

def Penambahan_Buku(kode,judul,penulis, stok): ### Hampir sama dengan Fungsi Pendaftaran Anggota ###
    myfile = open("buku.txt", 'a+')
    myfile.write(kode +","+judul+","+penulis+","+stok+"\n") ### Menambahkan inputan kode, judul, penulis, dan stok ke dalam file buku.txt ###
    myfile.close()

def readBuku(): ### Fungsi untuk membaca data buku yang tersedia ###
    dataBuku = [] ### Inisialisasi variabel untuk menampung isi dari buku.txt ###
    f = open('buku.txt')
    for each_line in f: ### Strip() digunakan untuk menghilangkan "\n" (newline) ###
        dataBuku.append(each_line.strip()) ### Menambahkan (append) data di dalam buku.txt ke dalam variabel dataBuku ###
    f.close()
    return dataBuku ### Mengembalikan Variabel dataBuku ###

def readAnggota(): ### Hampir sama dengan Fungsi readBuku ###
    dataAnggota = []
    f = open('anggota.txt')
    for each_line in f:
        dataAnggota.append(each_line.strip())
    f.close()
    return dataAnggota

def cek_buku(kd_buku): ### Fungsi untuk memeriksa apakah kode buku yang dimasukkan sudah benar/belum ###
    for i in readBuku(): ### Memanggil data buku terlebihdahulu ###
        if i[:6] == kd_buku: ### Membandingkan 6 karakter pertama(kode buku) dengan kode buku yang dimasukkan ###
            return True
    return False

def cek_bukuP(kd_buku): ### Fungsi untuk memeriksa apakah kode buku yang dimasukkan sudah benar/belum ###
    for i in readPinjamBuku(): ### Memanggil data buku terlebihdahulu ###
        if i[:6] == kd_buku: ### Membandingkan 6 karakter pertama(kode buku) dengan kode buku yang dimasukkan ###
            return True
    return False
def cek_anggota(kd_anggota): ### Hampir sama dengan fungsi cek buku ###
    for i in readAnggota():
        if i[:6] == kd_anggota:
            return True
    return False

def cek_stok(kd_buku): ### Fungsi untuk menmeriksa stok buku ###
    dataBuku = readBuku()
    for i in range (len(dataBuku)):
        if dataBuku [i][:6] == kd_buku:
            dataBuku[i] = dataBuku[i].split(",") ### Mengubah string menjadi list ###
            if int(dataBuku[i][-1]) > 0: ### mengubah string di index -1(terakhir) menjadi integer untuk dibandingkan dengan angka nol (0) ###
                return True
    return False

def kurangStok(kd_buku): ### Fungsi untuk mengurangi stok buku ###
    dataBuku = readBuku()
    for i in range(len(dataBuku)): ### Ini adalah perulangan ###
        if dataBuku[i][:6] == kd_buku: ### Mengecek buku ada atau tidak di dalam variabel dataBuku yang isinya adalah file buku.txt ###
            dataBuku[i] = dataBuku[i].split(",") ### Ini untuk mengubah jadi list ###
            dataBuku[i][-1] = str(int(dataBuku[i][-1]) - 1) ### List diubah menjadi string kemudian diubah menjadi integer kemudian baru dikurang ###
            dataBuku[i] = ",".join(dataBuku[i]) ### Mengembalikan menjadi string ### 
    myfile = open('buku.txt', 'w+')
    for i in dataBuku:
        myfile.write(i+"\n") ### Menulis ulang data yang ada di dalam file ###
    myfile.close()
def tambahStok(kd_buku): ### Hampir sama dengan Fungsi kurangStok ###
    dataBuku = readBuku()
    for i in range(len(dataBuku)): #Ini adalah perulangan 
        if dataBuku[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
            dataBuku[i] = dataBuku[i].split(",") #Ini untuk mengubah jadi list (ngambil stok)
            dataBuku[i][-1] = str(int(dataBuku[i][-1]) + 1)# Ngubah stok 
            dataBuku[i] = ",".join(dataBuku[i])#Ngembaliin menjadi str
    myfile = open('buku.txt', 'w+')
    for i in dataBuku:
        myfile.write(i+"\n")
    myfile.close()

def readPinjamBuku(): ### Hampir sama dengan Fungsi readBuku ###
    a_list = []
    myfile = open("peminjaman.txt")
    for line in myfile:
        a_list.append(line.strip())
    return a_list

def Peminjaman_Buku(kd_buku,kd_anggota): ### Fungsi untuk melakukan peminjaman buku ###
    dataPinjam = readPinjamBuku() ### Membaca buku yang tersedia ###
    ada = 0 ### Inisialisasi jika jika buku sudah dipinjam atau belum dipinjam ###
    for i in range(len(dataPinjam)): ### Ini adalah perulangan ###
        if dataPinjam[i][:6] == kd_buku: ### Jika buku telah dipinjam, maka hanya ditambah kode anggota dibaris tersebut ###
            dataPinjam[i] = dataPinjam[i]+","+kd_anggota
            ada = 1
    if ada == 1: ### Jika buku yang sama sudah ada yang meminjam dan belum dikembalikkan, maka variabel ada nilainya = 1 ###
        f = open('peminjaman.txt',"w+") ### Memperbaharui data dalam file peminjaman.txt ###
        for i in dataPinjam:
            f.write(i+"\n")
        f.close()
    else:
        f = open('peminjaman.txt',"a+") ### Menambah data baru ke dalam file peminjaman.txt, jika buku tersebut belum pernah dipinjam sebelumnya ###
        f.write(kd_buku+","+kd_anggota+"\n")
        f.close()

def cek_statusAngggota(kd_anggota): ### Fungsi untuk memeriksa apakah orang tersebut adalah anggota Karyawan NF Group atau bukan ###
    dataAnggota = readAnggota() ### Memasukkan isi dari file anggota.txt ke dalam variabel dataAnggota ###
    for i in range(len(dataAnggota)):
        if dataAnggota[i][:6] == kd_anggota:
            if dataAnggota[i][-1] == "1": ### Jika Tipe Keanggotaaan(index terakhir dalam baris dataAnggota) = 1 berarti dia adalah anggota ###
                return True
            else:
                return False
def anggota_pinjam(kd_buku,kd_anggota): ### Fungsi untuk mengetahui anggota yang meminjam buku ###
    dataPinjam = readPinjamBuku()
    for i in range(len(dataPinjam)):
        if dataPinjam[i][:6] == kd_buku:
            dataPinjam[i] = dataPinjam[i].split(",") ### Ini untuk mengubah jadi list ### 
            if dataPinjam[i].count(kd_anggota) == 1: ### Jika buku hanya dipinjam oleh satu orang makan fungsi akan mengembalikan True ###  
                return True
            else:
                return False
    
def remove_anggota(kd_buku,kd_anggota):
    dataPinjam = readPinjamBuku() ### Membaca data peminjamana atau bisa dikatakan memasukkan data di file peminjamaman.txt ke dalam variabel data pinjam ### 
    for i in range(len(dataPinjam)):
        if dataPinjam[i][:6] == kd_buku: ### Mengecek buku ada atau tidak di dalam file ###
            dataPinjam[i] = dataPinjam[i].split(",") ### Ini untuk mengubah jadi list  ###
            dataPinjam[i].remove(kd_anggota)
            if len(dataPinjam[i]) == 1 : ### Jika panjang dataPinjam pada index [i] hanya satu maka data maka baris tersebut akan dihapus ### 
                del dataPinjam[i]
            else:
                dataPinjam[i] = ",".join(dataPinjam[i]) ### Mengembalikan menjadi String ###
        
    myfile = open('peminjaman.txt', 'w+') ### Menulis ulang data pada file peminjaman.txt ###
    for i in dataPinjam:
        myfile.write(i+"\n") ### variabel i isinya adalah data yang ada di dataPinjam, sedangkan dataPinjam isinya adalah readPinjamBuku() yang sudah diperbaharui ###
    myfile.close()

def viewPinjam(): ### Fungsi untuk menampilkan/melihat siapa saja yang meminjam buku 
    ### Memasukkan data file-file ke dalam variabel ###
    dataPinjam  = readPinjamBuku() 
    dataBuku    = readBuku()
    dataAnggota = readAnggota()
    ### Deklarasi dict kosong ###
    dataBukuD    = {} 
    dataAnggotaD = {}
    
    for i in range(len(dataBuku)):
        dataBuku[i] = dataBuku[i].split(",") ### Mengubah jadi list setiap barisnya ### 
        dataBukuD[dataBuku[i][0]] = dataBuku[i][1:]

    for i in range(len(dataAnggota)):
        dataAnggota[i] = dataAnggota[i].split(",") ### Mengubah jadi list setiap barisnya ###
        dataAnggotaD[dataAnggota[i][0]] = dataAnggota[i][1:]

    for i in range(len(dataPinjam)):
        dataPinjam[i] = dataPinjam[i].split(",") ### Mengubah jadi list setiap barisnya ###
    if dataPinjam != []: ### Jika dataPinjamnya tidak kosong maka akan menampilkan: ###
            
        print("\n*** DAFTAR PEMINJAMAN BUKU ***\n")

        for i in range(len(dataPinjam)):
            print("Judul: "+dataBukuD[dataPinjam[i][0]][0])
            print("Penulis: "+dataBukuD[dataPinjam[i][0]][1])
            for j in range(len(dataPinjam[i][1:])):
                if dataAnggotaD[dataPinjam[i][j+1]][1] == "1": ### Jika yang meminjam adalah anggota NF Group di ujungnya doberi simbol bintang (*) ### 
                    print(str(j+1)+". "+dataAnggotaD[dataPinjam[i][j+1]][0]+"(*)")            
                else:
                    print(str(j+1)+". "+dataAnggotaD[dataPinjam[i][j+1]][0])            
            print()
    else: ### Jika file peminjman.txt kosong ###
        print("Tidak ada buku yang sedang dipinjam.")
    
def viewAnggota(): ### Fungsi untuk menampilkan/melihat daftar anggota ###
    dataAnggota = readAnggota()
    if dataAnggota != []:
        print("**** DAFTAR ANGGOTA ****\n")
        for i in range(len(dataAnggota)):
            dataAnggota[i] = dataAnggota[i].split(",") ### Mengubah jadi list ###
            print("Kode Anggota "+ dataAnggota[i][0]) 
            print("Nama Anggota : "+dataAnggota[i][1])
            print("Status Anggota : NF Group" if dataAnggota[i][2] == "1" else "Status Anggota : Masyarakat Umum")
            print()
    else:
        print("Tidak ada Anggota yang terdaftar")
def viewBuku(): ### Fungsi untuk menampilkan/melihat daftar buku ###
    dataBuku = readBuku()
    if dataBuku != [] :
        print("**** DAFTAR BUKU ****\n")
        for i in range(len(dataBuku)):
            dataBuku[i] = dataBuku[i].split(",")
            print("Kode Buku "+ dataBuku[i][0])
            print("Judul Buku : "+dataBuku[i][1])
            print("Penulis Buju : "+dataBuku[i][2])
            print("Stok Buku : "+dataBuku[i][3])
            print()
    else:
        print("Tidak ada Buku yang tersedia")



menu()

while True:
    pilih = input("Masukkan menu pilihan Anda: ")
    ### Fitur 1: Pendaftaran Anggota Baru ###
    if pilih == "1":
        print("\n*** PENDAFTARAN ANGGOTA BARU ***")
        Kode = "LIB" + ''.join(random.choice(string.digits) for _ in range(3))
        Nama = input("Masukkan nama: ")
        Tipe_Keanggotaan = input("Apakah merupakan karyawan NF Group? (Y/T): ")
        if Tipe_Keanggotaan == "Y" :
            Tipe_Keanggotaan = "1"
            Pendaftaran_Anggota_Baru(Kode,Nama,Tipe_Keanggotaan)
            print("Pendaftaran anggota dengan kode "+Kode+" atas nama "+Nama+" berhasil.")
        elif Tipe_Keanggotaan == "T":
            Tipe_Keanggotaan = "2"
            Pendaftaran_Anggota_Baru(Kode,Nama,Tipe_Keanggotaan)
            print("Pendaftaran anggota dengan kode "+Kode+" atas nama "+Nama+" berhasil.")
        ### 1 adalah karyawan NF Group sedangkan 2 bukan karyawan NF Group ###
        else:
            print("Pilihan Salah, silakan ulangi")
    ### Fitur 2: Penambahan Buku ###
    elif pilih == "2":
        print("\n*** PENAMBAHAN BUKU BARU ***")
        judul = input("Judul: ")
        penulis = input("Penulis: ")
        stok = input("Stok: ")
        penulis = penulis.split() ### Mengubah nama penulis yang awalnya string menjadi list ###
        penulis = "".join(penulis) ### Mengembalikan list ke dalam string, dan menghilangkan spasi ###
        kode = penulis[:3].upper() + ''.join(random.choice(string.digits) for _ in range(3)) ### Menambahkan 3 huruf pertama nama penulis ke dalam kode dan mengubahnya menjadi huruf kapital ###
        Penambahan_Buku(kode,judul, penulis, stok)
        print("Penambahan buku baru dengan kode "+kode+" dan judul "+judul+" berhasil.")

    ### Fitur 3: Peminjaman Buku ###
    elif pilih == "3":
        print("\n*** PEMINJAMAN BUKU ***")
        kd_buku = input("Kode buku: ")
        if cek_buku(kd_buku):
            if cek_stok(kd_buku):
                kd_anggota = input("Kode anggota: ")
                if cek_anggota(kd_anggota):
                    Peminjaman_Buku(kd_buku,kd_anggota)
                    kurangStok(kd_buku)
                    print("Peminjaman buku "+kd_buku+" oleh "+kd_anggota+" berhasil.")
                else:
                    print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
            else:
                print("Stok buku kosong. Peminjaman gagal.")
        else:
            print("Kode buku tidak ditemukan. Peminjaman gagal.\n")

    ### Fitur 4: Pengembalian Buku ###
    elif pilih == "4":
        print("\n*** PENGEMBALIAN BUKU ***")
        kd_buku = input("Kode buku: ")
        if cek_bukuP(kd_buku):
            kd_anggota = input("Kode anggota: ")
            if anggota_pinjam(kd_buku,kd_anggota):
                tambahStok(kd_buku)
                terlambat = int(input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat): "))
                if cek_statusAngggota(kd_anggota): 
                    denda = 1000 * terlambat ### Jika Karyawan NF Group maka besar dendanya 1000/hari ###
                else:
                    denda = 2500 * terlambat ### Jika bukan maka 2500/hari ###
                print("Total denda = Rp.",denda)
                print("Silakan membayar denda keterlambatan di kasir.")
                remove_anggota(kd_buku,kd_anggota)
                print("Pengembalian buku "+kd_buku+" oleh "+kd_anggota+" berhasil.")

            else:
                print("Kode anggota tidak terdaftar sebagai peminjam buku tersebut. Pengembalian buku gagal.\n")
        else:
            print("Kode buku salah. Pengembalian buku gagal.")
    ### Fitur 5: Lihat Data Peminjaman ###
    elif pilih == "5":
        viewPinjam()
    ### Fitur Bonus 1/Menu 6: Lihat Data Anggota yang Terdaftar ###
    elif pilih == "6":
        viewAnggota()
    ### Fitur Bonus 2/Menu 7: Lihat Data Buku yang Tersedia ### 
    elif pilih == "7":
        viewBuku()
    ### Menu 8: Untuk Mengakhiri/Keluar dari Program ###
    elif pilih == "8":
        print("Terima kasih atas kunjungan Anda...")
        break
    else:
        print("Pilihan Anda salah. Ulangi.")
    clear()
    menu()
