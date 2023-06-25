# import binascii
# from Crypto.Cipher import AES
# import getpass
import PySimpleGUI as sg
# from tkinter import *
# import json

from Crypto.Cipher import AES

plaintext = '{"configKeys":{"BettingEnabledGeo":[]}'
key = '5a677564567332496852716157716a376f774d774e5763314d766b6a36477548'
iv = 'f115c755ed1e3dc1627306b3a95b2aba'

key_bytes = bytes.fromhex(key)
iv_bytes = bytes.fromhex(iv)
block_size = AES.block_size
padded_plaintext = plaintext.encode('utf-8') + (block_size - len(plaintext) % block_size) * chr(block_size - len(plaintext) % block_size).encode('utf-8')
cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
ciphertext = cipher.encrypt(padded_plaintext)
encoded_ciphertext = ciphertext.hex()


# print(encoded_ciphertext)
sg.Print(encoded_ciphertext)
input()