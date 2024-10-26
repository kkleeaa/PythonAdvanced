from abc import ABC, abstractmethod

class pritable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class book(pritable):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def print_info(self):
        print(f"book:{self.title} by {self.author}")

book=book("the kite runner","khaled hosseini")
book.print_info()