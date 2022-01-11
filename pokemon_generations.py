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
# remove outlier
new_df = df.drop([k])

def pokemon_graph(generation):
    x = np.array(new_df[new_df["Generation"]==generation]["Log Divide"])
    y = np.array(new_df[new_df["Generation"]==generation]["Speed"])
    m = np.polyfit(x,y,1)
    plt.plot(x,y,'o',markersize=3)
    plt.plot(x, m[0]*x +m[1])
    plt.title("Generation " + str(generation) + " Pokemon Log Weight/Height vs Speed")
    plt.ylabel("Speed")
    plt.xlabel("Log Weight/Height")
    plt.show()

def pokemon_ols(generation):
    x = np.array(new_df[new_df["Generation"]==generation][["Weight", "Height"]])
    y = np.array(new_df[new_df["Generation"]==generation]["Speed"])
    x = sm.add_constant(x)
    model = sm.OLS(y,x)
    results = model.fit()
    print(results.summary(xname=["const", "Weight", "Height"], yname=("Generation " + str(generation) + " Speed")))

print(new_df.iloc[-1]["Generation"])
last_gen = new_df.iloc[-1]["Generation"]
for i in range(int(last_gen)):
    pokemon_ols(i+1)
    pokemon_graph(i+1)
