# Pokémon-OLS-Regression
Program that grabs data on all Pokémon (removing Mega Evolutions and other regions' versions) from the Pokémon Database website. The program then conducts several OLS Regressions on the available data, sorted by Pokémon type.

# Why Pokémon?
In the Pokémon universe, Pokémon are creatures trained to fight and battle. Because the universe is primarily a video game franchise, there are a lot of statistics available on each individual Pokémon, so that an experienced player can maximize their chances of winning a battle. Gameplay aside, Pokémon is such a beloved franchise that I found it interesting to observe the tendencies of Pokémon based on their types. To do so, I conduct OLS regressions on Pokémon weight, height, and speed, to see if there is a significant correlation between these statistics and whether they are dependant on a Pokémon's type.

# What is OLS Regression?
Ordinary Least-Squares (OLS) regression is a type of linear least squares model that estimates the unknown parameters in a linear regression. OLS estimates the relationship by minimizing the sum of the squares of the differences between the observed and predicted values of the dependent variable configured as a straight line.

# Part 1: Obtaining Data
Using the Beautiful Soup library on Python, the program initially parses the main Pokémon database website's Pokédex (https://pokemondb.net/pokedex/all), which includes a listing of all existing Pokémon. However, the website lists duplicates of Pokémon with the same name, but different Mega Evolutions and from different regions. For example, Venusaur (entry #003) in the website is listed twice--once as Venusaur, and the second also listed as Venusaur but with a little footnote that says it is actually Mega Venusaur. For the purposes of this project, such entries are cut from the obtained data as not to confuse anyone.

The main Pokédex page only has the basic stats of each Pokémon: Type, HP, Attack, Defense, Sp. Attack, Sp. Defense, and Speed. However, to make things more interesting, I wanted to obtain more data for each Pokémon as well. For example, additional data allows me to observe whether Pokémon size has a relationship with speed, etc. The program then runs through each individual Pokémon's website and parses data from there. In total, the web parser program runs through 899 links--one for the main Pokédex page, and 898 of all individual Pokémon.

# Part 2: OLS Regression and Data Analysis
After obtaining the data, it is exported to a .csv format so the regressions can be done on both Python and R simultaneously.
