import xml.etree.ElementTree as ET
from datetime import datetime

def listar_livros_disponiveis(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    print("Livros Disponíveis:")
    for book in root.find('books').findall('book'):
        if book.find('available').text == "true":
            print(f"ID: {book.get('id')}, Título: {book.find('title').text}, Autor: {book.find('author').text}")

def registrar_emprestimo(xml_file, book_id, reader_name):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Encontrar o livro e marcar como indisponível
    for book in root.find('books').findall('book'):
        if book.get('id') == str(book_id):
            if book.find('available').text == "true":
                book.find('available').text = "false"
                print(f"Livro '{book.find('title').text}' emprestado a {reader_name}.")
                
                # Criar novo empréstimo
                loan = ET.SubElement(root.find('loans'), 'loan')
                ET.SubElement(loan, 'bookId').text = str(book_id)
                ET.SubElement(loan, 'reader').text = reader_name
                ET.SubElement(loan, 'date').text = datetime.now().strftime('%Y-%m-%d')
                
                tree.write(xml_file)
                break
            else:
                print("Livro já está emprestado.")
                return

def consultar_historico(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    print("Histórico de Empréstimos:")
    for loan in root.find('loans').findall('loan'):
        book_id = loan.find('bookId').text
        reader = loan.find('reader').text
        date = loan.find('date').text

        # Procurar título do livro pelo ID
        for book in root.find('books').findall('book'):
            if book.get('id') == book_id:
                title = book.find('title').text
                print(f"Livro: {title}, Leitor: {reader}, Data: {date}")

def adicionar_novo_livro(xml_file, titulo, autor, ano):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Gerar um novo ID
    new_id = len(root.find('books').findall('book')) + 1

    # Criar novo livro
    new_book = ET.SubElement(root.find('books'), 'book', id=str(new_id))
    ET.SubElement(new_book, 'title').text = titulo
    ET.SubElement(new_book, 'author').text = autor
    ET.SubElement(new_book, 'year').text = str(ano)
    ET.SubElement(new_book, 'available').text = "true"

    tree.write(xml_file)
    print(f"Livro '{titulo}' adicionado com sucesso.")



