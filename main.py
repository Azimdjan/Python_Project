# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# plt.rcdefaults()
# fig, ax = plt.subplots()
# data = pd.read_csv("./Data/history_data.csv")
# df = pd.DataFrame(data)
# date = df['Date time'].to_list()
# temperature = df['Temperature'].to_list()
#
# y_pos = np.arange(len(date))
#
# ax.barh(y_pos, temperature, align='center', color='#a64fe8')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(date, color='blue')
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel("Temperature 'C", color='green')
# ax.set_title('Weather history of the USA in the last 8 days',
#              color='red')
#
# plt.show()
import sklearn
from sklearn import tree
# [height, weight, shoe size]
print('Please, input the height, weight, and the shoe size parameters of the individual whose gender you want to predict')
h = input('Input height ')
w = input('Input weight ')
s = input('Input shoe size ')
x = [[180, 80, 42], [192, 90, 43], [165,65,38], [170,55,37], [200,100,45],[200, 70, 39]]
y = ['male', 'male', 'female','female', 'male', 'female']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
prediction = clf.predict([[h, w,s]])
print(prediction)
