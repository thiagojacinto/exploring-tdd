from collection.books import (
    search_books
)

def test_when_search_by_author_should_return_a_string():
    result = type(search_books("Itamar Vieira Junior"))
    assert result == str