import Contato

def adicionar(lista):
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o numero do contato")
    
    contato = Contato(nome,numero)
    lista.append(contato)
    
    
def listar(listadecontatos):
    for contato in listadecontatos:
        print(contato.nome+" - "+contato.numero)
        