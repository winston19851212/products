products = []
while True:
    name = input('please inout the name of products: ')
    if name == 'q':
    	break
    price = input('input the price of this product: ')
    products.append([name, price])

print (products)
products[0][0]
