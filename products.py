import os

if os.path.isfile('products.csv'):
	print('yeah! I found the file!')
else:
	print('I can not find the file....')
	

products = []
with open ('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'product, price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)



while True:
    name = input('please inout the name of products: ')
    if name == 'q':
    	break
    price = input('input the price of this product: ')
    products.append([name, price])

print (products)

for p in products:
	print(p[0], " 's price is ", p[1])

with open ('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('product, price \n')
	for p in products:
		f.write(p[0] + ', ' + p[1] + '\n')


