import requests
from requests.structures import CaseInsensitiveDict
import json
def create_account(first_name,last_name,email,day,month,year,password,sex):
    #line
    url = "https://www.facebook.com/ajax/register.php"
    headers = CaseInsensitiveDict()
    headers["authority"] = "www.facebook.com"
    headers["x-fb-lsd"] = "AVqcTg9Tcaw"
    headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    headers["content-type"] = "application/x-www-form-urlencoded"
    headers["accept"] = "*/*"
    headers["origin"] = "https://www.facebook.com"
    headers["sec-fetch-site"] = "same-origin"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-dest"] = "empty"
    headers["referer"] = "https://www.facebook.com/"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["cookie"] = "sb=U405YfdfEIA3RIrSJs2mqGZ8; datr=U405YZOWKUpJ3pU_SI_XLeFl; fr=1KgfaGK4YbibU59aw.AWVo1a89PdDjYOxX8v7Z037n0X0.BhOvKv.GL.GFN.0.0.BhUV1J.AWUaVhuD3AM; wd=670x671"
    data = "jazoest=21006&lsd=AVqcTg9Tcaw&firstname="+first_name+"&lastname="+last_name+"&reg_email__="+email+"&reg_email_confirmation__=&reg_passwd__="+password+"&birthday_day="+day+"&birthday_month="+month+"&birthday_year="+year+"&birthday_age=&did_use_age=false&sex="+sex+"&preferred_pronoun=&custom_gender=&referrer=&asked_to_login=0&use_custom_gender=&terms=on&ns=0&ri=f573b07d-58a7-4c05-991a-2842823fa461&action_dialog_shown=&ignore=captcha%7Creg_email_confirmation__&locale=ml_IN&reg_instance=U405YZOWKUpJ3pU_SI_XLeFl&captcha_persist_data=AZmmgDXYezKHhijCrzaVvqYUnTYI7WRzmAhhj1P7TFaeisNZutCK3FmK9z770efuQGVmtTNkUpWhVyd5KTXekankAKT9ptT1hp6FV5bXb_VDD_7U0BchdSjSD0O2c37XQ26JcQ5X6qqlc18SyUm5eey4ijMHrC1hBM1PWM_0OaezCnvP8z_nxFKAcGD-kUatoZLBI7MQtEOBWj2HB0ZPABd0e34rpqUTzbD7q0zkQSk3b3LwrNhmJ4WfXu_pp3HV4nTc7W7sSxr_QOEnSW1OIQXKYNBB0OuLf49r8onePQFEV1EzLEjbgO4U4baBkCKt0sopJ7crcPa7pZ0JhpmkApHiDRaP1hXFyakSbs6OYlfAUiRp2TuKzkz43waH91MbY0I&captcha_response=&__user=0&__a=1&__dyn=7xe6FomK36Q5E5ObwBy9uC1swgE98nwgU6C7UW3q327E2vwXx60kO4o3Bw5VCwjE3awbG782Cw8G1nzUO0n2US1vw5zwwwi81nE2YxW0D83mwaS0zE5W08HwSyE158&__csr=&__req=b&__hs=18897.PHASED%3ADEFAULT.2.0.0.0.&dpr=1&__ccg=GOOD&__rev=1004457543&__s=c2m3vk%3Ayiqb2i%3A0ef1y9&__hsi=7012488637629718969-0&__comet_req=0&__spin_r=1004457543&__spin_b=trunk&__spin_t=1632722243"
    resp = requests.post(url, headers=headers, data=data)
    return resp.status_code
def details():
    #line
    f = open("label.txt", "r")
    print('\n')
    print(f.read())
    print('\n')
    print("Developed BY-SIBIN THOM4S\n")
def main():
    #line
    details()
    file1 = open('data.txt', 'r')
    count = 0
    while True:
        count += 1
        line = file1.readline()
        if not line:
            break
        user_name=line.strip()
        ini_string = json.dumps(user_name)
        final_dictionary = eval(json.loads(ini_string))
        result=create_account(final_dictionary["firstname"],final_dictionary["lastname"],final_dictionary["email"],final_dictionary["day"],final_dictionary["month"],final_dictionary["year"],final_dictionary["password"],final_dictionary["sex"])
        if(result == 200):
            print("[+] Account Created "+str(final_dictionary))
    file1.close()
main()
