#Atlantapizzas.py - calculadora de uma pizzaria


print("--------------------------------------------------")
print("olá,somos Atlanta pizzas !!!!!!")

#obter a quantidades de pizzas do cliente
num_pizzas = eval(input("quantas pizzas você deseja: "))

#obter o valor de cada pizza do cliente
valor_pizzas = eval(input("coloque o valor da pizza do cardapio: "))

#caluculo do total 
subtotal = num_pizzas * valor_pizzas

#calcular total da taxa e o definir
taxa = 0.08
taxatotal = subtotal * taxa

#calcular total de tudo e apresentar ao cliente
total = subtotal + taxatotal

print("O valor total é : R$ ",total)
print("O valor das pizzas é : R$ ",subtotal) 
print("É o imposto aplicado ao produto é de: R$ ",taxatotal)

print("--------------------------------------------------")