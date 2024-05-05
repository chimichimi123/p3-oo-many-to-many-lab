
class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []

    def contracts(self):
        return self._contracts

    def books(self):
        return self._books

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        self._books.append(book)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return self._authors


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("Book must be of type Book")
        if not isinstance(date, str):
            raise Exception("Date must be of type str")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be of type int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        author._contracts.append(self)
        author._books.append(book)
        book._contracts.append(self)
        book._authors.append(author)

        self.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]