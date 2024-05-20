class BookCollection:
    collection = []

    def insert_book(self, book_name):
        self.collection.append(book_name)
        print(self.collection)
        return self.collection

    def remove_book(self, book):
        self.collection.remove(book)
        print(self.collection)
        return self.collection

    def locate_book(self, book_name):
        index = self.collection.index(book_name)
        print(f'{index} - это индекс книги')
        return index

my_collection = BookCollection()
my_collection.insert_book('Война и мир')
my_collection.remove_book('Война и мир')
my_collection.insert_book('Гена')
my_collection.insert_book('Волк')
my_collection.locate_book('Волк')
