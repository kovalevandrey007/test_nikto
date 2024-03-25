from nikto import check_command
import pytest


def test_case1():
    assert check_command ( f'nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4 -output result.txt -Format text',
                           '0 error(s)'), 'test_1 Fail'