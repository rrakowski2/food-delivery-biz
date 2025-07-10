'''
Module containing a unit test and input validity checks/assertions
'''

import pytest


# Function to test input validity for index
def tester_idx_input(index_length):
    while 'index' not in locals(): 
        try:
            prompt = input("\nInput index of a product/courier/order to update: ")
            index = abs(int(prompt))
        except ValueError: 
             pass
        else: 
            if prompt == '':
                tester_idx_input(index_length)
            else:
                if index > int(index_length)-1:
                    index = abs(int(input('\n'f"Input valid index from range between 0 and {int(index_length)-1}: ")))
    return index


#######################################
# Unit test for the above func (uncomment last line to run this module as standalone in the pytest interactive mode (cmmd: $pytest -s))
@pytest.fixture()
def index_length():
    return '3'
def entity():
    return entity

def test_tester_idx_input():
    expected = type(int(1))
    total_no_of_indexes = 3
    actual = type(tester_idx_input(total_no_of_indexes))
    assert expected is actual
#test_tester_idx_input()


#######################################
# Function to test input validity for deletion index
def tester2_idx_input(index_length):
    while 'index' not in locals(): 
        try:
            prompt = input("\nConfirm index to delete order/product or courier: ")
            index = abs(int(prompt))
        except ValueError: 
             pass
        else: 
            if prompt == '':
                tester_idx_input(index_length)
            else:
                if index > int(index_length)-1:
                    index = abs(int(input('\n'f"Input valid index from range between 0 and {int(index_length)-1}: ")))
    return index


#######################################
# Function to test input validity for updated phone no.
def tester_phone_no_input(entity):
    while 'number' not in locals(): 
        try:
            prompt = input(f'\nInput new/updated phone for {entity} ')
            number = abs(int(prompt)) 
        except ValueError: 
             pass
        else: 
            if prompt == '':
                tester_idx_input(index_length)
            else:
                if len(str(number)) > 15:
                    number = abs(int(input('\n'f"Input valid phone no. ")))
    return number


#######################################
# Function to test input validity for updated product's price
def tester_price_input(entity):
    while 'price' not in locals(): 
        try:
            price = abs(float(input(f'Input new/updated price for {entity} '))) 
        except ValueError: 
             pass
    return price