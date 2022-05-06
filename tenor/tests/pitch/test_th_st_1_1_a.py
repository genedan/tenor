"""
Answers:

1. C1
2. E2
3. F3
4. B4
5. A5
6. G6
7. D7
"""

from tenor.piano import piano


def test_extract_c1():
    assert piano[3] == "C1"


def test_extract_e2():
    assert piano[19] == "E2"


def test_extract_f3():
    assert piano[32] == "F3"


def test_extract_b4():
    assert piano[50] == "B4"


def test_extract_a5():
    assert piano[60] == "A5"


def test_extract_g6():
    assert piano[70] == "G6"


def test_extract_d7():
    assert piano[77] == "D7"
