import PySimpleGUI as sg

button_size = (7, 3)
deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

layout = [
         [
             sg.Button("", key="-0-", size=button_size),
             sg.Button("", key="-1-", size=button_size),
             sg.Button("", key="-2-", size=button_size)
         ],

         [
             sg.Button("", key="-3-", size=button_size),
             sg.Button("", key="-4-", size=button_size),
             sg.Button("", key="-5-", size=button_size)
         ],

         [
             sg.Button("", key="-6-", size=button_size),
             sg.Button("", key="-7-", size=button_size),
             sg.Button("", key="-8-", size=button_size)
         ],
         [
             sg.Button("Close", key="-OK-")
         ]
         ]


def close_window(event):
    return event == sg.WIN_CLOSED or event == "-OK-"


def place_marks(window, event, current_player):
    if window.Element(event).ButtonText == "":
        index = int(event.replace("-", ""))
        deck[index] = current_player
        window.Element(event).Update(text=current_player)


def check_if_someone_won(PLAYER_ONE):
    for winner_play in winner_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                print("El jugador 1 ha ganado!!!")
            else:
                print("El jugador 2 ha ganado!!!")


def check_for_a_tie():
    if 0 not in deck:
        print("Ha terminado el juego! Nadie ha ganado")


def change_current_player(current_player, PLAYER_ONE, PLAYER_TWO):
    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE


def main():
    PLAYER_ONE = "X"
    PLAYER_TWO = "O"
    current_player = PLAYER_ONE
    window = sg.Window("Gato", layout)
    while True:
        event, value = window.read()
        if close_window(event):
            break
        place_marks(window, event, current_player)
        check_if_someone_won(PLAYER_ONE)
        check_for_a_tie()
        change_current_player(current_player, PLAYER_ONE, PLAYER_TWO)
    window.close()


if __name__ == "__main__":
    main()
