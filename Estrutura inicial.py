
usuarios = {
    "1": {"nome": "Matheus"},
    "2": {"nome": "Carlos"},
    "3": {"nome": "Paulo"},
    "4": {"nome": "Felipe"},
    "5": {"nome": "Agnaldo"},
}

livros = {
    "1": {"nome": "Dom Quixote", "emprestado": None},
    "2": {"nome": "Os Lusíadas", "emprestado": None},
    "3": {"nome": "Guerra e Paz", "emprestado": None},
    "4": {"nome": "Crime e Castigo", "emprestado": None},
    "5": {"nome": "A Divina Comédia", "emprestado": None},
}

def emprestar_livro():
    id_usuario = input("Qual o id do usuario: ")
    id_livro = input("Qual o id do livro: ")

    if id_usuario not in usuarios:
        print("Usuario nao existe!")
        return

    if id_livro not in livros:
        print("Livro nao existe!")
        return

    if livros[id_livro]["emprestado"] is not None:
        print("Livro já emprestado!")
        return

    livros[id_livro]["emprestado"] = id_usuario
    print("Livro emprestado!")

def devolver_livro():
    id_livro = input("Qual o id do livro: ")

    if id_livro not in livros:
        print("Livro nao existe!")
        return

    if livros[id_livro]["emprestado"] is None:
        print("Esse livro nao foi emprestado!")
        return

    nome_usuario = usuarios[livros[id_livro]["emprestado"]]["nome"]
    livros[id_livro]["emprestado"] = None

    print(f"Livro devolvido por {nome_usuario}!")

def cadastrar_usuario():
    nome = input("Qual seu nome: ")
    id_usuario = str(max(map(int, usuarios.keys())) + 1)
    usuarios[id_usuario] = {"nome": nome}
    print("Usuario cadastrado!")

def cadastrar_livro():
    livro = input("Qual o nome do livro: ")
    id_livro = str(max(map(int, livros.keys())) + 1)
    livros[id_livro] = {"nome": livro, "emprestado": None}
    print("Livro cadastrado!")

def lista_usuarios():
    print("\n===== LISTA DE USUARIOS =====\n")
    for id_usuario, dados in usuarios.items():
        print(f"Usuario: {id_usuario}")
        print(f"Nome: {dados['nome']}")
        print("-" * 40)

def lista_livros():
    print("\n===== LISTA DE LIVROS =====\n")
    for id_livro, dados in livros.items():
        status = "Disponivel"

        if dados["emprestado"] is not None:
            nome_usuario = usuarios[dados["emprestado"]]["nome"]
            status = f"Emprestado para {nome_usuario}"

        print(f"Livro: {id_livro}: {dados['nome']}")
        print(f"Status: {status}")
        print("-" * 40)

def menu():
    while True:
        print("\n===== SISTEMA BIBLIOTECA =====")
        print("1 - Cadastrar usuario")
        print("2 - Cadastrar livro")
        print("3 - Listar usuarios")
        print("4 - Listar livros")
        print("5 - Emprestar livro")
        print("6 - Devolver livro")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            cadastrar_livro()
        elif opcao == "3":
            lista_usuarios()
        elif opcao == "4":
            lista_livros()
        elif opcao == "5":
            emprestar_livro()
        elif opcao == "6":
            devolver_livro()
        elif opcao == "0":
            print("Sistema Fechado")
            break
        else:
            print("Opcao invalida!")
menu()
