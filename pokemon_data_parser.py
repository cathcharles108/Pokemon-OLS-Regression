import requests
import pandas as pd
from bs4 import BeautifulSoup

def space_string(s,s1):
    return s.split(s1)[0]

def cut_string(s):
    res = ""
    for i in range(len(s)-8):
        res += s[i]
    return res

poke_species = []
poke_height = []
poke_weight = []
poke_ev = []
poke_catch = []
poke_friend = []
poke_exp = []
poke_titles = []
poke_gen = []

def poke_data(name):
    global poke_titles
    global poke_species
    global poke_height
    global poke_weight
    global poke_ev
    global poke_catch
    global poke_friend
    global poke_exp
    global poke_gen
    link = "https://pokemondb.net" + name
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    titles = soup.findAll('th',limit=11)
    values = soup.findAll('td', limit=11)

    # unnecessary values from the data parser--remove these
    titles.pop(6)
    values.pop(6)
    titles.pop(5)
    values.pop(5)
    titles.pop(1)
    values.pop(1)
    titles.pop(0)
    values.pop(0)

    poke_titles=[]
    poke_values=[]
    for i in range(len(titles)):
        poke_titles.append(titles[i].text.strip())
        if (i==3):
            a = values[i].text.strip().split(", ")
            s = ""
            for j in range(len(a)):
                if j < len(a)-1:
                    s += a[j] + "; "
                else:
                    s += a[j]
            poke_values.append(s)
        else:
            poke_values.append(values[i].text.strip())
    # include generational information
    poke_titles.append("Generation")
    gen = soup.select_one("abbr")
    poke_values.append((gen.text)[-1])

    poke_values[1] = space_string(poke_values[1], "\xa0")
    poke_values[2] = space_string(poke_values[2], "\xa0")
    for i in range(3):
        poke_values[4 + i] = space_string(poke_values[4 + i], " ")
    poke_species.append(cut_string(poke_values[0]))
    poke_height.append(poke_values[1])
    poke_weight.append(poke_values[2])
    poke_ev.append(poke_values[3])
    poke_catch.append(poke_values[4])
    poke_friend.append(poke_values[5])
    poke_exp.append(poke_values[6])
    poke_gen.append(poke_values[7])

page = requests.get("https://pokemondb.net/pokedex/all")
soup = BeautifulSoup(page.content,'html.parser')
table = soup.findAll('tr')
links = []
for url in soup.findAll('a',class_="ent-name", href=True):
    links.append(url["href"])

previous = ""
table_clean = []
count = 0
toss = []
for i in table[1:]:
    if previous != i.a.text.strip():
        table_clean.append(i)
        previous = i.a.text.strip()
    else:
        toss.append(count)
    count += 1

for i in reversed(toss):
    links.pop(i)

category = table[0].text.strip().split(" ")
category[7]= category[7] + category[8]
category[9]= category[9] + category[10]
category.pop(10)
category.pop(8)

poke_names = []
for i in table_clean:
    poke_names.append(i.a.text.strip())

poke_types = []
for i in table_clean:
    types = i.findAll('a', class_="type-icon")
    s = ""
    for j in range(len(types)):
        if j == 1:
            s += "; " + types[j].text.strip()
        else:
            s += types[j].text.strip()
    poke_types.append(s)

num=[]
for i in range(len(table_clean)):
    num.append(table_clean[i].text.strip().split("\n"))

titles=[]
poke_totals=[]
titles.append(poke_totals)
poke_hp=[]
titles.append(poke_hp)
poke_attack=[]
titles.append(poke_attack)
poke_defense=[]
titles.append(poke_defense)
poke_spatk=[]
titles.append(poke_spatk)
poke_spdef=[]
titles.append(poke_spdef)
poke_speed=[]
titles.append(poke_speed)

for i in range(len(num)):
    for j in range(7):
        titles[j].append(num[i][j+1])

titles.insert(0,poke_types)
titles.insert(0,poke_names)

for i in range(len(titles[0])):
    poke_data(links[i])

titles.append(poke_species)
titles.append(poke_height)
titles.append(poke_weight)
titles.append(poke_ev)
titles.append(poke_catch)
titles.append(poke_friend)
titles.append(poke_exp)
titles.append(poke_gen)

for i in range(8):
    category.append(poke_titles[i])

print(category)

df = pd.DataFrame(titles).transpose()
df.rename(columns=lambda s:category[s + 1], index=lambda s: s + 1, inplace=True)
print(df)

# change filename to your intended destination file
df.to_csv("filename.csv", index=False)
