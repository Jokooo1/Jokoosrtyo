import json
from struktur import Stack, BubbleSort, StructAlat


class AdminMenu:
    def __init__(self):
        self.alat_berat = Stack()
        self.load_alat_berat()

    def load_alat_berat(self):
        try:
            with open("data/data_alat_berat.json", "r") as file:
                data = json.load(file)
                for item in reversed(data):  
                    alat = StructAlat(item["merek"], item["jenis_alat"], item["harga"], item["stock"])
                    self.alat_berat.push(alat)
        except FileNotFoundError:
            pass

    def save_alat_berat(self):
        data = [alat.to_dict() for alat in self.alat_berat.to_list()]
        with open("data/data_alat_berat.json", "w") as file:
            json.dump(data, file, indent=4)

    def list_alat_berat(self):
        print("\nDaftar Alat Berat:")
        if self.alat_berat.is_empty():
            print("Belum ada data alat berat.")
        else:
            self.alat_berat.display()

    def tambah_alat_berat(self):
        merek = input("Masukkan merek alat berat: ")
        jenis = input("Masukkan jenis alat berat: ")
        harga = int(input("Masukkan harga alat berat: "))
        stock = int(input("Masukkan stock alat berat: "))
        alat = StructAlat(merek, jenis, harga, stock)
        self.alat_berat.push(alat)
        self.save_alat_berat()
        print("Alat berat berhasil ditambahkan!")

    def hapus_alat_berat(self):
        if self.alat_berat.is_empty():
            print("Tidak ada alat berat untuk dihapus.")
        else:
            removed = self.alat_berat.pop()
            self.save_alat_berat()
            print(f'Alat berat "{removed.merek}" berhasil dihapus!')

    def menu(self):
        while True:
            print("\nMenu Admin:")
            print("1. List Alat Berat")
            print("2. Tambah Alat Berat")
            print("3. Hapus Alat Berat")
            print("4. Kembali ke Menu Utama")
            print("5. Keluar")
            pilihan = input("Pilih opsi: ")

            if pilihan == "1":
                self.list_alat_berat()
            elif pilihan == "2":
                self.tambah_alat_berat()
            elif pilihan == "3":
                self.hapus_alat_berat()
            elif pilihan == "4":
                break
            elif pilihan == "5":
                print("Terima kasih!")
                exit()
            else:
                print("Pilihan tidak valid!")
