class Library:
    def __init__(self) :
        self.members = []
        self.books = []

    def add_member(self):
        # self.members.append(member)
        name = input(' Enter member name: ')
        email = input(' Enter member email: ')
        level = input(' Enter member level (A/B/C): ').upper()
        value = False
        while not value:
            if level in ['A', 'B', 'C']:
                member = Member(name, email, level)
                self.members.append(member)
                print('# Member added successfully#')
                value = True
            else:
                level = input('Invalid Input ! , Please enter member level again (A/B/C): ').upper()



    def edit_member(self):
      id = int(input("Enter member ID: "))
      member=self.Find_MemberID(id)
      name = input('* Enter member name: ')
      email = input('* Enter member email: ')
      level = input('* Enter member level (A/B/C): ').upper()
      value = False
      while not value:
            if level in ['A', 'B', 'C']:
                 print('# Member details updated successfully')
                 value = True
            else:
                level = input('Invalid Input ! , Please enter member level again (A/B/C): ').upper()
      member.name=name
      member.email=email
      member.level=level





    def show_members(self):
        space = ' ' * 30
        # max lenght of name is (15) and max length of email is (30)
        print(f'ID  | Name{" " * 11}| Email{" " * 25}| Level')
        print('-' * 65)

        for memb in self.members:
            s1 = 15 - len(memb.name)  # spaces after name
            s2 = 30 - len(memb.email)  # spaces after email
            print(f'{memb.id_member}   | {memb.name + space[:s1]}| {memb.email + space[:s2]}| {memb.level}')

    def delete_member(self):
        id=int(input("enter the id_member !:"))
        x=self.Find_MemberID(id)
        if x:
         self.members.remove(x)
         print(f'# Member {x.name} deleted successfully')
         for book in self.books:
            if book.id in x.borrowd:
                book.is_available = False
                break


    def add_book(self):
        # self.books.append(book)
        title = input('* Enter Book Title: ')
        author = input('* Enter Book Author: ')
        level = input('* Enter Book level (A/B/C): ').upper()

        while True:
            if level in ['A', 'B', 'C']:
               book = Book(title,author,level)
               self.books.append(book)
               print('# Member added successfully')
               break
            else:
                level = input('Invalid Input ! , Please enter book level again (A/B/C): ').upper()


    def show_books(self):
        spaces = ' ' * 15
        # max lenght of title is (15) and max length of author is (15)
        print(f'ID  | Title{" " * 10}| Author{" " * 9}| Level | Status')
        print('-' * 65)
        for book in self.books:
            s1 = 15 - len(book.title)  # spaces after title
            s2 = 15 - len(book.author)  # spaces after author
            print(
                f'{book.id_book}   | {book.title + spaces[:s1]}| {book.author + spaces[:s2]}| {book.level + " " * 4} | {"Available" if book.is_available else "Not "}')

    def Find_BOOKID(self,id):
        for book in self.books:
            if book.id_book==id:
                return book
                break
            else:
               print("Invaild ID_BOOK ")


    def Find_MemberID(self,id):
        for member in self.members:
            if member.counter_mem==id:
                return member
                break
            else:
              print("Invaild ID_MEMBER")



    def borrow_book(self):
        member_id=int(input("enter the id_member :"))
        book_id = int(input("enter the id_book :"))

        member1 =self.Find_MemberID(member_id)
        book1 =self.Find_BOOKID(book_id)
        if member1 is None or book1 is None:
           print("Member or Book not found.")

        elif member1.level != book1.level:
            return "Member cannot borrow this book due to level mismatch."

        elif not book1.is_available:
            return "Book is already borrowed."
        else:
         member1.borrowd_books.append(book1.id_book)
         book1.is_available = False
         print(f"{member1.name} has borrowed {book1.title}.")

    def return_book(self):
        member_id = int(input("enter the id_member :"))
        book_id = int(input("enter the id_book :"))
        member = self.Find_MemberID(member_id)
        book = self.Find_BOOKID(book_id)

        if member is None or book is None:
           print( "Member or Book not found.")
        else:

         if book.id_book in member.borrowd_books:
            member.borrowd_books.remove(book.id_book)
            book.is_available = True
            print( f"{member.name} has returned {book.title}.")
         else:
           print( f"{member.name} did not borrow {book.title}.")


class Member:
    counter_mem=0
    def __init__(self, name, email, level) :
        Member.counter_mem += 1
        self.name = name
        self.email = email
        self.level = level
        self.id_member = Member.counter_mem
        self.borrowd_books = []


class Book:
    counter_book=0
    def __init__(self, title, author, level) :
        Book.counter_book+= 1
        self.title = title
        self.author = author
        self.level = level
        self.id_book = Book.counter_book
        self.is_available=True


lib = Library()

menu="""1. Add Member
2. Edit Member
3. Show Members
4. Delete Member
5. Add Book
6. Show Books
7. Borrow Book
8. Return Book
9. Exit"""

print(' Welcome to the Library System '.center(100,'-'))
while True:
    print(menu)
    try:
     choice = int(input('Enter your choice : '))
    except:
        print("value error ! please enter numrical value")
    else:
     if choice == 1:
        lib.add_member()

     elif choice == 2:
        lib.edit_member()

     elif choice == 3:
        lib.show_members()

     elif choice == 4:
        lib.delete_member()
     elif choice == 5:
        lib.add_book()

     elif choice == 6:
        lib.show_books()

     elif choice == 7:
        lib.borrow_book()

     elif choice == 8:
        lib.return_book()

     elif choice == 9:
        exit()

