#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv(r"Downloads/sales.csv")
print(sales)


# In[3]:


plt.plot(sales.month_name, sales.total_profit, linewidth = 5, marker = 'o', linestyle = 'dotted', markerfacecolor = 'yellow')
plt.legend([("profit")], loc = "upper right")

plt.xlabel('Month Name')
plt.ylabel('Item sold units number')

plt.show


# In[6]:


plt.pie(sales.total_units, labels = sales.month_name)
plt.show


# In[24]:


x = np.linspace(-10, 10, 1000)

y = x**2

fig, ax = plt.subplots()
ax.set_title("Parabola $Y = X^2$")
ax.plot(x, y)


# In[28]:


x = [1, 2, 3, 4, 5]

y = [16, 234, 25, 90, 32]

plt.bar(x, y)
plt.show()

