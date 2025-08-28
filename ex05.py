#5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".#

livros = ["Ideias Para Adiar O Fim do Mundo", "O Lugar Onde a Terra Descansa", "A Queda do Céu"]
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print("Livro removido com sucesso!")
else:
    print("Livro não encontrado")