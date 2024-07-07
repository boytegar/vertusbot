
import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime, timedelta

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'content-length': '0',
    'priority': 'u=1, i',
    'Origin': 'https://thevertus.app',
    'Referer': 'https://thevertus.app/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

def load_credentials():
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File token.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragent = [line.strip() for line in f.readlines()]
        if index < len(useragent):
            return useragent[index]
        else:
            return "Index out of range"
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'

def getdata(query, useragent):
    url = 'https://api.thevertus.app/users/get-data' #POST
    payload = {}
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getquest(query, useragent):
    url = 'https://api.thevertus.app/missions/get' #POST
    payload = {}
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def completequest(query, missionid, useragent):
    url = 'https://api.thevertus.app/missions/complete'
    payload = {
        'missionId': missionid
    }
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def collect(query, useragent):
    url = 'https://api.thevertus.app/game-service/collect'
    payload = {}
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def checkindaily(query, useragent):
    url = 'https://api.thevertus.app/users/claim-daily'
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    payload = {}
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def upgrade(query, useragent, type):
    url = 'https://api.thevertus.app/users/upgrade' # payload = { upgrade : farm, storage, population}
    payload = {
        'upgrade': type
    }
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getupgradecards(query, useragent):
    url = 'https://api.thevertus.app/upgrade-cards'
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None
    
def upgradecards(query, useragent, cardid):
    url = 'https://api.thevertus.app/upgrade-cards/upgrade'
    payload = {'cardId': cardid}
    headers['Authorization'] = f'Bearer {query}'
    headers['User-Agent'] = useragent
    try:
        response_codes_done = range(200, 211)
        response_code_notfound = range(400, 410)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        elif response.status_code in response_code_failed:
            print("error 500")
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimdaily():
    queries = load_credentials()
    default = 1000000000000000000
    while True:
        for index, query in enumerate(queries):
            useragent = getuseragent(index)
            detail_data = getdata(query, useragent)
            print(f'====================== Account {index+1} ======================')
            if detail_data is not None:
                valid = detail_data.get('isValid')
                if valid == True:
                    print(f"TelegramID : {detail_data['user']['telegramId']} || Wallet Address : {detail_data['user']['walletAddress']}")
                    print(f"Current balance : {detail_data['user']['balance']/default}")
                    print('Collecting...')
                    time.sleep(5)
                    data_collect = collect(query, useragent)
                    if data_collect is not None:
                        print(f"New balance : {data_collect['newBalance']/default}")
                else:
                    print('user not valid')
            else:
                print('User Not Found')
            
        delay = random.randint(7200, 7500)
        printdelay(delay)
        time.sleep(delay)

def claimtask():
    queries = load_credentials()
    default = 1000000000000000000
    for index, query in enumerate(queries):
            useragent = getuseragent(index)
            detail_data = getdata(query, useragent)
            print(f'====================== Account {index+1} ======================')
            if detail_data is not None:
                print(f"TelegramID : {detail_data['user']['telegramId']} || Wallet Address : {detail_data['user']['walletAddress']}")
                print(f"Current balance : {detail_data['user']['balance']/default}")
                data_quest = getquest(query, useragent)
                time.sleep(5)
                if data_quest is not None:
                    listgroup = data_quest.get('groups')
                    for group in listgroup:
                        title = group.get('title')
                        print(f"Task : {title}")
                        mission = group.get('missions')
                        for mis in mission:
                            for m in mis:
                                missionid = m.get('_id')
                                iscompleted = m.get('isCompleted')
                                if iscompleted != True:
                                    data_complete = completequest(query, missionid, useragent)
                                    newbalance = data_complete.get('newBalance')
                                    print(f"Task : {m['title']} | Current Balance : {newbalance/default}")
                                else:
                                    print(f"Task : {m['title']} Completed")
                                time.sleep(3)
                    time.sleep(2)

                    listsponsor = data_quest.get('sponsors')
                    for sponsor in listsponsor:
                        for spon in sponsor:
                            title = spon.get('title')
                            missionid = spon.get('_id')
                            iscompleted = spon.get('isCompleted')
                            if iscompleted != True:
                                data_complete = completequest(query, missionid, useragent)
                                newbalance = data_complete.get('newBalance')
                                print(f"Task : {spon['title']} | Current Balance : {newbalance/default}")
                            else:
                                print(f"Task : {spon['title']} Completed")
                            time.sleep(3)
                    time.sleep(2)

                    listcommunity = data_quest.get('community')
                    for community in listcommunity:
                        for com in community:
                            title = com.get('title')
                            missionid = com.get('_id')
                            iscompleted = com.get('isCompleted')
                            if iscompleted != True:
                                data_complete = completequest(query, missionid, useragent)
                                newbalance = data_complete.get('newBalance')
                                print(f"Task : {com['title']} | Current Balance : {newbalance/default}")
                            else:
                                print(f"Task : {com['title']} Completed")
                            time.sleep(3)
                    time.sleep(2)
            else:
                print('User Not Found')

def checkin():
    queries = load_credentials()
    default = 1000000000000000000
    for index, query in enumerate(queries):
            useragent = getuseragent(index)
            detail_data = getdata(query, useragent)
            print(f'====================== Account {index+1} ======================')
            if detail_data is not None:
                valid = detail_data.get('isValid')
                if valid == True:
                    print(f"TelegramID : {detail_data['user']['telegramId']} || Wallet Address : {detail_data['user']['walletAddress']}")
                    print(f"Current balance : {detail_data['user']['balance']/default}")
                    time.sleep(3)
                    data_checkin = checkindaily(query, useragent)
                    if data_checkin is not None:
                        success = data_checkin.get('success')
                        if success == True:
                            print(f"Checkin Done, Reward : {data_checkin['claimed']/default}")
                        else:
                            print(f"{data_checkin['msg']}")
                    else:
                        print('checkin failed')
                else:
                    print('user not valid')
                time.sleep(5)

def upgrademain():
    queries = load_credentials()
    default = 1000000000000000000
    for index, query in enumerate(queries):
            useragent = getuseragent(index)
            detail_data = getdata(query, useragent)
            print(f'====================== Account {index+1} ======================')
            if detail_data is not None:
                print(f"TelegramID : {detail_data['user']['telegramId']} || Wallet Address : {detail_data['user']['walletAddress']}")
                print(f"Current balance : {detail_data['user']['balance']/default}")
                time.sleep(3)
                for i in range(1, 1):
                    data_upgrade = upgrade(query, useragent, "farm")
                    print(data_upgrade)
                    time.sleep(5)

                for i in range(1, 5):
                    data_upgrade = upgrade(query, useragent, "population")
                    print(data_upgrade)
                    time.sleep(5)

def upgradecard():
    queries = load_credentials()
    default = 1000000000000000000
    while True:
        for index, query in enumerate(queries):
            useragent = getuseragent(index)
            detail_data = getdata(query, useragent)
            print(f'====================== Account {index+1} ======================')
            if detail_data is not None:
                valid = detail_data.get('isValid')
                if valid == True:
                    print(f"TelegramID : {detail_data['user']['telegramId']} || Wallet Address : {detail_data['user']['walletAddress']}")
                    print(f"Current balance : {detail_data['user']['balance']/default}")
                    print('Collection Data...')
                    time.sleep(5)
                    data_listcard = getupgradecards(query, useragent)
                    economycards = data_listcard.get('economyCards')
                    for economy in economycards:
                        types = economy.get('type')
                        name = economy.get('cardName')
                        id = economy.get('_id')
                        level = economy.get('currentLevel')
                        print(f"Type : {types} | name : {name}")
                        if level < 3:
                            data_upgrade = upgradecards(query, useragent, id)
                            print("success")
                            time.sleep(2)
                        else:
                            print('reach lvl 3')
                            time.sleep(2)
                        
                    militarycards = data_listcard.get('militaryCards')
                    for military in militarycards:
                        types = military.get('type')
                        name = military.get('cardName')
                        id = military.get('_id')
                        level = military.get('currentLevel')
                        print(f"Type : {types} | name : {name}")
                        if level <= 3:
                            data_upgrade = upgradecards(query, useragent, id)
                            print("success")
                            time.sleep(2)
                        else:
                            print('reach lvl 3')
                            time.sleep(2)
                            
                    sciencecards = data_listcard.get('scienceCards')
                    for science in sciencecards:
                        types = science.get('type')
                        name = science.get('cardName')
                        id = science.get('_id')
                        level = science.get('currentLevel')
                        print(f"Type : {types} | name : {name}")
                        if level <= 3:
                            data_upgrade = upgradecards(query, useragent, id)
                            print("success")
                            time.sleep(2)
                        else:
                            print('reach lvl 3')
                            time.sleep(2)
                else:
                    print('user not valid')

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")

######################################################################################################################################################

def main():
    print(r"""
        
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sanscryptox
              
        select this one :
        1. checkin daily
        2. claim daily
        3. upgrade card
        
          
          """)
 
    selector = input("Select the one ? (default 2): ").strip().lower()


    if selector == '1':
        checkin()
    elif selector == '2':
        claimdaily()
    elif selector == '3':
        upgradecard()
    else:
        exit()

def print_welcome_message(serial=None):
    print(r"""
              
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sansxgroup
              
          """)
    print()
    if serial is not None:
        print(f"Copy, tag bot @SnailHelperBot and paste this key in discussion group t.me/sansxgroup")
        print(f"Your key : {serial}")

def read_serial_from_file(filename):
    serial_list = []
    with open(filename, 'r') as file:
        for line in file:
            serial_list.append(line.strip())
    return serial_list

serial_file = "serial.txt"
serial_list = read_serial_from_file(serial_file)


def get_serial(current_date, getpcname, name, status):
    formatted_current_date = current_date.strftime("%d-%m-%Y")
    # Encode each value using base64
    getpcname += "knjt"
    name    += "knjt"
    encoded_getpcname = base64.b64encode(getpcname.encode()).decode().replace("=", "")
    encoded_current_date = base64.b64encode(formatted_current_date.encode()).decode().replace("=", "")
    encoded_name = base64.b64encode(name.encode()).decode().replace("=", "")
    encoded_status = base64.b64encode(str(status).encode()).decode().replace("=", "")

    # Calculate the length of each encoded value
    getpcname_len = len(encoded_getpcname)
    current_date_len = len(encoded_current_date)
    name_len = len(encoded_name)
    status_len = len(encoded_status)

    # Concatenate the encoded values with their lengths
    serial = "S4NS-"
    serial += str(getpcname_len).zfill(2) + encoded_getpcname
    serial += str(current_date_len).zfill(2) + encoded_current_date
    serial += str(name_len).zfill(2) + encoded_name
    serial += str(status_len).zfill(2) + encoded_status
    return serial

def decode_pc(serial, getpcname, name, current_date):
    try:
        getpcname_len = int(serial[5:7])
        encoded_getpcname = serial[7:7+getpcname_len]
        current_date_len = int(serial[7+getpcname_len:9+getpcname_len])
        encoded_current_date = serial[9+getpcname_len:9+getpcname_len+current_date_len]
        name_len = int(serial[9+getpcname_len+current_date_len:11+getpcname_len+current_date_len])
        encoded_name = serial[11+getpcname_len+current_date_len:11+getpcname_len+current_date_len+name_len]
        status_len = int(serial[11+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len])
        encoded_status = serial[13+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len+status_len]

        # Decode each value using base64
        decoded_getpcname = base64.b64decode(encoded_getpcname + "==").decode()
        decoded_current_date = base64.b64decode(encoded_current_date + "==").decode()
        decoded_name = base64.b64decode(encoded_name + "==").decode()
        decoded_status = base64.b64decode(encoded_status + "==").decode()
        
        dates = compare_dates(decoded_current_date)

        if decoded_status != '1':
            print("Key Not Generated")
            return None
            
        elif decoded_getpcname.replace("knjt", "") != getpcname:
            print("Different devices registered")
            return None
        
        elif decoded_name.replace("knjt", "") != name:
            print("Different bot registered")
            return None
        
        elif dates < 0:
            print("Key Expired")
            return None
        else:
            print(f"            Key alive until : {decoded_current_date} ")
            return dates
    except Exception as e:
        print(f'Key Error : {e}')

def compare_dates(date_str):
    tanggal_compare_dt = datetime.strptime(date_str, '%d-%m-%Y')
    tanggal_now = datetime.now()
    perbedaan_hari = (tanggal_compare_dt - tanggal_now).days
    return perbedaan_hari

def started():
    getpcname = socket.gethostname()
    name = "VERTUS"
    current_date = datetime.now() # Get the current date
    status = '0'

    if len(serial_list) == 0:
        serial = get_serial(current_date, getpcname, name, status)
        print_welcome_message(serial)
    else:
        serial = serial_list[0]
        if serial == 'S4NS-XXWEWANTBYPASSXX':
            main()
        else:
            decodeds = decode_pc(serial, getpcname, name, current_date)
            if decodeds is not None:
                    print_welcome_message()
                    time.sleep(10)
                    main()         
            else:
                serial = get_serial(current_date, getpcname, name, status)
                print_welcome_message(serial)
                print("Please submit the key to bot for get new key")
            

if __name__ == "__main__":
    started()

