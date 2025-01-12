import json
from prettytable import PrettyTable
from struktur import StructAlat, DoubleLinkedList, Queue


class PelangganMenu:
    def __init__(self):
        self.alat_berat = DoubleLinkedList()
        self.riwayat_pembelian = Queue()
        self.load_alat_berat()
        self.load_riwayat_pembelian()

    def load_alat_berat(self):
        try:
            with open("data/data_alat_berat.json", "r") as file:
                data = json.load(file)
                for item in data:
                    alat = StructAlat(item["merek"], item["jenis_alat"], item["harga"], item["stock"])
                    self.alat_berat.append(alat)
        except FileNotFoundError:
            pass

    def save_alat_berat(self):
        data = [alat.to_dict() for alat in self.alat_berat.to_list()]
        with open("data/data_alat_berat.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_riwayat_pembelian(self):
        try:
            with open("data/Riwayat_pembelian.json", "r") as file:
                if file.read().strip():  # Periksa apakah file tidak kosong
                    file.seek(0)  # Kembali ke awal file jika tidak kosong
                    data = json.load(file)
                    for item in data:
                        self.riwayat_pembelian.enqueue(item)
                else:
                    print("File Riwayat_pembelian.json kosong. Memulai dengan data kosong.")
        except FileNotFoundError:
            print("File Riwayat_pembelian.json tidak ditemukan. Memulai dengan data kosong.")
        except json.JSONDecodeError:
            print("File Riwayat_pembelian.json rusak atau formatnya salah. Memulai dengan data kosong.")


    def save_riwayat_pembelian(self):
        data = [riwayat for riwayat in self.riwayat_pembelian.queue.to_list()]
        with open("data/Riwayat_pembelian.json", "w") as file:
            json.dump(data, file, indent=4)

    def tampilkan_list_alat_berat(self):
        print("\nDaftar Alat Berat:")
        if not self.alat_berat.head:
            print("Belum ada data alat berat.")
        else:
            self.alat_berat.display()

    def binary_search(self, keyword, attribute):
        items = self.alat_berat.to_list()
        items.sort(key=lambda x: getattr(x, attribute))  
        low, high = 0, len(items) - 1
        while low <= high:
            mid = (low + high) // 2
            if getattr(items[mid], attribute).lower() == keyword.lower():
                return items[mid]
            elif getattr(items[mid], attribute).lower() < keyword.lower():
                low = mid + 1
            else:
                high = mid - 1
        return None

    def cari_alat_berat(self):
        print("\nPencarian Alat Berat:")
        print("1. Berdasarkan Merek")
        print("2. Berdasarkan Jenis Alat")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            keyword = input("Masukkan merek: ")
            result = self.binary_search(keyword, "merek")
        elif pilihan == "2":
            keyword = input("Masukkan jenis alat: ")
            result = self.binary_search(keyword, "jenis_alat")
        else:
            print("Pilihan tidak valid!")
            return
        if result:
            print(f"Alat ditemukan: {result.to_dict()}")
        else:
            print("Alat tidak ditemukan.")

    def bubble_sort(self, attribute):
        items = self.alat_berat.to_list()
        n = len(items)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if getattr(items[j], attribute).lower() > getattr(items[j + 1], attribute).lower():
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items

    def sorting_alat_berat(self):
        print("\nSorting Alat Berat:")
        print("1. Berdasarkan Merek")
        print("2. Berdasarkan Jenis Alat")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            sorted_items = self.bubble_sort("merek")
        elif pilihan == "2":
            sorted_items = self.bubble_sort("jenis_alat")
        else:
            print("Pilihan tidak valid!")
            return
        print("\nHasil Sorting:")
        table = PrettyTable(["Merek", "Jenis Alat", "Harga", "Stock"])
        for item in sorted_items:
            table.add_row([item.merek, item.jenis_alat, item.harga, item.stock])
        print(table)

    def beli_alat_berat(self):
        print("\nPembelian Alat Berat:")
        merek = input("Masukkan merek alat berat yang ingin dibeli: ")
        alat = self.binary_search(merek, "merek")
        if not alat:
            print("Alat berat tidak ditemukan.")
            return
        if alat.stock <= 0:
            print("Stok alat berat habis.")
            return
        nama = input("Masukkan nama Anda: ")
        alamat = input("Masukkan alamat Anda: ")
        no_telp = input("Masukkan nomor telepon Anda: ")

        
        alat.stock -= 1
        self.save_alat_berat()

        
        pembelian = {
            "pelanggan": nama,
            "alamat": alamat,
            "no_telp": no_telp,
            "merek": alat.merek,
            "jenis_alat": alat.jenis_alat,
        }
        self.riwayat_pembelian.enqueue(pembelian)
        self.save_riwayat_pembelian()

        print("Pembelian berhasil!")

    def menu(self):
        while True:
            print("\nMenu Pelanggan:")
            print("1. Tampilkan List Alat Berat")
            print("2. Cari Alat Berat")
            print("3. Sorting Alat Berat")
            print("4. Beli Alat Berat")
            print("5. Kembali ke Menu Utama")
            print("6. Keluar")
            pilihan = input("Pilih opsi: ")

            if pilihan == "1":
                self.tampilkan_list_alat_berat()
            elif pilihan == "2":
                self.cari_alat_berat()
            elif pilihan == "3":
                self.sorting_alat_berat()
            elif pilihan == "4":
                self.beli_alat_berat()
            elif pilihan == "5":
                break
            elif pilihan == "6":
                print("Terima kasih!")
                exit()
            else:
                print("Pilihan tidak valid!")
