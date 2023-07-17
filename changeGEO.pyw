import PySimpleGUI as sg
import pyperclip
sg.theme('Dark2')

# открываем локальную БД, создаем из нее dict, она уже по сути создана как словарь
def readDictPath(path):
    with open(path, "r", encoding='utf-8') as f:
        content = eval(f.read())
    return content


def dropdownMenu():
    dict = readDictPath("C:\\Users\\frolov.an\\Desktop\\countries.ini")
    countries = list(dict.keys())    
    
    layout = [
        [sg.Text("Choose the country")],
        [sg.DropDown(values=countries, default_value=countries[0], auto_size_text=True, key='-DROPDOWN-')],
        [sg.Button('Copy')]
        # , sg.Multiline("test", size=(50,25))
    ]
    
    window = sg.Window('countries', layout)
    while True:
        event, value = window.read(close=True)
        
        if event == 'Copy':
            selected_value = value['-DROPDOWN-']
            pyperclip.copy(dict[selected_value][1])
            dropdownMenu()
            
        if event in ('Cancel', None) or event == sg.WIN_CLOSED:
            try:
                exit(0)
            except Exception:
                exit(0)
        window.close()

dropdownMenu()





# def getData(countriesDict):
#     for i in countriesDict:
#         # i - страна, countries[i][0] - id страны, countries[i][1] - на подмену
#         print(i, f" id={countriesDict[i][0]}")
#         print(countriesDict[i][1])

# def provider():
#     font = ('Courier New', 11)
#     sg.set_options(font=font)
#     layout = [
#         [sg.TabGroup(
#             [[sg.Tab(f'TAB {i}', [[sg.Text(f'Tab {i}')]]) for i in range(3)] +
#             [sg.Tab('SUPPLIER', [[sg.Text('Supplier')]], key='-SUPPLIER-')]])],
#         [sg.Push(), sg.Button('Provider')],
#     ]
#     window = sg.Window('TabGroup', layout)

#     visible = True

#     while True:

#         event, values = window.read()

#         if event in (None, 'Exit'):
#             break
#         elif event == 'Provider':
#             visible = not visible
#             window['-SUPPLIER-'].update(visible=visible)
#     window.close()