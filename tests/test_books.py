from typing import Collection
from unittest import skip
from unittest.mock import (
    MagicMock,
    patch,
    Mock
)

from collection.books import (
    execute_url,
    search_books,
    write_file
)

@skip(reason = "Modified / Not yet implemented return type")
def test_when_search_by_author_should_return_a_string():
    result = type(search_books("Itamar Vieira Junior"))
    assert result == str

def test_when_search_by_author_should_prepare_a_request_with_that_data():
    author_name = "Itamar Vieira Junior"
    with patch("collection.books.prepare_request") as spy_prepare_request:
        search_books(author_name)
        spy_prepare_request.assert_called_once_with(author_name)

def test_when_search_with_author_name_should_use_prepare_request_return_as_input_to_get_url():
    author_name = "Itamar Vieira Junior"
    dados = { 'author_name': author_name }
    with patch("collection.books.prepare_request") as stub_prepare_request:
        stub_prepare_request.return_value = dados
        with patch("collection.books.get_url") as spy_get_url:
            search_books(author_name)
            spy_get_url.assert_called_once_with("https://go.to", dados)

def test_when_search_with_author_name_should_use_get_url_return_as_input_to_execute():
    author_name = "Itamar Vieira Junior"
    url = "https://go.to"
    with patch("collection.books.get_url") as stub_get_url:
        stub_get_url.return_value = url
        with patch("collection.books.execute") as spy_execute:
            search_books(author_name)
            spy_execute.assert_called_once_with(url)

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

@patch("collection.books.os.makedirs", side_effect=OSError("Not allowed to create directory /tmp"))
@patch("collection.books.logging")
def test_when_create_directory_should_throw_exception(spy_logging, stub_makedirs):
    file = '/tmp/file'
    content = 'this is the file content'
    write_file(file, content)
    stub_makedirs.assert_called_once_with('/tmp')
    spy_logging.exception.assert_called_once_with('Not allowed to create directory /tmp')

@patch("collection.books.os.makedirs")
@patch("collection.books.logging")
@patch("collection.books.open", side_effect=FileExistsError())
def test_when_create_file_that_already_exists(stub_open, spy_logging, stub_makedirs):
    file = '/tmp/test/file'
    content = 'this is the file content'
    write_file(file, content)
    stub_open.assert_called_once_with(file, 'w')
    spy_logging.exception.assert_called_once_with('File /tmp/test/file already exists')

