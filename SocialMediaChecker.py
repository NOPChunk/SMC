import requests


class Check:

    def __init__(self):
        self.email = str(input("Enter an Email > "))
        self.twitter()

    @staticmethod
    def first_condition():
        print("\t\t[👍] Founded     |\n\t\t------------------\n")

    @staticmethod
    def seccond_condition():
        print("\t\t[👎] Unfounded   |\n\t\t------------------\n")

    def twitter(self):
        print("\t\t==================\n\t\t[🐦] Twitter [🐦]\n\t\t==================")
        r = requests.Session()
        url = "https://api.twitter.com/i/users/email_available.json?email=" + self.email
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        host = "api.twitter.com"
        accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        r.headers = {'User-Agent': user_agent}
        r.headers = {'Host': host}
        r.headers = {'Accept': accept}
        req = r.get(url).json()
        text = str(req)
        # print(text)
        if not text.find("'valid': False") != True:
            self.first_condition()
        else:
            self.seccond_condition()
        self.instagram()

    def instagram(self):
        print("\t\t==================\n\t\t[⬚] Instagram [⬚]\n\t\t==================")
        r = requests.Session()
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        r.headers = {'user-agent': user_agent}
        r.headers.update({'X-CSRFToken': "missing"})
        data = {"email_or_username": self.email}
        req = r.post(url, data=data)
        # print(req.text)
        if req.text.find("We sent an self.email to") >= 0:
            self.first_condition()
        elif req.text.find("password") >= 0:
            self.first_condition()
        elif req.text.find("sent") >= 0:
            self.first_condition()
        else:
            self.seccond_condition()
        self.snapchat()

    def snapchat(self):
        print("\t\t==================\n\t\t[👻] SnapChat [👻]\n\t\t==================")
        r = requests.Session()
        url = "https://accounts.snapchat.com/accounts/merlin/login"
        r.headers = {
            'Host': 'accounts.snapchat.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-XSRF-TOKEN': 'missing',
            'Content-Type': 'application/json',
            'Origin': 'https://accounts.snapchat.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Connection': 'keep-alive',
            'Referer': 'https://accounts.snapchat.com/accounts/merlin/login'
        }
        cookies = {
            'xsrf_token': 'missing'
        }
        data = {
            'email': self.email, 'app': 'BITMOJI_APP'
        }
        req = r.post(url, cookies=cookies, json=data)

        if req.text.find("hasSnapchat") >= 0:
            self.first_condition()
        else:
            self.seccond_condition()


if __name__ == "__main__":
    print("""
    
           [🔎] SocialMediaChecker [🔍]
        [ Twitter - Instagram - Snapchat ]
        ================🍍================ 
        [+]      Created: NOPChunk       |
        [+]      Github : NOPChunk       |
        [+]      YouTube: Networkchunk   |
        ================🍍================
        
        """)
Check()
print("\n\t\t------------------\n\t\t[★] GOOD LUCK [★]\n\t\t------------------\n")
input("[🔥] Press enter to exit > ")
