import random
import os
from pprint import pprint
from pokeload import get_all_pokemons

BAR_SIZE = 20

def get_player_profile(pokemon_list):
    return {
        "player_name": input("¿Cuál es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_healt"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elige con que pokemon lucharás")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("¿Cuál eliges?: "))]
        except (ValueError, IndexError):
            print("Opción inválida")


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}/{}".format(pokemon["name"],
                                           pokemon["level"],
                                           pokemon["current_healt"],
                                           pokemon["base_healt"])


def player_table_type(player_pokemon, option, enemy_pokemon):
    if player_pokemon["attacks"][option]["type"].upper() == "LUCHA" or player_pokemon["attacks"][option]["type"].upper() == "FUEGO" or player_pokemon["attacks"][option]["type"].upper() == "TIERRA" and enemy_pokemon["type"].upper() == "ACERO":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "AGUA" or player_pokemon["attacks"][option]["type"].upper() == "PLANTA" or player_pokemon["attacks"][option]["type"].upper() == "LUCHA" or player_pokemon["attacks"][option]["type"].upper() == "ACERO" and enemy_pokemon["type"].upper() == "ROCA":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "HIELO" or player_pokemon["attacks"][option]["type"].upper() == "DRAGON" and enemy_pokemon["type"].upper() == "DRAGON":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "FUEGO" or player_pokemon["attacks"][option]["type"].upper() == "VOLADOR"or player_pokemon["attacks"][option]["type"].upper() == "ROCA" and enemy_pokemon["type"].upper() == "BICHO":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "LUCHA" and enemy_pokemon["type"].upper() == "NORMAL":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "AGUA" or player_pokemon["attacks"][option]["type"].upper() == "TIERRA" or player_pokemon["attacks"][option]["type"].upper() == "ROCA" and enemy_pokemon["type"].upper() == "FUEGO":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "PLANTA" or player_pokemon["attacks"][option]["type"].upper() == "ELECTRICO" and enemy_pokemon["type"].upper() == "AGUA":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "TIERRA" and enemy_pokemon["type"].upper() == "ELECTRICO":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "FUEGO" or player_pokemon["attacks"][option]["type"].upper() == "LUCHA" or player_pokemon["attacks"][option]["type"].upper() == "ROCA" or player_pokemon["attacks"][option]["type"].upper() == "ACERO" and enemy_pokemon["type"].upper() == "HIELO":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "HIELO" or player_pokemon["attacks"][option]["type"].upper() == "PSIQUICO" and enemy_pokemon["type"].upper() == "LUCHA":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "TIERRA" or player_pokemon["attacks"][option]["type"].upper() == "PSIQUICO" and enemy_pokemon["type"].upper() == "VENENO":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "AGUA" or player_pokemon["attacks"][option]["type"].upper() == "PLANTA" or player_pokemon["attacks"][option]["type"].upper() == "HIELO" and enemy_pokemon["type"].upper() == "TIERRA":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "ELECTRICO" or player_pokemon["attacks"][option]["type"].upper() == "HIELO" or player_pokemon["attacks"][option]["type"].upper() == "ROCA" and enemy_pokemon["type"].upper() == "VOLADOR":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "BICHO" or player_pokemon["attacks"][option]["type"].upper() == "FANTASMA" or player_pokemon["attacks"][option]["type"].upper() == "SINIESTRO" and enemy_pokemon["type"].upper() == "PSIQUICO":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "FANTASMA" or player_pokemon["attacks"][option]["type"].upper() == "SINIESTRO" or player_pokemon["attacks"][option]["type"].upper() == "SINIESTRO" and enemy_pokemon["type"].upper() == "FANTASMA":
        return 2
    elif player_pokemon["attacks"][option]["type"].upper() == "LUCHA" or player_pokemon["attacks"][option]["type"].upper() == "BICHO" and enemy_pokemon["type"].upper() == "SINIESTRO":
        return 2
    else:
        return 1


def player_attack(player_pokemon, enemy_pokemon):
    cont = 0
    for attack in player_pokemon["attacks"]:
        if int(attack["min_level"]) <= int(player_pokemon["level"]) and attack["damage"] != 0:
            print("{}.- {}".format(cont, attack["name"]),
                  "Tipo: {}".format(attack["type"].upper()),
                  "Daño: {}".format(attack["damage"]))
            cont += 1
    option = int(input("Que ataque deseas realizar? (1, 2, 3, etc): "))
    while option > cont:
        print("Opción inválida")
        option = int(input("Que ataque deseas realizar? (1, 2, 3, etc): "))
    if option <= cont and option >= 0:
        if player_pokemon["attacks"][option]["damage"] == 0:
            del(player_pokemon["attacks"][option])
        print("Has usado {} y le has quitado {} hp".format(player_pokemon["attacks"][option]["name"], player_pokemon["attacks"][option]["damage"]))
        enemy_pokemon["current_healt"] -= player_pokemon["attacks"][option]["damage"] * player_table_type(player_pokemon, option, enemy_pokemon)


def enemy_table_type(attack_enemy, player_pokemon):
    if attack_enemy["type"].upper() == "LUCHA" or attack_enemy["type"].upper() == "FUEGO" or attack_enemy["type"].upper() == "TIERRA" and player_pokemon["type"].upper() == "ACERO":
        return 2
    elif attack_enemy["type"].upper() == "AGUA" or attack_enemy["type"].upper() == "PLANTA" or attack_enemy["type"].upper() == "LUCHA" or attack_enemy["type"].upper() == "ACERO" and player_pokemon["type"].upper() == "ROCA":
        return 2
    elif attack_enemy["type"].upper() == "HIELO" or attack_enemy["type"].upper() == "DRAGON" and player_pokemon["type"].upper() == "DRAGON":
        return 2
    elif attack_enemy["type"].upper() == "FUEGO" or attack_enemy["type"].upper() == "VOLADOR"or attack_enemy["type"].upper() == "ROCA" and player_pokemon["type"].upper() == "BICHO":
        return 2
    elif attack_enemy["type"].upper() == "LUCHA" and player_pokemon["type"].upper() == "NORMAL":
        return 2
    elif attack_enemy["type"].upper() == "AGUA" or attack_enemy["type"].upper() == "TIERRA" or attack_enemy["type"].upper() == "ROCA" and player_pokemon["type"].upper() == "FUEGO":
        return 2
    elif attack_enemy["type"].upper() == "PLANTA" or attack_enemy["type"].upper() == "ELECTRICO" and player_pokemon["type"].upper() == "AGUA":
        return 2
    elif attack_enemy["type"].upper() == "TIERRA" and player_pokemon["type"].upper() == "ELECTRICO":
        return 2
    elif attack_enemy["type"].upper() == "FUEGO" or attack_enemy["type"].upper() == "LUCHA" or attack_enemy["type"].upper() == "ROCA" or attack_enemy["type"].upper() == "ACERO" and player_pokemon["type"].upper() == "HIELO":
        return 2
    elif attack_enemy["type"].upper() == "HIELO" or attack_enemy["type"].upper() == "PSIQUICO" and player_pokemon["type"].upper() == "LUCHA":
        return 2
    elif attack_enemy["type"].upper() == "TIERRA" or attack_enemy["type"].upper() == "PSIQUICO" and player_pokemon["type"].upper() == "VENENO":
        return 2
    elif attack_enemy["type"].upper() == "AGUA" or attack_enemy["type"].upper() == "PLANTA" or attack_enemy["type"].upper() == "HIELO" and player_pokemon["type"].upper() == "TIERRA":
        return 2
    elif attack_enemy["type"].upper() == "ELECTRICO" or attack_enemy["type"].upper() == "HIELO" or attack_enemy["type"].upper() == "ROCA" and player_pokemon["type"].upper() == "VOLADOR":
        return 2
    elif attack_enemy["type"].upper() == "BICHO" or attack_enemy["type"].upper() == "FANTASMA" or attack_enemy["type"].upper() == "SINIESTRO" and player_pokemon["type"].upper() == "PSIQUICO":
        return 2
    elif attack_enemy["type"].upper() == "FANTASMA" or attack_enemy["type"].upper() == "SINIESTRO" or attack_enemy["type"].upper() == "SINIESTRO" and player_pokemon["type"].upper() == "FANTASMA":
        return 2
    elif attack_enemy["type"].upper() == "LUCHA" or attack_enemy["type"].upper() == "BICHO" and player_pokemon["type"].upper() == "SINIESTRO":
        return 2
    else:
        return 1


def enemy_attack(enemy_pokemon, player_pokemon):
    attack_enemy = random.choice(enemy_pokemon["attacks"])
    while int(attack_enemy["min_level"]) > enemy_pokemon["level"] and attack_enemy["damage"] == 0:
        attack_enemy = random.choice(enemy_pokemon["attacks"])
    print("El {} ha usado {} y ha quitado {} hp".format(enemy_pokemon["name"], attack_enemy["name"], attack_enemy["damage"]))
    player_pokemon["current_healt"] -= attack_enemy["damage"] * enemy_table_type(attack_enemy, player_pokemon)


def assign_expirence(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

        while pokemon["current_exp"] > 20:
            pokemon["current_exp"] -= 20
            pokemon["level"] += 1
            pokemon["current_healt"] = pokemon["base_healt"]
            print("Tu pokemon ha subido al nivel {}".format(get_pokemon_info(pokemon)))


def catch_pokemon(enemy_pokemon, player_profile):
    catch_or_no = 0
    if enemy_pokemon["current_healt"] <= 25:
        catch_or_no = random.randint(1, 5)
    elif enemy_pokemon["current_healt"] > 25:
        catch_or_no = random.randint(1, 10)
    if catch_or_no == 2 or catch_or_no == 5:
        print("Has capturado ha {}".format(enemy_pokemon["name"]))
        player_profile["pokemon_inventory"] + [enemy_pokemon]
        enemy_pokemon["current_healt"] = 0
    else:
        print("{} no ha sido capturado".format(enemy_pokemon["name"]))


def cure_healt():
    pass


def life_bar(player_pokemon, enemy_pokemon):
    life_bar_player_pokemon = int(player_pokemon["current_healt"] * BAR_SIZE / player_pokemon["base_healt"])
    life_bar_enemy_pokemon = int(enemy_pokemon["current_healt"] * BAR_SIZE / enemy_pokemon["base_healt"])
    print("{}: [{}{}] ({}/{})".format(player_pokemon["name"], "*" * life_bar_player_pokemon, " "*(BAR_SIZE - life_bar_player_pokemon), player_pokemon["current_healt"], player_pokemon["base_healt"]))
    print("{}: [{}{}] ({}/{})".format(enemy_pokemon["name"], "*" * life_bar_enemy_pokemon, " "*(BAR_SIZE - life_bar_enemy_pokemon), enemy_pokemon["current_healt"], enemy_pokemon["base_healt"]))


def fight(player_profile, enemy_pokemon):
    print("---NUEVO COMBATE---")

    attack_history = []
    print("Oh un {} salvaje aparecio".format(get_pokemon_info(enemy_pokemon)))

    player_pokemon = choose_pokemon(player_profile)

    print("Tu sacas ah {}".format(get_pokemon_info(player_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_healt"] > 0:
        action = None
        while action not in ["A", "P", "V", "C"]:
            action = input("Que deseas hacer: [A]tacar, [P]okeball, Poción de [Vida], [C]ambiar: ")
            os.system("clear")

        if action == "A":
            player_attack(player_pokemon, enemy_pokemon)
            attack_history.append(player_pokemon)
            if enemy_pokemon["current_healt"] < 0:
                enemy_pokemon["current_healt"] = 0
            if player_pokemon["current_healt"] < 0:
                player_pokemon["current_healt"] = 0
            life_bar(player_pokemon, enemy_pokemon)
        elif action == "P":
            catch_pokemon(enemy_pokemon, player_profile)
            if enemy_pokemon["current_healt"] == 0:
                break
        elif action == "V":
            cure_healt()
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)
            print("Tu sacas ah {}".format(get_pokemon_info(player_pokemon)))

        input("Enter para continuar...")
        os.system("clear")

        enemy_attack(enemy_pokemon, player_pokemon)

        if enemy_pokemon["current_healt"] < 0:
            enemy_pokemon["current_healt"] = 0
        if player_pokemon["current_healt"] < 0:
            player_pokemon["current_healt"] = 0

        life_bar(player_pokemon, enemy_pokemon)

        input("Enter para continuar...")
        os.system("clear")

    if player_pokemon["current_healt"] == 0 and any_player_pokemon_lives(player_profile):
        player_pokemon = choose_pokemon(player_profile)

    if enemy_pokemon["current_healt"] == 0:
        print("Has ganado!")
        assign_expirence(attack_history)
        player_profile["combats"] += 1

    print("---FIN DEL COMBATE---")
    input("Presiona ENTER para continuar")
    os.system("clear")


def item_lotery(player_profile):
    random_number = random.randint(1, 4)
    if random_number == 2:
        print("Oh has ganado una pokeball")
        player_profile["pokeballs"] += 1
    elif random_number == 4:
        print("Oh has ganado una poción")
        player_profile["health_potion"] += 1


def get_enemy_pokemon_level(player_profile, enemy_pokemon):
    sum_of_levels = sum([pokemon["level"] for pokemon in player_profile["pokemon_inventory"]])
    if sum_of_levels < 5:
        enemy_pokemon["level"] = random.randint(1, 7)
    elif sum_of_levels < 10:
        enemy_pokemon["level"] = random.randint(5, 12)
    elif sum_of_levels < 15:
        enemy_pokemon["level"] = random.randint(10, 17)
    elif sum_of_levels < 20:
        enemy_pokemon["level"] = random.randint(15, 22)
    elif sum_of_levels < 25:
        enemy_pokemon["level"] = random.randint(20, 27)
    elif sum_of_levels < 30:
        enemy_pokemon["level"] = random.randint(25, 32)
    elif sum_of_levels < 35:
        enemy_pokemon["level"] = random.randint(30, 37)
    elif sum_of_levels < 40:
        enemy_pokemon["level"] = random.randint(35, 42)
    elif sum_of_levels < 45:
        enemy_pokemon["level"] = random.randint(40, 47)
    elif sum_of_levels < 50:
        enemy_pokemon["level"] = random.randint(45, 52)
    elif sum_of_levels < 55:
        enemy_pokemon["level"] = random.randint(50, 57)
    elif sum_of_levels < 60:
        enemy_pokemon["level"] = random.randint(55, 62)
    elif sum_of_levels < 65:
        enemy_pokemon["level"] = random.randint(60, 67)
    elif sum_of_levels < 70:
        enemy_pokemon["level"] = random.randint(65, 72)
    elif sum_of_levels < 75:
        enemy_pokemon["level"] = random.randint(70, 77)
    elif sum_of_levels < 80:
        enemy_pokemon["level"] = random.randint(75, 82)
    elif sum_of_levels < 85:
        enemy_pokemon["level"] = random.randint(80, 87)
    elif sum_of_levels < 90:
        enemy_pokemon["level"] = random.randint(85, 92)
    elif sum_of_levels < 105:
        enemy_pokemon["level"] = random.randint(90, 107)


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        get_enemy_pokemon_level(player_profile, enemy_pokemon)
        fight(player_profile, enemy_pokemon)
        item_lotery(player_profile)

    print("Has perdido en el combate n{}".format(player_profile["combats"] + 1))


if __name__ == "__main__":
    main()
