'''
Unit test for input validity
'''


import pytest


def tester_idx_input(index_length):
    while 'index' not in locals(): 
        try:
            index = abs(int(input("\nInput index of a product to update: ")))
        except ValueError: 
             pass
        else: 
            if index > int(index_length)-1:
                index = abs(int(input('\n'f"Input valid index from range between 0 and {int(index_length)-1}: ")))
    return index


@pytest.fixture()
def index_length():
    return '3'
def test_tester_idx_input():
    expected = type(int(1))
    total_no_of_indexes = 3
    actual = type(tester_idx_input(total_no_of_indexes))
    assert expected is actual
#test_tester_idx_input()
