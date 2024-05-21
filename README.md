# OOP-Project
# Library Management System
This Python script implements a simple command-line library management system. It allows users to add books, add sections, view books in a section, and search for books by title, author, or section.
## Features
- Add new books to the library.
- Create new sections for organizing books.
- View all books in a specific section or in all sections.
- Search for books by title, author, or section.
- Command-line interface for easy interaction.
4. Follow the on-screen instructions to navigate through the menu and perform various actions.
## On-Screen Instructions
### Library Menu
- The user is presented with a menu with the following options:
  - **Add Book**: Allows the user to add a new book to the library. The user will be prompted to enter the title, author, and section of the book.
  - **Add Section**: Allows the user to create a new section in the library to organize books.
  - **Show Section**: Displays all books in a specific section. The user needs to input the name of the section they want to view.
  - **Search**: Allows the user to search for books by title, author, or section. The user needs to input a keyword to search for.
  - **Exit**: Exits the application.
### Getting User's Choice
- After displaying the menu, the program prompts the user to enter their choice by typing a number from 1 to 5.
- If the user enters an invalid choice (a number outside the range 1-5), an error message is displayed, and the menu is displayed again.
### Executing User's Choice
- Depending on the user's choice, the corresponding action is executed:
  - If the user chooses to add a book (`1`), they are prompted to input the book's details, and the book is added to the library.
  - If the user chooses to add a section (`2`), they are prompted to input the name of the new section, and the section is created.
  - If the user chooses to show books in a section (`3`), they are prompted to input the name of the section they want to view, and the books in that section are displayed.
  - If the user chooses to search for books (`4`), they are prompted to input a keyword to search for, and the matching books are displayed.
  - If the user chooses to exit the application (`5`), a farewell message is displayed, and the program terminates.
### Error Handling
- If the user enters an invalid choice (not a number or a number outside the range 1-5), they receive an error message and are prompted to enter a valid choice.