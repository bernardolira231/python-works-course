import PySimpleGUI as sg

button_size = (7, 3)
PLAYER_ONE = "X"
PLAYER_TWO = "O"
current_player = PLAYER_ONE

layout = [
         [
             sg.Button("", key="-1-", size=button_size),
             sg.Button("", key="-2-", size=button_size),
             sg.Button("", key="-3-", size=button_size)
         ],

         [
             sg.Button("", key="-4-", size=button_size),
             sg.Button("", key="-5-", size=button_size),
             sg.Button("", key="-6-", size=button_size)
         ],

         [
             sg.Button("", key="-7-", size=button_size),
             sg.Button("", key="-8-", size=button_size),
             sg.Button("", key="-9-", size=button_size)
         ],

          [sg.Button("Close", key="-OK-")]]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "-OK-":
        break

    if window.Element(event).ButtonText == "":
        window.Element(event).Update(text = current_player)

    if current_player == PLAYER_ONE:
        current_player = PLAYER_TWO
    else:
        current_player = PLAYER_ONE

window.close()
