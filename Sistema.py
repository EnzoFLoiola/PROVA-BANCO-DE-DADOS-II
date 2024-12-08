from BancoDeDadosXML import listar_livros_disponiveis, registrar_emprestimo, consultar_historico, adicionar_novo_livro

print("-" * 10 + " BIBLIOTECA FACULDADE R SÁ " + "-" * 10)
print(" " * 12 + " BEM VINDO, ALUNO " + " " * 12)

controle = 0

while(controle != 5):

    print("--" * 24)
    print("""
    1 - LISTAR LIVROS DISPONIVEIS
    2 - REGISTRAR EMPRESTIMO
    3 - CONSULTAR HISTORICO
    4 - ADICIONAR LIVRO
    5 - SAIR
    """)
    print("--" * 24)

    controle = int(input("DIGITE A OPÇÃO: "))

    if(controle == 1):
        listar_livros_disponiveis("PROVA-BANCO-DE-DADOS-II/library.xml")
        input()

    if(controle == 2):
        reader = input("DIGITE O NOME DO LEITOR: ")
        id_livro = input("DIGITE O ID DO LIVRO: ")
        registrar_emprestimo("PROVA-BANCO-DE-DADOS-II/library.xml", id_livro, reader)
        input()

    
    if(controle == 3):
        consultar_historico("PROVA-BANCO-DE-DADOS-II/library.xml")
        input()


    if(controle == 4):
        titulo = input("DIGITE O TITULO DO LIVRO: ")
        autor = input("DIGITE O NOME DO AUTOR: ")
        ano = input("DIGITE O ANO DE PUBLICAÇÃO: ")
        adicionar_novo_livro("PROVA-BANCO-DE-DADOS-II/library.xml",titulo, autor, ano)
        input()


print("--" * 12 + " SISTEMA ENCERRADO, ATÉ A PRÓXIMA " + "--" * 12)
