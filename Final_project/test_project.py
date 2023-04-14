import unittest
from project import create_task, get_number, get_topic, get_pages, get_payment, get_deadline
from unittest.mock import Mock, patch



class TestProductClass(unittest.TestCase):
    def test_create_task(self):
        input_mock = Mock()
        input_mock.side_effect = ["111aaa", "10.10.2022", "Math", "10", "105"]

        with patch('builtins.input', input_mock):
            result = create_task()
        assert result.number == "111aaa"
        assert result.deadline == "10 Oct 2022"
        assert result.topic == "Math"
        assert result.pages == 10
        assert result.payment == 105

    def test_get_number(self) -> None:
        with patch('builtins.input', new=Mock(return_value='123abc')):
            assert get_number() == '123abc'
        with patch('builtins.input', new=Mock(return_value='111xxx')):
            assert get_number() == '111xxx'

    def test_get_topic(self) -> None:
        with patch('builtins.input', new=Mock(return_value='math')):
            assert get_topic() == 'Math'
        with patch('builtins.input', new=Mock(return_value='IT')):
            assert get_topic() == 'It'

    def test_get_pages(self) -> None:
        with patch('builtins.input', new=Mock(return_value='10')):
            assert get_pages() == 10
        with patch('builtins.input', new=Mock(return_value='5')):
            assert get_pages() == 5
        with patch('builtins.input', new=Mock(return_value='100')):
            assert get_pages() == 100

    def test_get_payment(self):
        assert get_payment(10) == 105.0
        assert get_payment(5) == 52.50
        assert get_payment(12) == 126.0

    def test_get_deadline(self) -> None:
        with patch('builtins.input', new=Mock(return_value='1.2.2022')):
            assert get_deadline() == '01 Feb 2022'
        with patch('builtins.input', new=Mock(return_value='06.08.2010')):
            assert get_deadline() == '06 Aug 2010'
        with patch('builtins.input', new=Mock(return_value='11.12.1999')):
            assert get_deadline() == '11 Dec 1999'


if __name__ == '__main__':
    unittest.main()