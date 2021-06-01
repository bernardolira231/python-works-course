import PySimpleGUI as sg

button_size = (7, 3)

layout = [[sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("Close")]]

window = sg.Window("Demo", layout).read
