import json 
import requests

es = requests.get("https://api.github.com/search/users?q=javascript")

json_data = es.json()

usCount = len(json_data['items']) - 1

for x in range(usCount):
    print(json_data['items'][x]['html_url'])

Results = """
https://github.com/javascript
https://github.com/javascript-tutorial 
https://github.com/javascripter        
https://github.com/javascriptit        
https://github.com/hyperlink
https://github.com/JavaScriptErika     
https://github.com/JavascriptDeNoobAPro
https://github.com/javascript-forks    
https://github.com/javascriptDev       
https://github.com/javascriptdezero    
https://github.com/JavascriptMick      
https://github.com/javascript666666    
https://github.com/javascripto
https://github.com/AmyDayday
https://github.com/javascriptacademy-stash
https://github.com/javascripteverywhere
https://github.com/luckyscc
https://github.com/JavascriptIsMagic
https://github.com/javascript-indonesias
https://github.com/javascript-ninja-123
https://github.com/javascriptextjs
https://github.com/javascript-queen
https://github.com/javascriptisscary
https://github.com/JavaScript-Resource
https://github.com/javaScriptKampala
https://github.com/javascript-obfuscator
https://github.com/javascriptlove
https://github.com/JavaScript-Packer
https://github.com/JavaScriptNoob
"""