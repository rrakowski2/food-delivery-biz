# add items from a Python list to a .txt file
def save_couriers(couriers):
    file = None
    try:
        open("couriers.txt", "w").close()
        file = open('couriers.txt', 'a')
        for item in couriers:
            file.write(item + '\n')
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    #else: 
        #file = open('couriers.txt', 'r')
        #var = file.read()
        #print(var)
    finally:
        if file:
            file.close()
