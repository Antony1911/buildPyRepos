import PySimpleGUI as sg
import requests

def enable_rewrite():
  url = 'http://192.168.137.1:8888/rewrite/enable'
  requests.post(url)
  # sg.popup('Rewrite enabled')

def disable_rewrite():
    url = 'http://192.168.137.1:8888/rewrite/disable'
    requests.post(url)
    # sg.popup('Rewrite disabled')

layout = [[sg.Button('Enable Rewrite'), sg.Button('Disable Rewrite')]]

window = sg.Window('Charles Proxy Rewrite Control', layout)

while True:
  event, _ = window.read()
  if event == sg.WINDOW_CLOSED:
    break
  elif event == 'Enable Rewrite':
    enable_rewrite()
  elif event == 'Disable Rewrite':
    disable_rewrite()

window.close()