import matplotlib.pyplot as plt

plt.figure(figsize=(11,8)) 
plt.style.use('ggplot')                                                                                                    # ggplot to be used as the style 


x = ['Plague - Europe, Asia\n & Africa (1346–1353)', 'Flu - Worldwide\n(1918–1920)','Plague - Europe \n& Asia (541–542)',
'HIV/AIDS - Worldwide \n(1981-present)', 'Plague - Worldwide\n(1855–1960)']                                                # taken from en.wikipedia.org

num_of_death = [ 200 , 100 , 50,  38 , 12 ]                                                                                # Number of death roll


"""
Colors           Meaning

black            highest number of death
silver           lowest death among top 5
"""

colors = ['black', 'darkred', 'red', 'gray', 'silver' ]  
            
x_pos = [i for i, _ in enumerate(x)]                                                                                       # prepares a counter to use later in a loop


plt.bar(x_pos, num_of_death, color=colors)                                                                                 # setting the bar-graph with colors, width and data
plt.xlabel("Location & Year (AD)")                                                                                         # Location and Year on X-Axis
plt.ylabel("Number of Death (Million)")                                                                                    # Death Number on Y-Axis
plt.title("Pandemics causing highest death toll ")                                                                         # Title of the plot
plt.xticks(x_pos, x)                                                                                                       # X-Axis range of values
plt.show()                                                                                                                 # displaying the plot
