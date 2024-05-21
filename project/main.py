from book import Book


def main():
  user_input = input('add book(1)\nadd section(2)\n>>> ').strip().lower()
  if user_input == '1':
    add_book()
  elif user_input == '2':
    add_section()
  else:
    print('wrong input')
  
  

def add_book():
    title = input('Title: ')
    author = input('Author: ')
    genre = input('Genre: ')
    # language = input('Language: ')
    # pages = input('Pages: ')
    # rating = input('rating: ')
    book = Book(title,author,genre) 

    
def add_section():
    genre = input('Section Name: ')
    with open(f'project/sections/{genre}.csv','w') as file:
      pass
    print(f'{genre} section added succefully')
    


if __name__ == '__main__':
  main()