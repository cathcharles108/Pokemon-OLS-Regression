# Pokémon-OLS-Regression
Program that grabs data on all Pokémon (removing Mega Evolutions and other regions' versions) from the Pokémon Database website. The program then conducts several OLS Regressions on the available data, sorted by Pokémon type and Generation.

# Why Pokémon?
In the Pokémon universe, Pokémon are creatures trained to battle other Pokémon. Because the universe is primarily a video game franchise, there are a lot of statistics available on each individual Pokémon, so that an experienced player can maximize their chances of winning a battle. Gameplay aside, Pokémon is such a beloved franchise that I found it interesting to observe the tendencies of Pokémon based on their types. Additionally, the franchise has been around long enough to have several 'Generations' of Pokémon; I analyze this as well. To do so, I conduct OLS regressions on Pokémon weight, height, and speed, to see if there is a significant correlation between these statistics and whether they are dependant on a Pokémon's type and/or a Pokémon's Generation.

The hypothesis for my analysis can be divided into three parts:
- I hypothesize that smaller Pokémon (lighter weight, smaller height) correlate positively with speed; that is, I expect smaller Pokémon to be faster. This is done under the assumption that smaller sized Pokémon are more agile.
- I hypothesize further that this trend should be visible across all Pokémon regardless of type.
- However, I am also expecting that the creators be more refined over time, causing higher statistical significance (lower p-values in my regressions) as the Generation number increases.

# What is OLS Regression?
Ordinary Least-Squares (OLS) regression is a type of linear least squares model that estimates the unknown parameters in a linear regression. OLS estimates the relationship by minimizing the sum of the squares of the differences between the observed and predicted values of the dependent variable configured as a straight line.

# Part 1: Obtaining Data
The program initially parses the main Pokémon database website's Pokédex (https://pokemondb.net/pokedex/all), which includes a listing of all existing Pokémon. However, the website lists duplicates of Pokémon with the same name, but different Mega Evolutions and from different regions. For example, Venusaur (entry #003) in the website is listed twice--once as Venusaur, and the second also listed as Venusaur but with a little footnote that says it is actually Mega Venusaur. For the purposes of this project, such entries are cut from the obtained data as not to confuse anyone.

The main Pokédex page only has the basic stats of each Pokémon: Type, HP, Attack, Defense, Sp. Attack, Sp. Defense, and Speed. However, to make things more interesting, I wanted to obtain more data for each Pokémon as well. For example, additional data allows me to observe whether Pokémon size has a relationship with speed, etc. The program then runs through each individual Pokémon's website and parses data from there. In total, the web parser program runs through 899 links--one for the main Pokédex page, and 898 of all individual Pokémon.

The packages used in this part of the project are as follows:
- Requests: to enable the program access the links
- Beautiful Soup: to parse the links after being directed to by Requests
- Pandas: to save the obtained data as a dataframe for easier processing and transfer to .csv

# Part 2: OLS Regression and Data Analysis
After obtaining the data, it is exported to a .csv format for future reference. Feel free to download the .csv file as it is right now for your own use, listed as 'pokemon_data.csv' in this repository. Certainly, I could have immediately continued with the program in Python using the initial pandas dataframe format, but I find it easier to understand the project as a whole when it is broken down into several parts.

After several attempts to visualize the data, I find that plotting the log of weight/height vs speed produces the nicest graph. However, there is still one outlier: Cosmoem has a weight to height ratio of 9999.0, massively skewing the data and the graphs, so I removed it from consideration. Then I proceed with conducting multivariate OLS regressions, setting Weight and Height as independent variables and Speed as the dependent variable. I do this by looping over the different types of Pokémon and their different Generations, also including a regression on all Pokémon as reference. I do not include all the results here but please find the graphs and OLS regression results in the 'Results' files of this repository.

The packages used in this part of the project are as follows:
- Pandas: to convert the .csv data into a dataframe, enabling easier partitions and selections of data
- Numpy: to enable easier processing of the datapoints into arrays
- Matplotlib: to create plots and graphs
- Math: to be able to use the log function
- Statsmodels.api: to conduct regressions

# Conclusion
The OLS regression of all Pokémon, regardless of type, produces a slight negative correlation between Weight and Speed (coefficient of -0.0361) and a positive correlation between Height and Speed (coefficient of 7.2180). Both results are statistically significant at the 0.005 level. This is surprising because our initial hypothesis is that both weight and height would correlate negatively with speed. Therefore, we reject our proposed hypothesis and accept that height moves in the other direction instead.

![image](https://user-images.githubusercontent.com/60662989/149184503-d41e69ee-bd80-4611-9c19-efd19565efc6.png)

The OLS regressions of Pokémon dependent on type, however, is no longer as clear-cut. Most of them have similar results: weight correlating negatively, height correlating positively. However, a lot of these results are not statistically significant. Therefore, we cannot draw any conclusions on the results, controlling for Pokémon type.

Controlling Pokémon by Generation also seems to yield similar results to the analysis by Pokémon type. There is a mixture of statistical significance and insignificance throughout the results; additionally, sometimes Weight correlates negatively, yet other times positively. Therefore, we also cannot form any conclusion based on Pokémon Generation. It can therefore be assumed that the creators of Pokémon might have assigned weight, height, and speed statistics to individual Pokémon somewhat arbitrarily.

# Next Steps
I acknowledge the limitations of this project since I am covering a very narrow scope of Pokémon data. Additionally, a possible extension of this project is to control for another variable that is not type nor Generation.
