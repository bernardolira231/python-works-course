import PySimpleGUI as sg

button_size = (7, 3)
PLAYER_ONE = "X"
PLAYER_TWO = "O"
current_player = PLAYER_ONE

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
             sg.Text("", key="-Winner-")
         ],
         [
             sg.Button("Close", key="-OK-")
         ]
         ]


def configure_layout():
    sg.Window("Demo", layout)


def close_game(event):
    event == sg.WIN_CLOSED or event == "-OK-"
    return


def create_deck(window, event, game_end):
    window.Element(event).ButtonText == "" and not game_end
    return


def init_deck(event, window):
    index = int(event.replace("-", ""))
    deck[index] = current_player
    window.Element(event).Update(text = current_player)
    return


def detect_winner_play(game_end):
    for winner_play in winner_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                print("El jugador 1 ha ganado!!!")
            else:
                print("El jugador 2 ha ganado!!!")
            game_end = True
    return game_end


def tie(game_end):
    if 0 not in deck:
        print("Ha terminado el juego! Nadie ha ganado")
        game_end = True
        return game_end


def change_current_player():
    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE


def main():
    window = configure_layout()
    game_end = False
    while True:
        event, values = window.read()
        if close_game(event):
            break
        if create_deck(window, event, game_end):
            init_deck(event, window)
        detect_winner_play(game_end)
        tie(game_end)
        change_current_player()

    window.close()


if __name__ == "__main__":
    main()
