
produto_1 = float(input("Preco 1: "))
produto_2 = float(input("Preco 2: "))
produto_3 = float(input("Preco 3: "))

if produto_1 > produto_2 and produto_2 > produto_3:
    print("Compre o produto 3")
elif produto_2 > produto_1 and produto_1 < produto_3:
    print("Compre o produto 1")