# import os untuk clearscreen()
import os

#variable global data_tugas guna dapat diakses ke berbagai operasi.
data_tugas = ""

def tambah_tugas():
    '''Fitur untuk menambahkan tugas tugas siswa yang berisi mulai dari input yang menyetorkan validasi dan nama tugas
    , lalu berbagai method percabangan dan perulangan untuk membuat struktur kontrol yang dinamis dalam membantu siswa
    mengorganisir tugas tugas mereka yang nantinya disimpan ke variable terbuka atau global yaitu data_tugas = "" '''

    # Variable boolean guna untuk menjalankan alur kontrolnya perulangan seperti while.
    status1 = True

    # looping untuk menjalankan program tmabah tugas dengan awal pertanyaan validasi.
    while status1:

        # input validasi guna untuk mesmatikan pengguna untuk menambahkan tugas atau tidak.
        Validasi = input("\nApakah kamu ingin menambahkan tugas ini? (y/n) : ")

        #kondisi ketika 'ya'.
        if Validasi.lower() == "y":

            # method untuk clearscreen guna memastikan pengguna dapat fokus untuk menambahkan tugas.
            os.system('cls')

            # boolean untuk mengatur ketika kondisi dimana pengguna salah input.
            status2 = True

            # looping kedua untuk keitka pengguna salah input terjadi.
            while status2:

                # Tampilan Tambahkan tugas.
                print("\n=======================================")
                print("========== Tambahkan Tugas ===========")
                print("=======================================")
                
                # nama tugas pengguna
                nama = input(str("\nMasukkan nama tugas : "))
                
                #validasi tipe input tugas itu string.
                cek_string = type(nama)

                #panggil data_tugas untuk ditambahkan ketika pengguna ingin menambahkan dan akan ada di tampilka_tugas().
                global data_tugas

                #kondisi ketika input yang diberikan bukan bertipe string untuk nama.
                if not cek_string: 
                    print("\n\033[91mmasukkan nama dengan benar ya 😡😡😡!!!\033[0m")
                    # jika salah, pengguna akan disuruh untuk input kembali.
                    status = False
                    continue
                #kondisi ketika data tugas akan ditambahkan ke database agar bisa di modifikasi ke setiap operasi utama.
                else:
                    # Tambahkan status default "belum" pada setiap tugas baru.
                    data_tugas += f";{nama} | belum dikerjakan"

                # Tampilan Konfirmasi Tugas siswa.
                print("\n=======================================")
                print("========== Konfirmasi Tugas ===========")
                print("=======================================\n")

                print(f"Nama tugas          : {nama}")

                # tekan enter untuk kembali
                print("\n========================================")
                input("\n[ Tekan ENTER untuk kembali ]")

                # boolean false ketika tugas telah selesai agar bisa kembali ke halaman utama.
                status2 = False
                break
            # lalu membersihkan CLI Terminal agar kembali ke menu utama.
            os.system('cls')
            # boolean false ketika operasi tambah tugas telah terjalankan.
            status1 = False    

        # Kondisi ketika pengguna memilih batal menambahkan tugas.
        elif Validasi.lower() == "n":
            os.system('cls')
            print("Batal menambahkan tugas.\n")
            # tekan enter untuk kembali.
            print("========================================")
            input("\n[ Tekan ENTER untuk kembali ]")
            os.system('cls')
            # keluar dari program.
            break

        # Kondisi ketika pengguna memberikan input yang tidak valid selain y atau n.
        else:
            print("\033[91mJawaban tidak valid. Silakan masukkan 'y' atau 'n'.\033[0m")
            continue

def tampil_tugas():
    '''Fitur untuk menampilkan tugas-tugas siswa yang berisi pertanyaan validasi, berbagai kondisi percabangan seperti 
    if elif else, dan perulangan seperti while guna memastikan operasi tampil_tugas() dapat berjalan dinamis layaknya
    operasi tambah_tugas(), hanya berbeda fungsionalitas dalam penggunaanya, jika tambah tugas itu adalah menambahkan
    tugas yang ada lalu di simpan di'variabel global yaitu data_tugas'''

    # looping untuk menjalankan program tambah tugas dengan awal pertanyaan validasi.
    status1 = True

    # looping untuk menjalankan program tmabah tugas dengan awal pertanyaan validasi.
    while status1:

        # input validasi guna untuk mesmatikan pengguna untuk menambahkan tugas atau tidak.
        Validasi = input("\nApakah kamu ingin melihat tugas ini? (y/n) : ")

        #kondisi ketika ya
        if Validasi.lower() == "y":
            os.system('cls')
            # boolean untuk mengatur ketika kondisi dimana pengguna salah input.
            status2 = True

            # looping kedua untuk keitka pengguna salah input terjadi.
            while status2:

                # Tampilan daftar Tugas
                print("===================================")
                print("========== Daftar Tugas ===========")
                print("===================================\n")

                '''panggil data_tugas agar bisa diaskes di tampil_tugas() guna menampikan data yang tertambah 
                pada operasi tambah_tugas()'''

                global data_tugas

                #kondisi ketika tugas kosong, maka pengguna di harapkan untuk menambahkan terlebih dahulu.
                if data_tugas == "":
                    print("\nBelum ada tugas disini, silahkan untuk menambahkan 😄\n")
                    # jika belum ada tugas, pengguna bisa menambahkan tugas.
                    tambah_tugas()

                #kondisi ketika tugas sudah tertambahkan pada operasi tambah_tugas().
                else:
                    '''diperlukan pemisah ';' guna untuk spasi pada setiap nama tugas yang telah tertambah pada 
                    operasi tambah_tugas()'''
                    daftar = data_tugas.split(';')

                    '''perulangan untuk menampilkan data tugas yang telah dioperasikan oleh tambah_data() 
                    secara real time ketika pengguna ingin mengakses kembali data yang telah ditambahkan'''

                    for i, tugas in enumerate(daftar):

                        '''kondisi ini diperlukan karena variabel global data_tugas tersebut bernilai kosong 
                        pada awal indeks yang bisa dilihat pada operasi tambah_tugas() yakni data_tugas = '', 
                        yang nantinya jika kondisi ini tidak ada maka akan menghasilkan output seperti ini :
                        
                        ===================================
                        ========== Daftar Tugas ===========
                        ===================================
                        0
                        1.Nama Tugas
                        '''
                        if tugas:
                            print(f"{i}. {tugas}\n")

                # tekan enter untuk kembali.
                print("====================================")
                input("\n[ Tekan ENTER untuk kembali ]")

                # boolean false ketika tugas telah selesai agar bisa kembali ke halaman utama.
                status2 = False
                # keluar dari program.
                break

            # lalu membersihkan CLI Terminal agar kembali ke menu utama.
            os.system('cls')
            # boolean false ketika operasi tambah tugas telah terjalankan.
            status1 = False  

        # Kondisi ketika pengguna memilih batal menambahkan tugas.
        elif Validasi.lower() == "n":
            os.system('cls')
            print("========================================")
            print("\nBatal menampilkan tugas.\n")
            # tekan enter untuk kembali/Melanjutkan operasi selanjutnya.
            print("========================================")
            input("\n[ Tekan ENTER untuk kembali/Melanjutkan ]")
            os.system('cls')
            break

        # Kondisi ketika pengguna memberikan input yang salah.
        else:
            print("\033[91mJawaban tidak valid. Silakan masukkan 'y' atau 'n'.\033[0m")
            continue        


def tandai_tugas():
    
    global data_tugas
    #kondisi jika belum diisi tugas oleh pengguna.
    if data_tugas == "":
        # lalu membersihkan CLI Terminal.
        os.system('cls')
        print("Belum ada tugas yang bisa ditandai.")
        print("========================================")
        input("\n[ Tekan ENTER untuk kembali ]")
        # lalu membersihkan CLI Terminal.
        os.system('cls')
        # lalu kembali ke halaman utama.
        return
    '''

    pembelajaran dari kami dapatkan terkait operasi tandai_tugas()

    Saat sedang mencari solusi di internet atau biasanya saya cari di stackoverflow.com, saya menemukan bahwa
    variabel daftar yang kami dapatkan itu, kami bertanya bahwasanya " Mengapa dari data_tugas itukan bernilai string 
    bisa dirubah ke index begitu kayak list alias array sesuai permintaan oleh input pengguna ?

    data_tugas awalnya adalah sebuah string, misalnya:

    "Matematika | belum;Fisika | selesai;Kimia | belum"

    ternyata Fungsi split(';') memecah string ini menjadi list/array berdasarkan tanda ;
    Jadi hasil dari 'daftar = data_tugas.split(';')' adalah

    ["Matematika | belum", "Fisika | selesai", "Kimia | belum"]

    Karena hasil split adalah list, maka daftar sekarang bisa diakses seperti array/list biasa :

    daftar[0] → "Matematika | belum"

    daftar[1] → "Fisika | selesai"

    daftar[2] → "Kimia | belum"

    sehingga kita dapat membuat assignment baru seperti :

    tugas = daftar[input_pengguna]

    Sintaks ini artinya itu ambil elemen dari list daftar pada indeks yang diminta input_pengguna.

    contoh :

    tugas = daftar[0]

    dan seterusnya sesuai yang diminata input_pengguna.

    '''
    daftar = data_tugas.split(';')

    # Tampilkan daftar tugas yang ada agar user bisa lihat nomor tugas.
    print("===================================")
    print("========== Daftar Tugas ===========")
    print("===================================\n")
    # method perulangan untuk menampilkan sementara daftar tugas.
    for i, tugas in enumerate(daftar):
        if tugas.strip():
            print(f"{i}. {tugas.strip()}\n")
    print("\n===================================")

    ''' 
        try - except berfungsi untuk menjalankan operasi tandai_tugas() guna meminimalisir ValueError dan IndexError
        contohnya tidak memasukkan nomor yang valid atau bukan integer, atua nomor tugas yang akan ditandai diluar
        konteks atau tidak sesuai dengan nomor yang tersedia di daftar tugas.
    '''
    try:
        # Menyetor input pengguna bertipe integer guna menandai tugas menggunakan penomoran.
        input_pengguna = int(input('Pilih nomor tugas untuk ditandai selesai : '))

        # Validasi nomor tugas valid
        if input_pengguna < 0 or input_pengguna >= len(daftar):
            print("\033[91mNomor tugas tidak valid.\033[0m")
            return
        
        # Variabel tugas yang berisi list daftar guna mengambil indeks yang diminta input_pengguna.
        tugas = daftar[input_pengguna]

        # Pisahkan nama dan status, jika status belum ada, beri default "belum".
        if '|' not in tugas:
            nama = tugas.strip()
            status = "belum dikerjakan"
        else:
            nama, status = [x.strip() for x in tugas.split('|')]

        # Update status tugas jadi selesai.
        tugas_baru = f"{nama} | selesai"
        daftar[input_pengguna] = tugas_baru

        # Gabungkan kembali ke string data_tugas dengan .join.
        data_tugas = ';'.join(daftar)

        print(f"\nTugas '{nama}' telah berhasil ditandai sebagai selesai.\n")
    except ValueError:
        print("\033[91mMasukkan nomor tugas yang valid (angka saja).\033[0m")
    except IndexError:
        print("\033[91mNomor tugas di luar jangkauan daftar tugas.\033[0m")

    input("[ Tekan ENTER untuk kembali ]")
    os.system('cls')


def hapus_tugas():
    '''kami menggunakan module untuk hapus_tugas guna mempermudah kami dalam mengoperasikan fungsi hapus_tugas dengan
    memanggil fungsi hapus dari modul eksternal dan mengupdate data global'''
    
    # panggil data_tugas sebagai tempat penyimpanan yang nantinya akan update.
    global data_tugas
    # import tugasdeleted dari modul hapus_tugas.
    from operasi_hapus import tugasdeleted
    # Simpan update hasil penghapusan ke global.
    data_tugas = tugasdeleted(data_tugas) 


def cari_tugas_rekursif(daftar_tugas, keyword, indeks=0):
    """
    Mencari tugas yang mengandung keyword secara rekursif pada list tugas.
    daftar_tugas: list (by reference)
    keyword: string pencarian
    indeks: posisi saat ini, default=0 (rekursi)
    
    Mengembalikan indeks tugas yang cocok atau -1 jika tidak ditemukan.
    """
    if indeks >= len(daftar_tugas):
        return -1  # dasar rekursi, tidak ditemukan.

    if keyword.lower() in daftar_tugas[indeks].lower():
        return indeks  # ditemukan

    # panggil rekursif untuk indeks berikutnya.
    return cari_tugas_rekursif(daftar_tugas, keyword, indeks + 1)

def cari_tugas():
    ''' 
    dipanggil kembali guna bisa mengakses dan menggunakan variabel global data_tugas 
    yang menyimpan seluruh tugas dalam bentuk string. 
    '''
    global data_tugas
    # kondisi ketika data tugas kosong atau belum ditambahkan.
    if data_tugas == "":
        print("\nBelum ada tugas untuk dicari.\n")
        return

    # Ubah ke list (mutable, by reference).
    daftar = data_tugas.split(';')  
    keyword = input("Masukkan kata kunci tugas yang ingin dicari: ")

    # Assigment variable untuk mencari keyword dalam daftar.
    hasil = cari_tugas_rekursif(daftar, keyword)

    # Tampilkan Daftar Tugas
    print("\n===================================")
    print("========== Daftar Tugas ===========")
    print("===================================\n")

    # Kondisi ketika tugas belum ditambahkan sehingga tidak ditemukan.
    if hasil == -1:
        print("Tugas tidak ditemukan.")
    else:
        # Tampilkan tugas yang ditemukan dengan format yang sama seperti daftar tugas.
        print(f"{hasil}. {daftar[hasil].strip()}")

    print("\n===================================")
    input("\n[ Tekan ENTER untuk kembali ]")
    os.system('cls')


def statistik_tugas():
    '''
    fungsi yang digunakan untuk memeriksa berapa banyak jumlah total tugas, jumlah tugas yang terselesaikan
    , jumlah tugas yang belum dikerjakan.
    '''
    
    # kondisi ketika tugas belum ditambahkan.
    if data_tugas == "":
        print("Belum ada tugas yang bisa ditampilkan statistiknya.")
        print("========================================")
        input("\n[ Tekan ENTER untuk kembali ]")
        os.system('cls')
        return
    
    # Assigment untuk melihat statistik tugas siswa atau pengguna.
    statistik_tugas = data_tugas.split(';')

    # VARIABLE UTAMA (Total Tugas, Tugas Selesai, Tugas Belum Selesai).
    total_tugas = 0
    tugas_belum = 0
    tugas_selesai = 0
    
    # Perulangan untuk statistik tugas guna melakukan proses perhitungan jumlah untuk tugas selesai dan belum. 
    for i in statistik_tugas:
        if i == "":
            continue
        total_tugas += 1
        if "belum" in i:
            tugas_belum += 1
        else:
            tugas_selesai += 1
    
    # Tampilan Statistik Tugas yang berisi Total Tugas, Belum dikerjakan, Selesai  
    print ("===================================")
    print ("======= Statistik Tugas ==========")  
    print ("===================================")
    print(f"Total Tugas         : {total_tugas}       ")
    print(f"Belum dikerjakan    : {tugas_belum}       ")
    print(f"Selesai             : {tugas_selesai}     ")
    print ("===================================")

    print("========================================")
    input("\n[ Tekan ENTER untuk kembali ]")
    # lalu membersihkan CLI Terminal
    os.system('cls')