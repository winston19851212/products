import os

def read_file(filename):
    products = []
    with open (filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'product, price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products




def user_input(products):
    while True:
        name = input('please inout the name of products: ')
        if name == 'q':
            break
        price = input('input the price of this product: ')
        products.append([name, price])

    print (products)
    return(products)

def print_products(products):
    for p in products:
        print(p[0], " 's price is ", p[1])

def write_file(filename, products):
    with open (filename, 'w', encoding = 'utf-8') as f:
        f.write('product, price \n')
        for p in products:
            f.write(p[0] + ', ' + p[1] + '\n')



def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('yeah! I found the file!')
        products = read_file(filename)
    else:
        print('I can not find the file')


    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
