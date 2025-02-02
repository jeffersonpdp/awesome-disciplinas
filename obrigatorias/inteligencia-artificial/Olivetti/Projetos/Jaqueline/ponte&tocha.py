# PROBLEMA DA PONTE E DA TOCHA
# Quatro pessoas chegam a um rio no meio da noite.
# Há uma ponte estreita, mas ela só pode aguentar duas pessoas ao mesmo tempo.
# Porque é noite, a tocha deve ser usada para atravessar a ponte.
# A pessoa A pode atravessar a ponte em um minuto;
# A pessoa B em 2 minutos;
# A pessoa C em 5 minutos;
# A pessoa D em 8 minutos;
# Quando duas pessoas atravessam a ponte juntos, eles devem se mover no ritmo da pessoa mais lenta.
# Todos eles poderão atravessar a ponte em 15 minutos ou menos?

#Resolução baseada nos conceitos de Best-First Search e Greedy Search, onde o nó expandido minimiza o custo.

tmax = 15
V = [8,1,2,5]
V.sort(key=int)

A = V[0]
B = V[1]
C = V[2]
D = V[3]

print(f' A - pessoa mais rápida - travessia em {A} minuto(s).')
print(f' B - pessoa rápida - travessia em {B} minuto(s).')
print(f' C - pessoa lenta - travessia em {C} minuto(s).')
print(f' D - pessoa mais lenta - travessia em {D} minuto(s).')
print('*'*30)

LadoA = V
LadoB = []
move = []
Ttotal = 0
Tfica = 0
Tvolta = 0
c = 0
next = 0

while len(LadoA) >2:
  next = c + 1
  LadoB.append(V[c]) #otimiza o tempo escolhendo as duplas (nó) com menor ou maior tempo, força os dois mais lentos a atravessarem juntos
  LadoB.append(V[next])
  LadoB.sort(key=int) #organiza a lista das pessoas que já estão no lado final para que a de menor tempo seja escolhida para voltar
  print(f'Passo {next}: As pessoas que atravessam em {V[c]} e {V[next]} minuto(s) cruzam a ponte.')
  Tvolta = LadoB[0]
  Tfica = V[next]
  print(f' A que atravessa em {Tvolta} minuto(s) volta.')
  del (LadoB[0])
  del (LadoA[next])
  del (LadoA[c])
  LadoA.append(Tvolta)
  LadoA.sort(key=int)
  print(f'Lado inicial: {LadoA}.')
  print(f'Lado final: {LadoB}.')
  c = c + 1
  Ttotal = Ttotal + Tfica + Tvolta
  print(f'Tempo gasto: {Ttotal}!')
  print('*' * 30)

  while len(LadoA) == 2: #se só existem 2 pessoas do lado inicial, não é preciso escolher quem atravessará
    print(f'Passo {next+1}: As pessoas que atravessam em {LadoA[0]} e {LadoA[1]} minuto(s) cruzam a ponte.')
    LadoB.append(LadoA[0])
    del (LadoA[0])
    LadoB.append(LadoA[0])
    LadoB.sort(key=int)
    del (LadoA[0])
    Ttotal = Ttotal + LadoB[1]
    print(f'Lado inicial: {LadoA}.')
    print(f'Lado final: {LadoB}.')
    T = Ttotal + LadoB[1]
    print(f'Tempo gasto: {Ttotal}!')
    print('*' * 30)

if Ttotal <= tmax:
    print(f'A travessia foi feita dentro do prazo de {tmax} minuto(s) estipulado.')
else:
    print(f'A travessia não foi feita dentro do prazo de {tmax} minuto(s) estipulado.')

print('FIM!')


