from prettytable import PrettyTable


class StructAlat:
    def __init__(self, merek, jenis_alat, harga, stock):
        self.merek = merek
        self.jenis_alat = jenis_alat
        self.harga = harga
        self.stock = stock

    def to_dict(self):
        return {
            "merek": self.merek,
            "jenis_alat": self.jenis_alat,
            "harga": self.harga,
            "stock": self.stock,
        }


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    def display(self):
        table = PrettyTable(["Merek", "Jenis Alat", "Harga", "Stock"])
        current = self.head
        while current:
            data = current.data.to_dict()  
            table.add_row([data["merek"], data["jenis_alat"], data["harga"], data["stock"]])
            current = current.next
        print(table)


class Stack:
    def __init__(self):
        self.head = None  
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return removed_data

    def is_empty(self):
        return self.size == 0

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    def display(self):
        """Menampilkan data dalam stack menggunakan PrettyTable."""
        table = PrettyTable(["Merek", "Jenis Alat", "Harga", "Stock"])
        current = self.head
        while current:
            data = current.data.to_dict()  
            table.add_row([data["merek"], data["jenis_alat"], data["harga"], data["stock"]])
            current = current.next
        print(table)


class Queue:
    def __init__(self):
        self.queue = DoubleLinkedList()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue.head:
            return None
        data = self.queue.head.data
        self.queue.head = self.queue.head.next
        if self.queue.head:
            self.queue.head.prev = None
        else:
            self.queue.tail = None
        return data

    def display(self):
        table = PrettyTable(["Nama Pelanggan", "Alamat", "No Telepon", "Merek", "Jenis Alat"])
        current = self.queue.head
        while current:
            data = current.data
            table.add_row([data["pelanggan"], data["alamat"], data["no_telp"], data["merek"], data["jenis_alat"]])
            current = current.next
        print(table)

class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self, key):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j][key] > self.data[j + 1][key]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]


class BinarySearch:
    def __init__(self, data):
        self.data = data

    def search(self, key, value):
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid][key] == value:
                return self.data[mid]
            elif self.data[mid][key] < value:
                left = mid + 1
            else:
                right = mid - 1
        return None