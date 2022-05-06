"""
Answers:

1. A1
2. F2
3. D3
4. A4
5. E5
6. G6
7. C8

"""
from tenor.piano import piano


def test_extract_a1():
    assert piano[12] == "A1"


def test_extract_f2():
    assert piano[20] == "F2"


def test_extract_d3():
    assert piano[29] == "D3"


def test_extract_a4():
    assert piano[48] == "A4"


def test_extract_e5():
    assert piano[55] == "E5"


def test_extract_g6():
    assert piano[70] == "G6"


def test_extract_c8():
    assert piano[87] == "C8"
