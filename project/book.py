
from tabulate import tabulate
import sys
class Library:
  
  
  @staticmethod
  def save_book(title,author,section):
    try:
      with open(f'project/sections/{section}.csv','r+') as file:
        content = file.readlines() 
        if len(content) > 0:
          file.write(f'{title},{author},{section}\n')
          GREEN = '\033[32m'
          REST = "\033[0m"
          print(f'{GREEN}{title} book added to {section} section succefully{REST}')
        else:
          file.write(f'Title,Author,section\n')
          file.write(f'{title},{author},{section}\n')
          GREEN = '\033[32m'
          REST = "\033[0m"
          print(f"{GREEN}{title} book added to {section} section succefully{REST}")
    except FileNotFoundError:
      RED = "\033[31m"
      RESET = "\033[0m"
      print(f"{RED}{section}section is not exist, try adding it{RESET}")
      
  @staticmethod
  def add_book():
    title = input('Title: ').strip()
    author = input('Author: ').strip()
    section = input('Section: ').strip()
    book = Book(title,author,section) 
    
  @staticmethod
  def add_section():
    section = input('Section Name: ')
    with open(f'project/sections/{section}.csv','w') as file:
      pass
    
    print(f'{section} section added succefully')
    with open(f'project/sections/section_paths.csv','a') as file:
      file.write(f'{section}.csv\n')
    

  
  @staticmethod
  def show_books(section):
  
    if section == 'all':
      headers = ['Title', 'Author', 'section']
      data = []
      with open('project/sections/section_paths.csv','r') as file:
        lines = file.readlines()
        for line in lines:
          with open(f'project/sections/{line.strip()}','r') as file:
            lines = file.readlines()
            
            for index,line in enumerate(lines[1:]):
              title,author,section = line.split(',') 
              data.append([title, author, section])
      print(tabulate(data, headers, tablefmt='grid'))
        
      
    else:
      try:
        with open(f'project/sections/{section}.csv','r') as file:
          lines = file.readlines()
          headers = ['Title', 'Author', 'section']
          data = []
          for index,line in enumerate(lines[1:]):
            title,author,section = line.split(',') 
            data.append([title, author, section])
          print(tabulate(data, headers, tablefmt='grid'))
      except FileNotFoundError:
        sys.exit(f'{section} section not exist :(')
  @staticmethod
  
  def search(keyword):
    headers = ['Title', 'Author', 'section']
    data = []
    with open('project/sections/section_paths.csv','r') as file:
        lines = file.readlines()
        for line in lines:
          with open(f'project/sections/{line.strip()}','r') as file:
            lines = file.readlines()
            
            for index,line in enumerate(lines[1:]):
              if keyword.lower() in line.lower():
                title,author,section = line.split(',') 
                data.append([title, author, section])
    if len(data) == 0:
      RED = "\033[31m"
      RESET = "\033[0m"
      print(f'{RED}sorry no data found :({RESET}') 
      return          
    print(tabulate(data, headers, tablefmt='grid'))
 


class Book:
  def __init__(self,title,author,section):
    self.title = title
    self.author = author
    self.section = section
    Library.save_book(self.title,self.author,self.section)
    
  
    
  
  
      
      
      
      