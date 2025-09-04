
def mostrar_lista(lista):
    """Mostra a lista de compras"""
    print("\n--- SUA LISTA DE COMPRAS ---")
    if not lista:
        print("Lista vazia! Adicione alguns itens.")
    else:
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
    print("----------------------------")


def main():
    lista_compras = []

    print("BEM-VINDO À LISTA DE COMPRAS!")
    print("Digite 'sair' para encerrar")
    print("Digite 'mostrar' para ver a lista")
    print("Digite 'remover' para apagar um item")
    print("------------------------------------")

    while True:
        item = input("\nO que você quer adicionar? ").strip()

        if item.lower() == 'sair':
            break

        elif item.lower() == 'mostrar':
            mostrar_lista(lista_compras)

        elif item.lower() == 'remover':
            if not lista_compras:
                print(" Lista vazia!")
            else:
                mostrar_lista(lista_compras)
                try:
                    numero = int(input("Qual número quer remover? "))
                    if 1 <= numero <= len(lista_compras):
                        removido = lista_compras.pop(numero - 1)
                        print(f"'{removido}' removido com sucesso!")
                    else:
                        print("Número inválido!")
                except ValueError:
                    print("Digite um número válido!")

        elif item:
            lista_compras.append(item)
            print(f"'{item}' adicionado à lista!")

        else:
            print("Digite algo ou 'sair' para encerrar")


    print("\n LISTA FINAL DE COMPRAS:")
    mostrar_lista(lista_compras)


if __name__ == "__main__":
    main()