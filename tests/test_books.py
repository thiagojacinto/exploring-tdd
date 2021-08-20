from unittest import skip
from unittest.mock import patch

from collection.books import (
    execute_url,
    search_books
)

@skip(reason = "Modified / Not yet implemented return type")
def test_when_search_by_author_should_return_a_string():
    result = type(search_books("Itamar Vieira Junior"))
    assert result == str

def test_when_search_by_author_should_prepare_a_request_with_that_data():
    author_name = "Itamar Vieira Junior"
    with patch("collection.books.prepare_request") as duble_prepare_request:
        search_books(author_name)
        duble_prepare_request.assert_called_once_with(author_name)

def test_when_search_with_author_name_should_use_prepare_request_return_as_input_to_get_url():
    author_name = "Itamar Vieira Junior"
    dados = { 'author_name': author_name }
    with patch("collection.books.prepare_request") as duble_prepare_request:
        duble_prepare_request.return_value = dados
        with patch("collection.books.get_url") as duble_get_url:
            search_books(author_name)
            duble_get_url.assert_called_once_with("https://go.to", dados)

def test_when_search_with_author_name_should_use_get_url_return_as_input_to_execute():
    author_name = "Itamar Vieira Junior"
    url = "https://go.to"
    with patch("collection.books.get_url") as duble_get_url:
        duble_get_url.return_value = url
        with patch("collection.books.execute") as duble_execute:
            search_books(author_name)
            duble_execute.assert_called_once_with(url)

class StubHttpResponse:

    def read(self):
        return b""

    def __enter__(self):
        return self

    def __exit__(self, p1, p2, p3):
        pass

def test_when_call_execute_url_then_string_should_be_returned():
    with patch("collection.books.urlopen", return_value = StubHttpResponse()):
        result = execute_url("https://go.to")
        assert type(result) == str