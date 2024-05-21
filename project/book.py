class Library:
  @staticmethod
  def save_book(title,author,section):
    try:
      with open(f'project/sections/{section}.csv','r+') as file:
        content = file.readlines() 
        if len(content) > 0:
          file.write(f'{title},{author},{section}\n')
        else:
          file.write(f'Title,Author,section\n')
          file.write(f'{title},{author},{section}\n')
          print(f'{title} book added to {section} succefully')
    except FileNotFoundError:
      print(f'{section} section is not exist, try adding it')
  

class Book:
  def __init__(self,title,author,section):
    self.title = title
    self.author = author
    self.section = section
    # self.language = language
    # self.pages = pages
    # self.rating = rating
    # self.summary = summary
    Library.save_book(self.title,self.author,self.section)
    
  
    
  
  
      
      
      
      
# sample > Harry Poter ,J.K. Rowling, fiction
      