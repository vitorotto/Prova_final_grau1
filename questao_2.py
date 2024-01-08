# Vitor Hugo Otto
# Q - 02
nome = input("Insira seu nome: ")
n1 = float(input("Qual sua primeira nota? "))
n2 = float(input("Qual sua segunda nota? "))

media = (n1 + n2) / 2

if media >= 8:
    print(nome, "você foi aprovado por média %.1f" %media)
else:
  if media < 8:
    if media < 4:
        print(nome, "você foi reprovado por média %.1f" %media)
    else:
      nota_exame = float(input("insira a nota do exame: "))
      if n1 < n2:
          media = (nota_exame + n2) / 2
      else: 
          media = (nota_exame + n1) / 2
          if media >= 6:
             print(nome, "você foi aprovado após exame com média %.1f" %media)
          else:
             print(nome, "você foi reprovado após exame com média %.1f" %media)