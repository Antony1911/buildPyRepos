import PySimpleGUI as sg
from pyperclip import copy
sg.theme('Dark2')
dict = {   
   'USA, Florida':['153', '{ "Success": true, "Value": { "City": "Джексонвилл", "Region": "Флорида", "Country": "США", "CountryCode": "US", "CityId": 26292, "RegionId": 1697, "CountryId": 153, "Continent": "NA", "Ip": "171.22.76.4" } }'],
   'Ангилья':['10', '{ "Success": true, "Value": { "Country": "Ангилья", "CountryCode": "AI", "CityId": 0, "RegionId": 0, "CountryId": 10, "Continent": "NA", "Ip": "5.62.58.9" } }'],
   'Антигуа и Барбуда':['12', '{ "Success": true, "Value": { "Country": "Антигуа и Барбуда", "CountryCode": "AG", "CityId": 0, "RegionId": 0, "CountryId": 12, "Continent": "NA", "Ip": "5.62.56.15" } }'],
   'Аруба':['16', '{ "Success": true, "Value": { "Country": "Аруба", "CountryCode": "AW", "CityId": 0, "RegionId": 0, "CountryId": 16, "Continent": "NA", "Ip": "5.62.56.22" } }'],
   'Армения, Котайкская область':['15', '{ "Success": true, "Value": { "City": "Цахкадзор", "Region": "Котайкская область", "Country": "Армения", "CountryCode": "AM", "CityId": 28491, "RegionId": 2968, "CountryId": 15, "Continent": "AS", "Ip": "5.62.62.15" } }'],
   'Австралия':['4', '{ "Success": true, "Value": { "Region": "Западная Австралия", "Country": "Австралия", "CountryCode": "AU", "CityId": 0, "RegionId": 2181, "CountryId": 4, "Continent": "OC", "Ip": "103.231.89.165" } }'],
   'Аландские острова':['None', '{     "Success": true,     "Value": {         "CountryCode": "AX",         "Continent": "EU",         "Ip": "5.62.63.245"     } }'],
   'Австрия':['5', '{ "Success": true, "Value": { "Country": "Австрия", "CountryCode": "AT", "CityId": 0, "RegionId": 0, "CountryId": 5, "Continent": "EU", "Ip": "185.244.212.179" } }'],
   'Ангола':['9', '{ "Success": true, "Value": { "Country": "Ангола", "CountryCode": "AO", "CityId": 0, "RegionId": 0, "CountryId": 9, "Continent": "AF", "Ip": "5.62.62.11" } }'],
   'Бразилия':['31', '{ "Success": true, "Value": { "Region": "Sao Paulo", "Country": "Бразилия", "CountryCode": "BR", "CityId": 0, "RegionId": 274, "CountryId": 31, "Continent": "SA", "Ip": "185.54.230.51" } }'],
   'Багамские о-ва':['18', '{ "Success": true, "Value": { "Country": "Багамские о-ва", "CountryCode": "BS", "CityId": 0, "RegionId": 0, "CountryId": 18, "Continent": "NA", "Ip": "5.62.58.27" } }'],
   'Бурунди':['35', '{ "Success": true, "Value": { "Country": "Бурунди", "CountryCode": "BI", "CityId": 0, "RegionId": 0, "CountryId": 35, "Continent": "AF", "Ip": "5.62.62.62" } }'],
   'Бенин':['25', '{ "Success": true, "Value": { "Country": "Бенин", "CountryCode": "BJ", "CityId": 0, "RegionId": 0, "CountryId": 25, "Continent": "AF", "Ip": "5.62.62.35" } }'],
   'Бельгия':['24', '{ "Success": true, "Value": { "Country": "Бельгия", "CountryCode": "BE", "CityId": 0, "RegionId": 0, "CountryId": 24, "Continent": "EU", "Ip": "5.62.20.35" } }'],
   'Босния и Герцеговина':['29', '{ "Success": true, "Value": { "City": "Сараево", "Region": "Сараевский кантон", "Country": "Босния и Герцеговина", "CountryCode": "BA", "CityId": 22628, "RegionId": 3567, "CountryId": 29, "Continent": "EU", "Ip": "5.62.60.41" } }'],
   'Болгария':['27', '{ "Success": true, "Value": { "Country": "Болгария", "CountryCode": "BG", "CityId": 0, "RegionId": 0, "CountryId": 27, "Continent": "EU", "Ip": "5.62.62.53" } }'],
   'Венгрия':['40', '{ "Success": true, "Value": { "Region": "Будапешт", "Country": "Венгрия", "CountryCode": "HU", "CityId": 0, "RegionId": 303, "CountryId": 40, "Continent": "EU", "Ip": "185.128.26.101" } }'],
   'Великобртания':['39', '{ "Success": true, "Value": { "Country": "Великобритания", "CountryCode": "GB", "CityId": 0, "RegionId": 0, "CountryId": 39, "Continent": "EU", "Ip": "159.242.227.64" } }'],
   'Гана':['48', '{ "Success": true, "Value": { "Country": "Гана", "CountryCode": "GH", "CityId": 0, "RegionId": 0, "CountryId": 48, "Continent": "AF", "Ip": "5.62.60.150" } }'],
   'Гвинея-Бисау':['52', '{ "Success": true, "Value": { "Region": "Бисау", "Country": "Гвинея-Бисау", "CountryCode": "GW", "CityId": 0, "RegionId": 377, "CountryId": 52, "Continent": "AF", "Ip": "5.62.62.162" } }'],
   'Греция':['60', '{ "Success": true, "Value": { "Region": "Аттика", "Country": "Греция", "CountryCode": "GR", "CityId": 0, "RegionId": 1747, "CountryId": 60, "Continent": "EU", "Ip": "5.62.60.157" } }'],
   'Германия, Берлин':['53', '{ "Success": true, "Value": { "Country": "Германия", "CountryCode": "DE", "CityId": 0, "RegionId": 0, "CountryId": 53, "Continent": "EU", "Ip": "80.255.12.235" } }'],
   'Дания':['62', '{ "Success": true, "Value": { "Country": "Дания", "CountryCode": "DK", "CityId": 0, "RegionId": 0, "CountryId": 62, "Continent": "EU", "Ip": "37.120.232.115" } }'],
   'Доминика':['none', '{ "Success": true, "Value": { "CountryCode": "DM", "Continent": "NA", "Ip": "5.62.56.78" } }'],
   'Доминиканская Республика':['', '{ "Success": true, "Value": { "Country": "Доминиканская республика", "CountryCode": "DO", "CityId": 0, "RegionId": 0, "CountryId": 65, "Continent": "NA", "Ip": "5.62.56.81" } }'],
   'Египет':['66', '{ "Success": true, "Value": { "Country": "Египет", "CountryCode": "EG", "CityId": 0, "RegionId": 0, "CountryId": 66, "Continent": "AF", "Ip": "5.62.62.110" } }'],
   'Замбия':['67', '{ "Success": true, "Value": { "Country": "Замбия", "CountryCode": "ZM", "CityId": 0, "RegionId": 0, "CountryId": 67, "Continent": "AF", "Ip": "5.62.61.223" } }'],
   'Испания, Барселона':['78', '{ "Success": true, "Value": { "Region": "Каталония", "Country": "Испания", "CountryCode": "ES", "CityId": 0, "RegionId": 1870, "CountryId": 78, "Continent": "EU", "Ip": "37.120.142.28" } }'],
   'Италия':['79', '{ "Success": true, "Value": { "Country": "Италия", "CountryCode": "IT", "CityId": 0, "RegionId": 0, "CountryId": 79, "Continent": "EU", "Ip": "84.17.59.47" } }'],
   'Израиль':['70', '{ "Success": true, "Value": { "Country": "Израиль", "CountryCode": "IL", "CityId": 0, "RegionId": 0, "CountryId": 70, "Continent": "AS", "Ip": "185.185.133.179" } }'],
   'Ирландия':['76', '{ "Success": true, "Value": { "Country": "Ирландия", "CountryCode": "IE", "CityId": 0, "RegionId": 0, "CountryId": 76, "Continent": "EU", "Ip": "81.17.242.166" } }'],
   'Иран':['75', '{ "Success": true, "Value": { "Region": "Esfahan", "Country": "Иран", "CountryCode": "IR", "CityId": 0, "RegionId": 519, "CountryId": 75, "Continent": "AS", "Ip": "5.62.62.169" } }'],
   'Катар':['86', '{ "Success": true, "Value": { "Country": "Катар", "CountryCode": "QA", "CityId": 0, "RegionId": 0, "CountryId": 86, "Continent": "AS", "Ip": "5.62.61.95" } }'],
   'Канада, Онтарио':['85', '{ "Success": true, "Value": { "Region": "Онтарио", "Country": "Канада", "CountryCode": "CA", "CityId": 0, "RegionId": 1678, "CountryId": 85, "Continent": "NA", "Ip": "95.142.124.20" } }'],
   'Куба':['97', '{ "Success": true, "Value": { "Country": "Куба", "CountryCode": "CU", "CityId": 0, "RegionId": 0, "CountryId": 97, "Continent": "NA", "Ip": "5.62.56.75" } }'],
   'Китай':['90', '{ "Success": true, "Value": { "Region": "Beijing", "Country": "Китай", "CountryCode": "CN", "CityId": 0, "RegionId": 768, "CountryId": 90, "Continent": "AS", "Ip": "5.62.34.43" } }'],
   'Кипр':['88', '{ "Success": true, "Value": { "Region": "Никосия", "Country": "Кипр", "CountryCode": "CY", "CityId": 0, "RegionId": 1937, "CountryId": 88, "Continent": "EU", "Ip": "5.62.62.105" } }'],
   'Казахстан':['82', '{ "Success": true, "Value": { "Country": "Казахстан", "CountryCode": "KZ", "CityId": 0, "RegionId": 0, "CountryId": 82, "Continent": "AS", "Ip": "5.62.62.187" } }'],
   'Кения':['87', '{ "Success": true, "Value": { "Country": "Кения", "CountryCode": "KE", "CityId": 0, "RegionId": 0, "CountryId": 87, "Continent": "AF", "Ip": "5.62.62.190" } }'],
   "Кот-д'Ивуар":['96', '{ "Success": true, "Value": { "Country": "Кот-д`Ивуар", "CountryCode": "CI", "CityId": 0, "RegionId": 0, "CountryId": 96, "Continent": "AF", "Ip": "5.62.62.102" } }'],
   'Конго':['94', '{ "Success": true, "Value": { "Country": "Конго (Kinshasa)", "CountryCode": "CD", "CityId": 0, "RegionId": 0, "CountryId": 94, "Continent": "AF", "Ip": "5.62.60.103" } }'],
   'Камерун':['84', '{ "Success": true, "Value": { "Country": "Камерун", "CountryCode": "CM", "CityId": 0, "RegionId": 0, "CountryId": 84, "Continent": "AF", "Ip": "5.62.62.71" } }'],
   'Ливан':['105', '{ "Success": true, "Value": { "Country": "Ливан", "CountryCode": "LB", "CityId": 0, "RegionId": 0, "CountryId": 105, "Continent": "AS", "Ip": "5.62.62.210" } }'],
   'Латвия':['102', '{ "Success": true, "Value": { "Country": "Латвия", "CountryCode": "LV", "CityId": 0, "RegionId": 0, "CountryId": 102, "Continent": "EU", "Ip": "185.135.85.161" } }'],
   'Люксенбург':['109', '{ "Success": true, "Value": { "Region": "Luxembourg", "Country": "Люксембург", "CountryCode": "LU", "CityId": 0, "RegionId": 866, "CountryId": 109, "Continent": "EU", "Ip": "92.38.172.12" } }'],
   'Литва':['107', '{ "Success": true, "Value": { "Country": "Литва", "CountryCode": "LT", "CityId": 0, "RegionId": 0, "CountryId": 107, "Continent": "EU", "Ip": "5.62.60.237" } }'],
   'Мексика, Керетаро':['120', '{ "Success": true, "Value": { "City": "Керетаро", "Region": "Керетаро", "Country": "Мексика", "CountryCode": "MX", "CityId": 21500, "RegionId": 2024, "CountryId": 120, "Continent": "NA", "Ip": "31.14.72.24" } }'],
   'Мальта':['118', '{ "Success": true, "Value": { "Country": "Мальта", "CountryCode": "MT", "CityId": 0, "RegionId": 0, "CountryId": 118, "Continent": "EU", "Ip": "5.62.63.1" } }'],
   'Мозамбик':['121', '{ "Success": true, "Value": { "Country": "Мозамбик", "CountryCode": "MZ", "CityId": 0, "RegionId": 0, "CountryId": 121, "Continent": "AF", "Ip": "5.62.63.35" } }'],
   'Нидерланды':['133', '{ "Success": true, "Value": { "Region": "Северная Голландия", "Country": "Нидерланды", "CountryCode": "NL", "CityId": 0, "RegionId": 2194, "CountryId": 133, "Continent": "EU", "Ip": "84.17.46.161" } }'],
   'Нигерия':['132', '{ "Success": true, "Value": { "Country": "Нигерия", "CountryCode": "NG", "CityId": 0, "RegionId": 0, "CountryId": 132, "Continent": "AF", "Ip": "5.62.63.55" } }'],
   'Норвегия':['137', '{     "Success": true,     "Value": {         "Country": "Норвегия",         "CountryCode": "NO",         "CityId": 0,         "RegionId": 0,         "CountryId": 137,         "Continent": "EU",         "Ip": "146.70.103.87"     } }'],
   'ОАЭ':['139', '{ "Success": true, "Value": { "Country": "ОАЭ", "CountryCode": "AE", "CityId": 0, "RegionId": 0, "CountryId": 139, "Continent": "AS", "Ip": "5.62.63.189" } }'],
   'Польша':['147', '{ "Success": true, "Value": { "City": "Варшава", "Region": "Мазовецкое воеводство", "Country": "Польша", "CountryCode": "PL", "CityId": 17866, "RegionId": 1778, "CountryId": 147, "Continent": "EU", "Ip": "84.17.55.2" } }'],
   'Португалия':['148', '{ "Success": true, "Value": { "Region": "Лиссабон", "Country": "Португалия", "CountryCode": "PT", "CityId": 0, "RegionId": 2489, "CountryId": 148, "Continent": "EU", "Ip": "194.39.126.121" } }'],
   'Перу':['145', '{ "Success": true, "Value": { "Region": "Cusco", "Country": "Перу", "CountryCode": "PE", "CityId": 0, "RegionId": 1019, "CountryId": 145, "Continent": "SA", "Ip": "5.62.58.161" } }'],
   'Пакистан':['141', '{ "Success": true, "Value": { "Country": "Пакистан", "CountryCode": "PK", "CityId": 0, "RegionId": 0, "CountryId": 141, "Continent": "AS", "Ip": "5.62.63.63" } }'],
   'Панама':['142', '{ "Success": true, "Value": { "Country": "Панама", "CountryCode": "PA", "CityId": 0, "RegionId": 0, "CountryId": 142, "Continent": "NA", "Ip": "5.62.56.169" } }'],
   'Румыния':['152', '{ "Success": true, "Value": { "Region": "Бухарест", "Country": "Румыния", "CountryCode": "RO", "CityId": 0, "RegionId": 1782, "CountryId": 152, "Continent": "EU", "Ip": "5.62.63.81" } }'],
   'Россия':['1', '{ "Success": true, "Value": { "City": "Москва", "Region": "Москва и Московская обл.", "Country": "Россия", "CountryCode": "RU", "CityId": 1, "RegionId": 1, "CountryId": 1, "Continent": "EU", "Ip": "5.62.18.63" } }'],
   'Сирия':['170', '{ "Success": true, "Value": { "Country": "Сирия", "CountryCode": "SY", "CityId": 0, "RegionId": 0, "CountryId": 170, "Continent": "AS", "Ip": "5.62.63.145" } }'],
   'Сингапур':['169', '{ "Success": true, "Value": { "Country": "Сингапур", "CountryCode": "SG", "CityId": 0, "RegionId": 0, "CountryId": 169, "Continent": "AS", "Ip": "92.223.85.67" } }'],
   'Саудовская Аравия':['158', '{ "Success": true, "Value": { "Region": "Эр-Рияд", "Country": "Саудовская Аравия", "CountryCode": "SA", "CityId": 0, "RegionId": 2076, "CountryId": 158, "Continent": "AS", "Ip": "5.62.63.106" } }'],
   'Cловения':['172', '{ "Success": true, "Value": { "Country": "Словения", "CountryCode": "SI", "CityId": 0, "RegionId": 0, "CountryId": 172, "Continent": "EU", "Ip": "5.62.61.145" } }'],
   'Словакия':['171', '{ "Success": true, "Value": { "Region": "Bratislava", "Country": "Словакия", "CountryCode": "SK", "CityId": 0, "RegionId": 1242, "CountryId": 171, "Continent": "EU", "Ip": "5.62.61.141" } }'],
   'Сенигал':['165', '{ "Success": true, "Value": { "Region": "Дакар", "Country": "Сенегал", "CountryCode": "SN", "CityId": 0, "RegionId": 3667, "CountryId": 165, "Continent": "AF", "Ip": "5.62.61.129" } }'],
   'Турция':['190', '{ "Success": true, "Value": { "City": "Стамбул", "Region": "Стамбул", "Country": "Турция", "CountryCode": "TR", "CityId": 15636, "RegionId": 1308, "CountryId": 190, "Continent": "AS", "Ip": "92.38.180.49" } }'],
   'Туркменистан':['188', '{ "Success": true, "Value": { "Country": "Туркменистан", "CountryCode": "TM", "CityId": 0, "RegionId": 0, "CountryId": 188, "Continent": "AS", "Ip": "5.62.63.171" } }'],
   'Тунис':['187', '{ "Success": true, "Value": { "Country": "Тунис", "CountryCode": "TN", "CityId": 0, "RegionId": 0, "CountryId": 187, "Continent": "AF", "Ip": "5.62.63.167" } }'],
   'Танзания':['181', '{ "Success": true, "Value": { "Country": "Танзания", "CountryCode": "TZ", "CityId": 0, "RegionId": 0, "CountryId": 181, "Continent": "AF", "Ip": "5.62.63.155" } }'],
   'Тайвань':['179', '{ "Success": true, "Value": { "Country": "Тайвань", "CountryCode": "TW", "CityId": 0, "RegionId": 0, "CountryId": 179, "Continent": "AS", "Ip": "172.107.246.163" } }'],
   'Таджикистан':['178', '{ "Success": true, "Value": { "Country": "Таджикистан", "CountryCode": "TJ", "CityId": 0, "RegionId": 0, "CountryId": 178, "Continent": "AS", "Ip": "5.62.63.151" } }'],
   'Уганда':['191', '{ "Success": true, "Value": { "Country": "Уганда", "CountryCode": "UG", "CityId": 0, "RegionId": 0, "CountryId": 191, "Continent": "AF", "Ip": "5.62.63.175" } }'],
   'Украина':['2', '{ "Success": true, "Value": { "Country": "Украина", "CountryCode": "UA", "CityId": 0, "RegionId": 0, "CountryId": 2, "Continent": "EU", "Ip": "31.14.75.34" } }'],
   'Финляндия':['197', '{ "Success": true, "Value": { "Region": "Уусимаа", "Country": "Финляндия", "CountryCode": "FI", "CityId": 0, "RegionId": 1710, "CountryId": 197, "Continent": "EU", "Ip": "185.77.217.48" } }'],
   'Фиджи':['195', '{     "Success": true,     "Value": {         "Country": "Фиджи",         "CountryCode": "FJ",         "CityId": 0,         "RegionId": 0,         "CountryId": 195,         "Continent": "OC",         "Ip": "5.62.58.94"     } }'],
   'Франция':['198', '{ "Success": true, "Value": { "Region": "Прованс — Альпы — Лазурный Берег", "Country": "Франция", "CountryCode": "FR", "CityId": 0, "RegionId": 1711, "CountryId": 198, "Continent": "EU", "Ip": "138.199.14.142" } }'],
   'Хорватия':['201', '{ "Success": true, "Value": { "Country": "Хорватия", "CountryCode": "HR", "CityId": 0, "RegionId": 0, "CountryId": 201, "Continent": "EU", "Ip": "5.62.63.225" } }'],
   'Чехия':['204', '{ "Success": true, "Value": { "Country": "Чехия", "CountryCode": "CZ", "CityId": 0, "RegionId": 0, "CountryId": 204, "Continent": "EU", "Ip": "185.246.210.131" } }'],
   'Швеция':['207', '{ "Success": true, "Value": { "Country": "Швеция", "CountryCode": "SE", "CityId": 0, "RegionId": 0, "CountryId": 207, "Continent": "EU", "Ip": "37.46.121.225" } }'],
   'Швейцария':['207', '{ "Success": true, "Value": { "Country": "Швейцария", "Region": "Zrich", "CountryCode": "CH", "CityId": 0, "RegionId": 1513, "CountryId": 206, "Continent": "EU", "Ip": "146.70.99.149" } }'],
   'Эфиопия':['213', '{ "Success": true, "Value": { "Country": "Эфиопия", "CountryCode": "ET", "CityId": 0, "RegionId": 0, "CountryId": 213, "Continent": "AF", "Ip": "5.62.62.127" } }'],
   'Эстония':['212', '{ "Success": true, "Value": { "Region": "Харьюмаа", "Country": "Эстония", "CountryCode": "EE", "CityId": 0, "RegionId": 1861, "CountryId": 212, "Continent": "EU", "Ip": "5.62.62.121" } }'],
   'Ямайка':['none', '{ "Success": true, "Value": { "CountryCode": "JM", "Continent": "NA", "Ip": "5.62.56.129" } }']}


# открываем локальную БД, создаем из нее dict, она уже по сути создана как словарь
def readDictPath(path):
    with open(path, "r", encoding='utf-8') as f:
        content = eval(f.read())
    return content


def dropdownMenu():
    # dict = readDictPath("C:\\Users\\frolov.an\\Desktop\\countries.ini")
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
            copy(dict[selected_value][1])
            dropdownMenu()
            
        if event in ('Cancel', None) or event == sg.WIN_CLOSED:
            break
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