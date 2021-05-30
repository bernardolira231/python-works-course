# Progama Lista de la Compra
print('Progama lista de la compra')

lista_de_la_compra = []
necesario = input('Que deseas comprar? (Q para salir): ')

while necesario != "Q":
    if necesario not in lista_de_la_compra:
        lista_de_la_compra.append(necesario)
        opcion = input('Seguro que quiere poner {}? [S/N]: '.format(necesario))
        if opcion == 'S' or 's':
            print('Se ha puesto {} en la lista de la compra\n'.format(necesario))
        else:
            print('No se pondra {} en la lista\n'.format(necesario))
        necesario = input('Que deseas comprar? (Q para salir): ')
    elif necesario in lista_de_la_compra:
        print('{} ya esta en la lista!\n'.format(necesario))
        necesario = input('Que deseas comprar? (Q para salir): ')

print('La lista de la compra es \n {}'.format(lista_de_la_compra))
