'''
    ========================================================================================
    |                                                                                      |
    |                           SISTEM PENDAFTARAN KURSUS ONLINE                           |
    |                                                                                      |
    |                                                                                      |
    |                                        OLEH:                                         |
    |                                                                                      |
    |                       Muhammad Rossi Ramadhan ( 250535625057 )                       |
    |                       Muhammad Totti Al Fikri ( 250535630175 )                       |
    |                       Naufal Hilman Azhary    ( 250535601012 )                       |
    |                                                                                      |
    |                                                                                      |
    ========================================================================================
'''
# import os untuk clearscreen().
import os

# import tambah_tugas, tampil_tugas, tandai_tugas, hapus_tugas, cari_tugas, statistik_tugas dari modul operasi_utama.
from operasi_utama import tambah_tugas, tampil_tugas, tandai_tugas, hapus_tugas, cari_tugas, statistik_tugas

# Kondisi benar pada perulangan agar program utama tetap berjalan hingga keputusan pengguna atau siswa memilih keluar program.
while True:

    # Tampilan Menu Utama Sistem Manajemen Tugas Sederhana.
    print("==================================")
    print("Sistem Manajemen Tugas Sederhana")
    print("==================================\n")
    print("1. Tambah Tugas\n")
    print("2. Lihat Tugas\n")
    print("3. Tandai Tugas\n")
    print("4. Hapus Tugas\n")
    print("5. Cari Tugas\n")
    print("6. Statistik Tugas\n")

    # Input pengguna atau siswa untuk memilih menu guna membantu siswa mengorganisir tugas-tugas mereka.
    pilihan = input("Pilih menu dengan memasukkan angka saja (1,2,3,4,5,6) : ")

    # kondisi match-case guna memilih sesuai penomoran yang dipilih oleh siswa atau pengguna.
    match pilihan:
        case "1":
            tambah_tugas()
        case "2":
            tampil_tugas()
        case "3":
            tandai_tugas()
        case "4":
            hapus_tugas()
        case "5":
            cari_tugas()
        case "6":
            statistik_tugas()
        # Kondisi ketika pengguna memberikan input selain penomoran menu utama Sistem Manajemen Tugas Sederhana.
        case _:
            print("\ntidak valid, mohon masukkan angka saja (1,2,3,4,5,6)")
            input("\n[ Tekan ENTER untuk melanjutkan ]")
            os.system('cls')
            continue