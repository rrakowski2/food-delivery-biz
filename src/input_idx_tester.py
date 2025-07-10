def tester_idx_input(data=None):

    while 'index' not in locals(): 
        try:
            index = int(input("\nInput index of a product to update: "))
        except ValueError: 
             pass
        else: 
            if index > len(data)-1:
                index = int(input('\n'f"Input valid index from range between 0 and {len(data)-1}: "))
    return index