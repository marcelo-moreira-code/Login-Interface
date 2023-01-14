from PySimpleGUI import PySimpleGUI as sg

# Layout

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Ckeckbox('Salvar Login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()  # Untracking
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        valores['usuario'] == 'marcelo' and valores['senha'] == '12345'
        print('Bem-vindo ao Serviço!')

