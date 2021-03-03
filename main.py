import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcdefaults()
fig, ax = plt.subplots()
data = pd.read_csv("./Data/history_data.csv")
df = pd.DataFrame(data)
date = df['Date time'].to_list()
temperature = df['Temperature'].to_list()

y_pos = np.arange(len(date))

ax.barh(y_pos, temperature, align='center', color='#a64fe8')
ax.set_yticks(y_pos)
ax.set_yticklabels(date, color='blue')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("Temperature 'C", color='green')
ax.set_title('Weather history of the USA in the last 8 days',
             color='red')

plt.show()
