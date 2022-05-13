from termcolor import colored
from os import system
import mmh3
import requests
import codecs
import urllib3

system("clear")
banner = '''
  ╔═╗┌─┐┬  ┬┬┌─┐┌─┐┌┐┌  ╦ ╦┌─┐┌─┐┬ ┬┌─┐┌─┐
  ╠╣ ├─┤└┐┌┘││  │ ││││  ╠═╣├─┤└─┐├─┤├┤ └─┐
  ╚  ┴ ┴ └┘ ┴└─┘└─┘┘└┘  ╩ ╩┴ ┴└─┘┴ ┴└─┘└─┘
        # Coded by Ilham | @ilhamrzr
'''

print(colored(banner, 'green'))
target = input("Target Url: ")
urllib3.disable_warnings()
response = requests.get(target, verify=False)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print("Result: " +colored(hash, 'red'))
print("Shodan Dorks: http.favicon.hash:{}\n".format(hash))