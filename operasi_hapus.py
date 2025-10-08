# import os untuk clearscreen().
import os

def tugasdeleted(Tugas_deteled):
    '''tools untuk menghapus tugas-tugas siswa yang telah tertambahkan di tampilan_data() guna siswa atau pengguna
    bisa dengan mudah menghapus tugas mereka yang telah selesai dan ingin menggantikan tugas yang baru.'''

    # kondisi ketika pengguna masih belum menambahkan tugas dan memberikan peringatan untuk menambahkan tugas.
    if Tugas_deteled == "":
        os.system('cls')
        print("Tugas masih kosong, belum ada yang bisa dihapus!")
        print("========================================")
        input("\n[ Tekan ENTER untuk kembali ]")
        os.system('cls')
        # langsung kembalikan parameter tanpa lanjut.
        return Tugas_deteled  

    ''' Tampilan Daftar tugas sementara guna pengguna atau siswa bisa melihat terkait 
    'Apa saja daftar tugas yang akan di hapus ?' '''

    os.system('cls')
    print("===================================")
    print("========== Daftar Tugas ===========")
    print("===================================\n")
    # .split guna memisahkan beberapa daftar nama tugas yang telah ditambahkan.
    daftar = Tugas_deteled.split(';')
    for i, tugas in enumerate(daftar):
        if tugas.strip():
            print(f"{i}. {tugas.strip()}\n")
    print("===================================")

    #try-except guna meminimalisir terjadinya ValueError seperti input tidak valid.
    try:
        tugas_otwhapus = int(input("\nMasukkan nomor tugas yang mau dihapus : "))

        ''' kondisi ketika penomoran tugas tersebut harus lebih dari atau sama dengan 0 
        hingga kurang dari panjang objek tipe data variable daftar '''

        if 0 <= tugas_otwhapus < len(daftar):
            print(f"Tugas '{daftar[tugas_otwhapus]}' berhasil dihapus.")

            # Hapus elemen sesuai indeks yang dipilih
            del daftar[tugas_otwhapus]
        
        # Kondisi sebaliknya jika nomor yang diinput tidak sesuai persyaratan kondisi percabangan ( if ).
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor tugas yang benar.")

    # Lalu menggabungkan list yang sudah diperbarui itu menjadi string kembali.
    Tugas_deteled = ';'.join(daftar)

    input("\n[ Tekan ENTER untuk kembali ]")
    os.system('cls')
    # langsung kembalikan parameter tanpa lanjut.
    return Tugas_deteled