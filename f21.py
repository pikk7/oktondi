import requests
from bs4 import BeautifulSoup
page = requests.get("http://f21.hu/fogjunkosszeadiakokert/")
soup = BeautifulSoup(page.content, 'html.parser')
test=soup.select(".content p")[4:]
test=[ n.get_text() for n in test]

nevek=soup.select('.content strong')[10:]
nevek=[ n.get_text() for n in nevek]
nevek=[ n.replace(':',"") for n in nevek]
nevek=[ n.strip() for n in nevek]


megyek=soup.find_all('h3')
megyek=[ n.get_text() for n in megyek]

telepulesek=soup.find_all('h4')
telepulesek=[ n.get_text() for n in telepulesek]
telepulesek=[ n.replace(':',"") for n in telepulesek]

# for item in test:
#     print(item.split('(')[0])
#     print(item)



targy_tanar_dict = {'magyar': [], 'matek': [], 'angol': [],'informatika':[],"történelem":[],"biológia":[],"német":[]}

targy=['magyar', 'matek', 'angol','informatika',"történelem","biológia","német"]

for item in test:
    if any(s in item for s in targy):
        if(targy[0] in item):
            targy_tanar_dict[targy[0]].append(item)
        if(targy[1] in item):
            targy_tanar_dict[targy[1]].append(item)
        if(targy[2] in item):
            targy_tanar_dict[targy[2]].append(item)
        if(targy[3] in item):
            targy_tanar_dict[targy[3]].append(item)
        if(targy[4] in item):
            targy_tanar_dict[targy[4]].append(item)
        if(targy[5] in item):
            targy_tanar_dict[targy[5]].append(item)
        if(targy[6] in item):
            targy_tanar_dict[targy[6]].append(item)
    else:
        print('item')


for key in targy_tanar_dict:
    with open(key+'.txt', "w", encoding="utf-8") as f:
        for elem in targy_tanar_dict.get(key):
            f.write(elem+'\n')