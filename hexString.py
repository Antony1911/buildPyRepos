import binascii
from Crypto.Cipher import AES
import getpass
import PySimpleGUI as sg
from tkinter import *
from tkinter import filedialog
import json
import ctypes
import keyboard
sg.theme('SystemDefault1')

# 0x409
# charlyConfigPath = f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Charles\\charles.config"
# продовский ключ
# keyMain = ['5a677564567332496852716157716a376f774d774e5763314d766b6a36477548', 'test04', 'test05', 'test06']
keyMain = '5a677564567332496852716157716a376f774d774e5763314d766b6a36477548'

def check_language():
    # user32 = ctypes.WinDLL('user32', use_last_error=True)
    # curr_window = user32.GetForegroundWindow()
    # thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    # klid = user32.GetKeyboardLayout(thread_id)
    # lid = klid & (2**16 - 1)
    # lid_hex = hex(lid)

    
    if hex(ctypes.WinDLL('user32', use_last_error=True).GetKeyboardLayout(ctypes.WinDLL('user32', use_last_error=True).GetWindowThreadProcessId(ctypes.WinDLL('user32', use_last_error=True).GetForegroundWindow(), 0)) & (2**16 - 1)) == "0x409":
        print('eng_local')
    else:
        keyboard.press_and_release('win+space')

 
def readDictPath(path):
    with open(path, "r", encoding='utf-8') as f:
        content = f.read()
    return content
def decodeConfig(hex_bytes, key,  ivStr):
    # hex_bytes = readDictPath(path)
    # for elem in [hex_bytes[i:i+31] for i in range(0, len(hex_bytes), 31)]:
    #     print(elem)
    
    # конвертация hexadecimal-байтов в байты
    bytes = binascii.unhexlify(hex_bytes)

    # конвертация ключа в байты
    key = binascii.unhexlify(key)

    # конвертация IV в байты
    iv = binascii.unhexlify(ivStr)

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
    resultWindow(prettyPrint, ivStr)
def encodeConfig(plaintext, key, iv):
    key_bytes = bytes.fromhex(key)
    iv_bytes = bytes.fromhex(iv)
    block_size = AES.block_size
    padded_plaintext = plaintext.encode('utf-8') + (block_size - len(plaintext) % block_size) * chr(block_size - len(plaintext) % block_size).encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    ciphertext = cipher.encrypt(padded_plaintext)
    encoded_ciphertext = ciphertext.hex()
    
    prettyPrint = '{' + '\n\t"data": {\n\t\t"dataHex": ' + f'"{encoded_ciphertext}",\n\t\t"ivHex": ' + f'"{iv}"' + '\n\t}' + '}'
    startMenu(prettyPrint)


def startMenu(textTo): 
    layout =  [
        [sg.Input(size=(55,1), default_text=keyMain, key='key', enable_events=True,
                  readonly=True, disabled=True), sg.Text("64-byte key", text_color='green')],

        # [sg.Combo(keyMain, default_value=keyMain[0], key='key', enable_events=True), 
        #  sg.Text("64-byte key", text_color='green')],

        [sg.Multiline(f"""{textTo}""", size=(70,13), key='mLine', focus=True)],
        [sg.Button('decode', size=(12, 1)), sg.CloseButton('Close', size=(12, 1))]
    ]
    
    window = sg.Window('encoded', layout, no_titlebar=False, grab_anywhere=True)
    while True:
        event, value = window.read(close=True)
        
        if event == 'decode':
            
            data = json.loads(value['mLine'])
            ivMain = data['data']['ivHex']
            decodeConfig(data['data']['dataHex'], keyMain, ivMain)
        
        if event in ('Close', None) or event == sg.WIN_CLOSED:
            try:
                exit(0)
            except:
                break
        window.close()
def resultWindow(resultText, iv):
    def get_text():
        getText = text.get("1.0", "end-1c")
        root.destroy()
        encodeConfig(getText, keyMain, iv)
        return getText
        
    def save_text():
        getText = text.get("1.0", "end-1c")
        try:
            path = filedialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
            root.title('remoteConfig ' + path)
        except:
            return   
        with open(path, 'w') as f:
            f.write(getText)
    
    def prompt():
        sg.popup_notify("Настроить (Настройка популярного) --> hasMainscreenSettings = True")
        
    #to create a window
    #root window is the parent window
    root = Tk()
    fram = Frame(root)
    
    root.title('RemoteConfig v.0.2')
    root.geometry("700x900+700+40")

    
    #saveas button
    buttSave = Button(fram, text='Save as', command=save_text)
    buttSave.pack(side=LEFT)

    #adding label to search box
    Label(fram,text='Text to find: ',).pack(side=LEFT)
    
    
    #adding of single line text box
    edit = Entry(fram, width=40)

    #positioning of text box
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    
    #setting focus
    edit.focus_set()
# =================================================================
    # encode back
    buttEncode = Button(fram, text='Encode', command=get_text, bg='red')
    buttEncode.pack(side=RIGHT)
    
# =================================================================

    buttClear = Button(fram, text='Clear', bg='yellow') 
    buttClear.pack(side=RIGHT)
    
    buttFind = Button(fram, text='Find', bg='#248c0f') 
    buttFind.pack(side=RIGHT)


    # fram.bind("<Control-f>", key)
    # fram.bind("found", callback)
    fram.pack(side=TOP)

    #  scrollBar
    v = Scrollbar(root, orient = 'vertical')
    v.pack(side=RIGHT, fill = 'y')
    
    #text box in root window
    text = Text(root, height=40, width=70, font=('Consolas',14), yscrollcommand=v.set)
    v.config(command=text.yview)
    text.pack(expand=True)
    # text.insert('1.0',open("C:\\Users\\frolov.an\\Desktop\\testHex.txt", 'r').read())
    text.insert("1.0", resultText)
    # text.config(state='disabled')
        
        
    #function to search string in text
    def clear():
        text.tag_remove('found', '1.0', END)
        edit.delete(0, END)
        
    def find():
        #remove tag 'found' from index 1 to END
        text.tag_remove('found', '1.0', END)
        
        #returns to widget currently in focus
        s = edit.get().split(' ')[0]
        if s:
            idx = '1.0'
            while 1:
                #searches for desired string from index 1
                idx = text.search(s, idx, nocase=1,
                                stopindex=END)
                if not idx: break
                
                #last index sum of current index and
                #length of text
                lastidx = '%s+%dc' % (idx, len(s))
                
                #overwrite 'Found' at idx
                text.tag_add('found', idx, lastidx)
                idx = lastidx
                # text.mark_set("insert", lastidx)
            
            #mark located string as red
            text.tag_config('found', background='yellow', selectbackground='black')
            text.see(lastidx)

        edit.focus_set()
   

    def select_all(e):
        edit.tag_add(SEL, "1.0", END)
        edit.mark_set(INSERT, "1.0")
        edit.see(INSERT)
        edit.focus_set()
        edit.selection_range(0, END)
        
   
    def press_f(e):
        edit.focus_set()
        edit.selection_range(0, END)

    def press_v(e):
        find()

    def press_x(e):
        clear()
        
    root.bind('<Control-f>', press_f)
    root.bind('<Control-v>', press_v)
    root.bind('<Control-x>', press_x)
    
    buttEncode.config(command=get_text)
    buttClear.config(command=clear)
    buttFind.config(command=find)
    
    root.mainloop()
    root.destroy()

check_language()
startMenu('')

