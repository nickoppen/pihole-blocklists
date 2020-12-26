##
## 0. Install python3+ and the requests library if required
## 1. Get an account at SecurityTrails.com (free ones are available for infrequent users)
## 2. Get your APIKEY from the the dash board and replace the text "Your Security Trails APIKey here" below
## 3. Replace the text "addYourDomain.com" below with the domain you want to block
## 4. The domains with "0.0.0.0 on the front will be added to a text file in your working directory (domain.com.txt)
## 5. Add the content of the output file to a new or existing blocklist
## 6. Repeat from step 3 for each domain
##


import requests
import os

domain = "addYourDomain.com"

url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"

querystring = {"children_only":"false"}

headers = {
    "Accept": "application/json",
    "APIKEY": "Your Security Trails APIKey here"
}

response = requests.request("GET", url, headers=headers, params=querystring)

lstSubs = response.json()["subdomains"]

count = 0
with open (os.getcwd()+"\\"+domain+".txt", "w") as f:
    f.write("0.0.0.0 " + domain + "\n")
    for sub in lstSubs:
        f.write("0.0.0.0 " + sub + "." + domain+"\n")
        count = count + 1
    print ("Blocklist with "+str(count)+" domains written to: "+f.name)
