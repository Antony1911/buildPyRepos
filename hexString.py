import binascii
from Crypto.Cipher import AES
import getpass
import PySimpleGUI as sg
import json
import webbrowser
import re

# получение hexadecimal-байтов от пользователя
# hex_bytes = input("Введите hexadecimal-байты: ")
path = "C:\\Users\\frolov.an\\Downloads\\_dist-20230515T085103Z-001\\_dist\\bytes.ini"
charlyConfigPath = f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Charles\\charles.config"

def readDictPath(path):
    with open(path, "r", encoding='utf-8') as f:
        content = f.read()
    return content

def getConfig(hex_bytes, key,  iv):
    # hex_bytes = readDictPath(path)
    # for elem in [hex_bytes[i:i+31] for i in range(0, len(hex_bytes), 31)]:
    #     print(elem)

    # конвертация hexadecimal-байтов в байты
    bytes = binascii.unhexlify(hex_bytes)

    # получение 64-байтового ключа от пользователя
    # key = input("Введите 64-байтовый ключ: ")
    # key = b'5a677564567332496852716157716a376f774d774e5763314d766b6a36477548'

    # конвертация ключа в байты
    key = binascii.unhexlify(key)

    # получение 32-байтового IV от пользователя
    # iv = input("Введите 32-байтовый IV: ")
    # iv = b'f115c755ed1e3dc1627306b3a95b2aba'

    # конвертация IV в байты
    iv = binascii.unhexlify(iv)

    # создание объекта AES cipher с mode-CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # декодирование байтов с помощью AES cipher
    decoded_bytes = cipher.decrypt(bytes)

    # конвертация декодированных байтов в строку
    decoded_string = decoded_bytes.decode('utf-8')
    # decoded_string = decoded_bytes.decode('utf-8')
    text_without_hex = ''.join(['' if ord(c) < 32 or ord(c) > 126 else c for c in decoded_string])
    parsed = json.loads(text_without_hex)
    prettyPrint = json.dumps(parsed, indent=4)
    # print(prettyPrint)

    # sg.Print(prettyPrint)
    sg.popup_scrolled(prettyPrint)
    # input()

def uiMenu():
    # layout = [
    #     [sg.Input(default_text="dataHex", size=(55,1), key='hex'), sg.Text("зашифрованный конфиг")],
    #     [sg.Input(size=(55,1), default_text="5a677564567332496852716157716a376f774d774e5763314d766b6a36477548", key='key'), sg.Text("64-байтовый ключ", text_color='yellow')],
    #     [sg.Input(size=(55,1), default_text="ivHex", key='iv'), sg.Text("32-байтовый IV")],
    #     [sg.Button('go')]
    #     # , sg.Multiline("test", size=(50,25))
    #     # f115c755ed1e3dc1627306b3a95b2aba
    # ]
    
    
    layout =  [
        [sg.Input(size=(55,1), default_text="5a677564567332496852716157716a376f774d774e5763314d766b6a36477548", key='key', enable_events=True,
                  readonly=True, disabled=True), sg.Text("64-byte key", text_color='yellow')],
        [sg.Multiline("""""", size=(70,13), key='mLine', focus=True)],
        [sg.Button('go', size=(12, 1))]
    ]
    
    window = sg.Window('', layout)
    while True:
        event, value = window.read(close=True)
        
        # if event == 'go':
        #     getConfig(value['hex'], value['key'], value['iv'])
        
        if event == 'go':
            data = json.loads(value['mLine'])
            getConfig(data['data']['dataHex'], value['key'], data['data']['ivHex'])
        
        
        if event in ('Cancel', None) or event == sg.WIN_CLOSED:
            try:
                exit(0)
            except:
                break
        window.close()

uiMenu()



