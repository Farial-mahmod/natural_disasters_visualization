import matplotlib.pyplot as plt

plt.figure(figsize=(11,8))                                                                # size of the figure
plt.style.use('ggplot')                                                                   # ggplot to be used as the style 


x = ['China (1556)', 'Haiti (2010)', 'China (1920)', 'Turkey (526)', 'China (1976)']      # taken from en.wikipedia.org
num_of_death = [830000, 316000, 273000, 250000, 242419]                                   # Number of death roll


"""
Colors           Meaning

black            highest number of death
silver           lowest death among top 5
"""

colors = ['black', 'darkred', 'red', 'gray', 'silver' ]  
            
x_pos = [i for i, _ in enumerate(x)]                                                      # prepares a counter to use later in a loop


plt.bar(x_pos, num_of_death, color=colors)                                                # setting the bar-graph with colors, width and data
plt.xlabel("Location & Year (AD)")                                                        # Location and Year on X-Axis
plt.ylabel("Number of Death")                                                             # Death Number on Y-Axis
plt.title("Earthquakes causing highest death toll ")                                      # Title of the plot
plt.xticks(x_pos, x)                                                                      # X-Axis range of values
plt.show()                                                                                # displaying the plot
