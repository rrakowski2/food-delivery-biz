# add products from a Python list to a .txt file
def save_products(cafe_products):
    file = None
    #print(cafe_products)
    try:
        open("products.txt", "w").close()
        file = open('products.txt', 'a')
        for item in cafe_products:
            file.write(item + '\n')
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    finally:
        if file:
            file.close()