from menu_admin import AdminMenu
from menu_plgn import PelangganMenu

def main():
    print("Sistem Penjualan Alat Berat")
    while True:
        print("\nPilih peran:")
        print("1. Admin")
        print("2. Pelanggan")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            admin_menu = AdminMenu()
            admin_menu.menu()
        elif pilihan == "2":
            pelanggan_menu = PelangganMenu()
            pelanggan_menu.menu()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem!")
            exit()
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
