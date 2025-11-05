import os

print("Bem Vindo a YMarinhoTech!")
nome = input("Qual seu nome? ")
lista = {}

def salvar_em_arquivo():
    caminho = os.path.join(os.path.dirname(__file__), "gastos_salvos.txt")
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Relatório de gastos - Usuário: {nome}\n\n")
        if not lista:
            arquivo.write("Nenhuma lista cadastrada.\n")
        else:
            for minha_lista, valores in lista.items():
                arquivo.write(f"Lista: {minha_lista}\n")
                for v in valores:
                    arquivo.write(f"  - R$ {v:.2f}\n")
                arquivo.write(f"  Total: R$ {sum(valores):.2f}\n\n")

while True:
    print()
    start = int(input(f"bem vindo {nome}, vamos iniciar nosso serviço:\n1 - Criar lista\n2 - Acessar listas existentes\n3 - Mostrar todas\n4 - Sair e salvar\n5 - Salvar agora\n- "))
    if start == 1:
        minha_lista = str(input("insira o nome de sua lista:\n- ")).strip().lower()
        if minha_lista not in lista:
            lista[minha_lista] = []
            print(f"Adicionamos a lista chamada: {minha_lista} com sucesso!")
        elif minha_lista in lista:
            print(f"{minha_lista} já esta criada!")
            continue

    elif start == 2:
        if not lista:
            print("Não existe nenhuma lista cadastrada!")
            continue
        minha_lista = input("insira o nome de sua lista:\n- ").strip().lower()
        if minha_lista not in lista:
            print(f"{minha_lista}, é inexistente")
            continue
        #MENU DA PARTE 2
        while True:
            print()
            print(f"Lista atual é: {lista}")
            opções = int(input("1 - Adicionar gastos\n2 - Remover gastos\n3 - Ver gastos totais\n4 - Voltar\nEscolha: "))
            if opções == 1:
                try:
                    valor = float(input("Digite o valor do gasto: R$ ").replace(",","."))
                    lista[minha_lista].append(valor)
                    print(f"Gasto de R${valor:.2f} adicionado com sucesso!")
                except ValueError:
                    print("Você devia ter colocado numeros!")
                
            elif opções == 2:
                print(f"gastos atuais: {lista[minha_lista]}")
                try:
                    valor = float(input("Digite o valor do gasto: R$ ").replace(",","."))
                    if valor in lista[minha_lista]:
                        lista[minha_lista].remove(valor)
                        print(f"Gasto de R$ {valor:.2f} removido com sucesso!")
                    else:
                        print("Valor não está na lista")
                except ValueError:
                    print("Você devia ter colocado numeros!")

            elif opções == 3:
                soma = sum(lista[minha_lista])
                print(f"gastos totais em {minha_lista} é igual a R${soma:.2f}")
            
            elif opções == 4:
                print("retornando ao menu principal")
                break
            else:
                print("Opção invalida, tente novamente!")
    
    elif start == 3:
        if not lista:
            print("Não existe nenhuma lista cadastrada!")
        else:
            for minha_lista, valor in lista.items():
                print(f"- {minha_lista.capitalize()}: {len(valor)} gastos | Total R$ {sum(valor):.2f}")
        print()
    
    elif start == 4:
        salvar_em_arquivo()
        print("Ok, até a proxima!")
        break
    
    elif start == 5:
        salvar_em_arquivo()

    else:
        print("opção Invalida!")