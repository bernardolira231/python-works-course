import readchar
import os
import random
from random import randint

POS_X = 0
POS_Y = 1
NUM_OF_POKEMON_TRAINERS = 5
BAR_SIZE = 20
INITIAL_LIFE_OF_PIKACHU = 80
INITIAL_LIFE_OF_OTHER_POKEMON = 80

obstacle_definition = """\
############################
                    ########
########   ###      ########
#      #   ####      #######
#      ##           ########
#  ##  ##  ####     ########
#  #####            ########
#  #####           #########
#                  #########
#            ###############
#           ################
####            ############
########              ######
###########           ######
############################\
"""

my_position = [0,1]
map_trainers = []
other_pokemon = 1
pokemon_enemy = None
num_of_combats = 0

end_game = False
end_combat = False
died = False
win = False

life_of_pikachu = INITIAL_LIFE_OF_PIKACHU
life_of_other_pokemon = INITIAL_LIFE_OF_OTHER_POKEMON

# Create the obstacules
obstacle_definition = [list(row) for row in obstacle_definition.split('\n')]

MAP_WIDTH =len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

#Generate trainers in positions randoms
while len(map_trainers) < NUM_OF_POKEMON_TRAINERS:
    new_position = [random.randint(0,MAP_WIDTH - 1), random.randint(0,MAP_HEIGHT - 1)]

    if new_position not in map_trainers and new_position != my_position and \
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != '#':
            map_trainers.append(new_position)

# Main
while not end_game:

    os.system('clear')
    end_combat = False

    if other_pokemon == 1:
        pokemon_enemy = 'Squirtle'
    elif other_pokemon == 2:
        pokemon_enemy = 'Charmander'
    elif other_pokemon == 3:
        pokemon_enemy = 'Bulbasaur'
    elif other_pokemon == 4:
        pokemon_enemy = 'Pidgey'
    elif other_pokemon == 5:
        pokemon_enemy = 'Rattata'

    #Draw map
    print('+' + '-' * MAP_WIDTH * 2 + '+')

    for coordinate_y in range(MAP_HEIGHT):
        print('|', end='')
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = '  '
            trainer_in_cell = None

            for map_trainer in map_trainers:
                if map_trainer[POS_X] == coordinate_x and map_trainer[POS_Y] == coordinate_y:
                    char_to_draw = ' *'
                    trainer_in_cell = map_trainer

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = ' @'

                if trainer_in_cell:
                    map_trainers.remove(trainer_in_cell)

                    os.system('clear')
                    print('Incia el combate Pokemon\n Tu sacas a Pikachu')
                    print('Tu enemigo saca a {}'.format(pokemon_enemy))

                    # Start combat
                    while not end_combat:
                        if life_of_pikachu <= 0:
                            life_of_pikachu = 0
                        elif life_of_other_pokemon <= 0:
                            life_of_other_pokemon = 0

                        # Pikachu Turn
                        print('Es turno de tu Pikachu')
                        pikachu_attack = None

                        while pikachu_attack not in ['I', 'R', 'B', 'C', 'S']:
                            pikachu_attack = input('Que ataque deseas realizar? [I]mpactrueno, [R]ayo, [B]ola voltio, [C]ola Ferrea, [S]altar turno: ')
                            if pikachu_attack == 'I':
                                # Impactrueno
                                print('Has usado Impactrueno')
                                life_of_other_pokemon -= 10

                            elif pikachu_attack == 'R':
                                # Rayo
                                print('Has usado Rayo')
                                life_of_other_pokemon -= 20

                            elif pikachu_attack == 'B':
                                # Bola voltio
                                print('Has usado Bola Voltio')
                                life_of_other_pokemon -= 15

                            elif pikachu_attack == 'C':
                                # Cola Ferrea
                                print('Has usado Cola Ferrea')
                                life_of_other_pokemon -= 8

                            elif pikachu_attack == 'S':
                                # Saltar ataque
                                print('Has saltado tu turno')

                            else:
                                print('No has escogido ningun ataque pierdes el turno')

                            if life_of_pikachu <= 0:
                                life_of_pikachu = 0
                            elif life_of_other_pokemon <= 0:
                                life_of_other_pokemon = 0

                            life_bar_pikachu = int(life_of_pikachu * BAR_SIZE / INITIAL_LIFE_OF_PIKACHU)
                            life_bar_other_pokemon = int(life_of_other_pokemon * BAR_SIZE / INITIAL_LIFE_OF_OTHER_POKEMON)

                            print('Pikachu: [{}{}] ({}/{})'.format('*' * life_bar_pikachu, ' '*(BAR_SIZE - life_bar_pikachu),
                                                                   life_of_pikachu, INITIAL_LIFE_OF_PIKACHU))
                            print('{}: [{}{}] ({}/{})'.format(pokemon_enemy, '*' * life_bar_other_pokemon, ' '*(BAR_SIZE - life_bar_other_pokemon),
                                                              life_of_other_pokemon, INITIAL_LIFE_OF_OTHER_POKEMON))

                            if life_of_pikachu <= 0:
                                life_of_pikachu = 0
                            elif life_of_other_pokemon <= 0:
                                life_of_other_pokemon = 0

                            if life_of_other_pokemon == 0:
                                print('Has ganado')
                                print('Enter para continuar...')
                                end_combat = True
                                life_of_other_pokemon = 80
                                life_of_pikachu = 80
                                other_pokemon += 1
                                num_of_combats += 1
                                break
                            elif life_of_pikachu == 0:
                                print('Has perdido')
                                input('Enter para continuar...')
                                end_combat = True
                                end_game = True
                                died = True
                                break

                            input('Enter para continuar...')
                            os.system('clear')

                            # Turn of other pokemon enemy
                            if pokemon_enemy == 'Squirtle':
                                print('Es turno de Squirtle')
                                squirtle_attack = randint(1, 4)
                                if squirtle_attack == 1:
                                    print('Squirtle enemigo ha usado Pistola Agua')
                                    life_of_pikachu -= 10
                                elif squirtle_attack == 2:
                                    print('Squirtle enemigo ha usado Hidropulso')
                                    life_of_pikachu -= 20
                                elif squirtle_attack == 3:
                                    print('Squirtle enemigo ha usado Salmuera')
                                    life_of_pikachu -= 15
                                elif squirtle_attack == 4:
                                    print('Squirtle enemigo ha usado Burbujas')
                                    life_of_pikachu -= 8

                            elif pokemon_enemy == 'Charmander':
                                print('Es turno de Charmander')
                                charmander_attack = randint(1, 4)
                                if charmander_attack == 1:
                                    print('Charmander enemigo ha usado Lanzallamas')
                                    life_of_pikachu -= 10
                                elif charmander_attack == 2:
                                    print('Charmander enemigo ha usado Infierno')
                                    life_of_pikachu -= 20
                                elif charmander_attack == 3:
                                    print('Charmander enemigo ha usado Furia Dragon')
                                    life_of_pikachu -= 15
                                elif charmander_attack == 4:
                                    print('Charmander enemigo ha usado Ascuas')
                                    life_of_pikachu -= 8

                            elif pokemon_enemy == 'Bulbasaur':
                                print('Es turno de Bulbasaur')
                                bulbasaur_attack = randint(1, 4)
                                if bulbasaur_attack == 1:
                                    print('Bulbasaur enemigo ha usado Hoja Afilada')
                                    life_of_pikachu -= 10
                                elif bulbasaur_attack == 2:
                                    print('Bulbasaur enemigo ha usado Bomba Germen')
                                    life_of_pikachu -= 20
                                elif bulbasaur_attack == 3:
                                    print('Bulbasaur enemigo ha usado Doble Filo')
                                    life_of_pikachu -= 15
                                elif bulbasaur_attack == 4:
                                    print('Bulbasaur enemigo ha usado Latigo Cepa')
                                    life_of_pikachu -= 8

                            elif pokemon_enemy == 'Pidgey':
                                print('Es turno de Pidgey')
                                pidgey_attack = randint(1, 4)
                                if pidgey_attack == 1:
                                    print('Pidgey enemigo ha usado Ataque Ala')
                                    life_of_pikachu -= 10
                                elif pidgey_attack == 2:
                                    print('Pidgey enemigo ha usado Vendaval')
                                    life_of_pikachu -= 20
                                elif pidgey_attack == 3:
                                    print('Pidgey enemigo ha usado Tajo Aereo')
                                    life_of_pikachu -= 15
                                elif pidgey_attack == 4:
                                    print('Pidgey enemigo ha usado Ciclon')
                                    life_of_pikachu -= 8

                            elif pokemon_enemy == 'Rattata':
                                print('Es turno de Rattata')
                                rattata_attack = randint(1, 4)
                                if rattata_attack == 1:
                                    print('Rattata enemigo ha usado Buena Baza')
                                    life_of_pikachu -= 10
                                elif rattata_attack == 2:
                                    print('Rattata enemigo ha usado Golpe Bajo')
                                    life_of_pikachu -= 20
                                elif rattata_attack == 3:
                                    print('Rattata enemigo ha usado Triturar')
                                    life_of_pikachu -= 15
                                elif rattata_attack == 4:
                                    print('Rattata enemigo ha usado Mordisco')
                                    life_of_pikachu -= 8

                            if life_of_pikachu <= 0:
                                life_of_pikachu = 0
                            elif life_of_other_pokemon <= 0:
                                life_of_other_pokemon = 0

                            life_bar_pikachu = int(life_of_pikachu * BAR_SIZE / INITIAL_LIFE_OF_PIKACHU)
                            life_bar_other_pokemon = int(life_of_other_pokemon * BAR_SIZE / INITIAL_LIFE_OF_OTHER_POKEMON)

                            print('Pikachu: [{}{}] ({}/{})'.format('*' * life_bar_pikachu, ' '*(BAR_SIZE - life_bar_pikachu),
                                                                   life_of_pikachu, INITIAL_LIFE_OF_PIKACHU))
                            print('{}: [{}{}] ({}/{})'.format(pokemon_enemy, '*' * life_bar_other_pokemon, ' '*(BAR_SIZE - life_bar_other_pokemon),
                                                              life_of_other_pokemon, INITIAL_LIFE_OF_OTHER_POKEMON))

                            if life_of_other_pokemon == 0:
                                print('Has ganado')
                                input('Enter para continuar...')
                                end_combat = True
                                life_of_other_pokemon = 80
                                life_of_pikachu = 80
                                other_pokemon += 1
                                num_of_combats += 1
                                break
                            elif life_of_pikachu == 0:
                                print('Has perdido')
                                input('Enter para continuar...')
                                end_combat = True
                                end_game = True
                                died = True
                                break

                            input('Enter para continuar...')
                            os.system('clear')

            if obstacle_definition [coordinate_y][coordinate_x] == '#':
                char_to_draw = '##'

            print('{}'.format(char_to_draw), end='')
        print('|')
    print('+' + '-' * MAP_WIDTH * 2 + '+')

    # User moves
    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == 's':
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == 'd':
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == 'x':
        end_game = True
        os.system('clear')

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != '#':
            my_position = new_position

    if num_of_combats == 5:
        win = True
        end_game = True

if (win == True):
    print('Has ganado a todos los entrenadores eres el campeon pokemon')

if (died == True):
    print('Te han ganado has muerto')
