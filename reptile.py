import requests
import re
html=requests.get("https://movie.douban.com/top250")
print(html.text)
results=re.findall("<a\shref='(.*?)'.*?alt='(.*?)'.*?</a>",html,re.S)
for result in results:
    print(result.group[1],result.group[2])