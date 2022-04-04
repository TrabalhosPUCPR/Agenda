def menu():
    print("-"*50)
    print("1 - Cadastro")
    print("2 - Buscar")
    print("3 - Listar todos")
    print("4 - Deletar")
    print("5 - Alterar")
    print("-"*50)

def cadastro(agenda):
    try:
        nome = input("Digite o nome: ")
        telefone = int(input("Digite o telefone: "))
        email = input("Digite o email: ")
        agenda.append([nome, telefone, email])
    except:
        print("Digite algo valido")
    return agenda

def buscar(agenda):
    nome = [input("Digite o nome da pessoa que quer buscar: ")]
    encontrado = False
    print("-"*50)
    for i in range(len(agenda)):
        if any(palavra in agenda[i][0] for palavra in nome):
            if encontrado == False:
                encontrado = True
                print('-'*10, "Contatos encontrado", '-'*10,)
            print(f'Nome: {agenda[i][0]}, Telefone: {agenda[i][1]}, Email: {agenda[i][2]} ')
    if encontrado == False:
        print("Nao existe usuario com este nome")
    print("-"*50)

def lista(agenda):
    print("-"*50)
    for i in range(len(agenda)):
        print(f'Nome: {agenda[i][0]}, Telefone: {agenda[i][1]}, Email: {agenda[i][2]}, ')
    print("-"*50)

def deletar(agenda):
    nome = [input("Digite o nome da pessoa que deseja deletar: ")]
    for i in range(len(agenda)):
        if any(palavra in agenda[i][0] for palavra in nome):
            print(f'\nNome: {agenda[i][0]}, Telefone: {agenda[i][1]}, Email: {agenda[i][2]} ')
            esc = str(input("Deseja deletar este contato? (s/n): "))
            if esc == "s":
                print(f'Contato {agenda[i][0]} deletado com sucesso')
                agenda.remove(agenda[i])
                break
            else:
                break
    print("Usuario nao encontrado")

def alterar(agenda):
    nome = [input("Digite o nome da pessoa que deseja alterar: ")]
    for i in range(len(agenda)):
        if any(palavra in agenda[i][0] for palavra in nome):
            print(f'\nNome: {agenda[i][0]}, Telefone: {agenda[i][1]}, Email: {agenda[i][2]} ')
            esc = str(input("O que deseja alterar neste contato?: "))
            if esc == "nome":
                nome = str(input("Digite o novo nome para o contato: "))
                agenda[i][0] = nome
            elif esc == "telefone":
                while True:
                    try:
                        telefone = int(input("Digite o novo telefone para o contato: "))
                        break
                    except:
                        print("Digite um numero de telefone valido")
                agenda[i][1] = telefone      
            elif esc == "email":
                email = str(input("Digite o novo email para o contato: "))
                agenda[i][2] = email
            break


agenda = [["leofhgfgh", 543534, "gdffgddf"]]
while True:
    menu()
    esc = str(input("Digite a opcao: "))
    if esc == "1":
        cadastro(agenda)
    if esc == "2":
        buscar(agenda)
    if esc == "3":
        lista(agenda)
    if esc == "4":
        deletar(agenda)
    if esc == "5":
        alterar(agenda)









    

