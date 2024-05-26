#test.py

import unittest.mock
from book import Library

class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        # Test adding a book
        title = "Test Title"
        author = "Test Author"
        section = "test_section"
        Library.save_book = unittest.mock.Mock()
        Library.add_book(title, author, section)
        Library.save_book.assert_called_with(title, author, section)

    def test_add_section(self):
        # Test adding a section
        section = "test_section"
        with unittest.mock.patch('os.path.exists', return_value=False):
            with unittest.mock.patch('os.makedirs') as mock_makedirs:
                Library.add_section(section)
                mock_makedirs.assert_called_with(f'project/sections/{section}')

def test_search(self):
    # Test searching for a book
    keyword = "Test Title"
    with unittest.mock.patch('builtins.print'):
        Library.search(keyword)
        Library.show_books.assert_called_with('all')




if __name__ == '__main__':
    unittest.main()
