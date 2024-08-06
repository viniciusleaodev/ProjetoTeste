lista = []
while True:
  num = float(input("Informe os gastos do dia:"))
  if num == 0:
    break
  
  lista.append(num)

if lista:
  lista.sort(reverse=True)
  mGast = lista[0]
  print("O seu maior gasto hoje foi R$", mGast)
else:
  print("Você não teve gastos hoje!")