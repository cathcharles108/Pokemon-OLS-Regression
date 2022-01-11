import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statsmodels.api as sm

df = pd.read_csv(filename)

df["Divide"] = df["Weight"] / df["Height"]
df["Log Divide"] = df["Divide"].apply(math.log)
p = np.array(df["Divide"])

k = 0
for i in range(len(p)):
    if p[i]>8000:
        k = i
        break
# removing the outlier
new_df = df.drop([k])

def pokemon_graph(type_name):
    x = np.array(new_df[new_df["Type"].str.contains(type_name)]["Log Divide"])
    y = np.array(new_df[new_df["Type"].str.contains(type_name)]["Speed"])
    # print(x,y)
    m = np.polyfit(x,y,1)
    plt.plot(x,y,'o',markersize=3)
    plt.plot(x, m[0]*x +m[1])
    if type_name == "":
        plt.title("Pokemon Log Weight/Height vs Speed")
    else:
        plt.title(type_name + " Pokemon Log Weight/Height vs Speed")
    plt.ylabel("Speed")
    plt.xlabel("Log Weight/Height")
    plt.show()

def pokemon_ols(type_name):
    x = np.array(new_df[new_df["Type"].str.contains(type_name)][["Weight","Height"]])
    y = np.array(new_df[new_df["Type"].str.contains(type_name)]["Speed"])
    x = sm.add_constant(x)
    model = sm.OLS(y,x)
    results = model.fit()
    if type_name == "":
        print(results.summary(xname=["const", "Weight", "Height"], yname="Speed"))
    else:
        print(results.summary(xname=["const", "Weight", "Height"], yname=(type_name + " Speed")))

x = np.array(new_df["Type"])
y = []
for i in range(len(x)):
    a = x[i].split("; ")
    for j in range(len(a)):
        y.append(a[j])
poke_types = []
for i in range(len(y)):
    if y[i] not in poke_types:
        poke_types.append(y[i])
poke_types.append("")

for s in poke_types:
    pokemon_ols(s)
    pokemon_graph(s)
