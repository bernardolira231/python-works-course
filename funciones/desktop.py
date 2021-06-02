import PySimpleGUI as sg

button_size = (7, 3)

layout = [[sg.Button("", key="-1-", size=button_size), sg.Button("", key="-2-", size=button_size), sg.Button("", key="-3-", size=button_size)],
          [sg.Button("", key="-4-", size=button_size), sg.Button("", key="-5-", size=button_size), sg.Button("", key="-6-", size=button_size)],
          [sg.Button("", key="-7-", size=button_size), sg.Button("", key="-8-", size=button_size), sg.Button("", key="-9-", size=button_size)],
          [sg.Button("Close")]]

window = sg.Window("Demo", layout)
value = window.read()
print(value)
