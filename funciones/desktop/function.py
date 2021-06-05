import PySimpleGUI as sg

def close_window(event):
    if event == sg.WIN_CLOSED or event == "-OK-":
        break

