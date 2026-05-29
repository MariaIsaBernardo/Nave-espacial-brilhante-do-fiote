#Definir as variaveis
combustivel = 110
tripulantes = []

##Definir funções

def viajar ():
    global combustivel
    if (combustivel >= 30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else :
        print ("Você está sem combustível o suficiente. Abasteça!")

def abastecer():
    global combustivel
    combustivel = 110
    print("Tanque Cheio! 🛢️")

def status_nave():
   print("\n-------- Status Da Nave --------")
   print(f"Temos {combustivel} de combustível")
   print(f"Os tripulantes são: {tripulantes}")
   print("----------------------------- \n")

def registrarTripulantes():
    novoTripulante = input("Qual o nome do novo tripulante?: ")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido com sucesso! 🚀")

while True:
    print("\nBem vindo ao menu interativo da nave espacial. Por favor selecione uma opção:")
    print ("\n1-Mostrar status da nave | 2-Viajar | 3-Abastecer | 4-Novo tripulante | 5-Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registrarTripulantes()
    elif (opcao == "5"):
        print("Viagem encerrada!")
        break
        
#status_nave()
#registrarTripulantes()
#status_nave()