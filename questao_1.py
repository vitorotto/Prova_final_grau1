# Vitor Hugo Otto
# Q - 01
produto = int(input("Código do produto: "))
quant = int(input("Quantidade: "))
prod24 = 12.9
prod32 = 3.5
prod46 = 22

if produto == 24:
    divida = prod24 * quant
    print("O total a ser pago é: R$%.2f" %divida)
elif produto == 32:
    divida = prod32 * quant
    print("O total a ser pago é: R$%.2f" %divida)
elif produto == 46:
    divida = prod46 * quant
    print("O total a ser pago é: R$%.2f" %divida)




