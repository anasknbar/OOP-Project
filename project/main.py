from book import Book
from book import Library

def main():
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            title = input('Title: ').strip()
            author = input('Author: ').strip()
            section = input('Section: ').strip()
            Library.add_book(title, author, section)
        elif choice == '2':
            section = input('Section Name: ')
            Library.add_section(section)
        elif choice == '3':
            Library.show_books(input('Section: ').strip().lower())
        elif choice == '4':
            keyword = input('Enter Book Title or Author to search for: ').strip()
            Library.search(keyword)
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            RED = "\033[31m"
            RESET = "\033[0m"
            print(f"{RED}Invalid choice. Please select a number between 1 and 5.{RESET}")

 
def display_menu():
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add Section")
    print("3. Show section")
    print("4. Search")
    print("5. Exit")
    print("--------------------")

def get_user_choice():
    choice = input("Enter your choice (1-5): ").lower().strip()
    return choice

if __name__ == '__main__':
    main()
