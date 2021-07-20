from unittest import mock
from unittest.mock import MagicMock, mock_open

import pytest
from pytest import raises

from linereader import readFromFile


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock()
    mock_file.readline.return_value = "test line"
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = readFromFile("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"


def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = readFromFile("blah")
