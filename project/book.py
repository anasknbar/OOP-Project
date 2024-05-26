from tabulate import tabulate
import sys
import os

class Library:
  
    @staticmethod
    def save_book(title, author, section):
        try:
            with open(f'project/sections/{section}.csv', 'a') as file:
                if os.path.getsize(f'project/sections/{section}.csv') == 0:
                    file.write('Title,Author,Section\n')
                file.write(f'{title},{author},{section}\n')
                GREEN = '\033[32m'
                RESET = "\033[0m"
                print(f'{GREEN}{title} book added to {section} section successfully{RESET}')
        except FileNotFoundError:
            RED = "\033[31m"
            RESET = "\033[0m"
            print(f"{RED}{section} section does not exist. Try adding it.{RESET}")

    @staticmethod
    def add_book(title, author, section):
        Library.save_book(title, author, section)
    
    @staticmethod
    def add_section(section):
        try:
            os.makedirs(f'project/sections/{section}')
            print(f'{section} section added successfully')
        except FileExistsError:
            print(f'{section} section already exists.')
  
    @staticmethod
    def show_books(section):
        if section == 'all':
            headers = ['Title', 'Author', 'Section']
            data = []
            with open('project/sections/section_paths.csv', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    with open(f'project/sections/{line.strip()}', 'r') as section_file:
                        lines = section_file.readlines()
                        for index, line in enumerate(lines[1:]):
                            title, author, section = line.strip().split(',')
                            data.append([title, author, section])
            print(tabulate(data, headers, tablefmt='grid'))      
        else:
            try:
                with open(f'project/sections/{section}.csv', 'r') as file:
                    headers = ['Title', 'Author', 'Section']
                    data = []
                    lines = file.readlines()
                    for index, line in enumerate(lines[1:]):
                        title, author, section = line.strip().split(',')
                        data.append([title, author, section])
                    print(tabulate(data, headers, tablefmt='grid'))
            except FileNotFoundError:
                sys.exit(f'{section} section does not exist.')
    
    @staticmethod
    def search(keyword):
        headers = ['Title', 'Author', 'Section']
        data = []
        with open('project/sections/section_paths.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                with open(f'project/sections/{line.strip()}', 'r') as section_file:
                    lines = section_file.readlines()
                    for index, line in enumerate(lines[1:]):
                        if keyword.lower().strip() in line.lower().strip():
                            title, author, section = line.strip().split(',')
                            data.append([title, author, section])
        if len(data) == 0:
            RED = "\033[31m"
            RESET = "\033[0m"
            print(f'{RED}Sorry, no data found.{RESET}') 
            return          
        print(tabulate(data, headers, tablefmt='grid'))

class Book:
    def __init__(self, title, author, section):
        self.title = title
        self.author = author
        self.section = section
        Library.save_book(self.title, self.author, self.section)
