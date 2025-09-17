#menu
books = []

while True:
  print( ' --- Library Menu ---')
  print('1. Add Book')
  print('2. View All Books')
  print('3. Search Book')
  print('4. Remove Book')
  print('5. Exit')


  choice = int(input('enter option: '))

  if choice == 1:
        bookname = input('enter book name:')
        author = input('enter author name:')
        bookdetail = {"title": bookname, "author": author}
        books.append(bookdetail)
        print('book added successfull')
    
  elif choice == 2:
        print('Books ', books)

  elif choice == 3:
      search = input("Enter book name to search: ")
  
      found = False
      for book in books:
          if book["title"].lower() == search.lower():   # case-insensitive
              print("Book found:", book)
              found = True
              break
  
      if not found:
          print("No such book available")
