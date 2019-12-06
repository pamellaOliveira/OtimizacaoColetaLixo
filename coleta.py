from pulp import *

print("Aqui você poderá ver qual a melhor opção para a coleta de lixo da sua cidade")
escolha = int(input("Se você deseja utilizar o cenário proposto por nós digite 1, se desejar inserir seus dados digite 0: "))
if escolha == 1:
    caminhao1 = 2000
    caminhao2 = 1500
    caminhao3 = 2000
    caminhao4 = 1500

    capacidadeCaminhao1 = 12000
    capacidadeCaminhao2 = 6000
    capacidadeCaminhao3 = 12000
    capacidadeCaminhao4 = 6000

    gari1 = 2
    gari2 = 4 
    gari3 = 3
    gari4 = 3

    totalGari = 10.0
    totalLixo = 24000.0
    totalCaminhao = 3.0
    
elif escolha == 0:
    print("Informe o valor que cada caminhão custará a prefeitura")
    caminhao1 = int(input("Digite o custo do primeiro caminhao "))
    caminhao2 = int(input("Digite o custo do segundo caminhao "))
    caminhao3 = int(input("Digite o custo do terceiro caminhao "))
    caminhao4 = int(input("Digite o custo do quarto caminhao "))
    print("-----------------------------------------------------------------------")
    capacidadeCaminhao1 = int(input("Digite a capacidade do primeiro caminhao "))
    capacidadeCaminhao2 = int(input("Digite a capacidade do segundo caminhao "))
    capacidadeCaminhao3 = int(input("Digite a capacidade do terceiro caminhao "))
    capacidadeCaminhao4 = int(input("Digite a capacidade do quarto caminhao "))
    print("-----------------------------------------------------------------------")
    
    gari1 = int(input("Digite a quantidade de garis necessaria para o caminhao 1 "))
    gari2 = int(input("Digite a quantidade de garis necessaria para o caminhao 2 "))
    gari3 = int(input("Digite a quantidade de garis necessaria para o caminhao 3 "))
    gari4 = int(input("Digite a quantidade de garis necessaria para o caminhao 4 "))

    totalCaminhao = int(input("Digite o valor de caminhões máximo de caminhões que você terá disponível "))
    totalLixo = int(input("Digite o total de lixo a ser coletado "))
    totalGari = int(input("Digite o total de garis disponíveis "))

else:
    print("valor incorreto")


TipoCaminhao = ['Caminhao1', 'Caminhao2', 'Caminhao3', 'Caminhao4']

custo = {'Caminhao1': caminhao1,
          'Caminhao2': caminhao2,
          'Caminhao3': caminhao3,
          'Caminhao4': caminhao4}

capacidadeCaminhao = {'Caminhao1': capacidadeCaminhao1,
          'Caminhao2': capacidadeCaminhao2,
          'Caminhao3': capacidadeCaminhao3,
          'Caminhao4': capacidadeCaminhao4}
 
garis = {'Caminhao1': gari1,
          'Caminhao2': gari2,
          'Caminhao3': gari3,
          'Caminhao4': gari4}


prob = LpProblem("Caminhoes de Lixo", LpMinimize)

tipoCaminhaoVars = LpVariable.dicts("Tipo",TipoCaminhao,0)
prob += lpSum([custo[i]*tipoCaminhaoVars[i] for i in TipoCaminhao])

prob += lpSum([tipoCaminhaoVars[i] for i in TipoCaminhao]) == totalCaminhao #Quantidade de caminhões
prob += lpSum([capacidadeCaminhao[i] * tipoCaminhaoVars[i] for i in TipoCaminhao]) >= totalLixo #Volume de lixo em quilos
prob += lpSum([garis[i] * tipoCaminhaoVars[i] for i in TipoCaminhao]) <= totalGari#total de garis disponiveis


prob.writeLP("lixo.lp")

prob.solve()

print ("Status:", LpStatus[prob.status])

for v in prob.variables():
    print (v.name, "=", v.varValue)

print ("Custo total sera de:", value(prob.objective))
