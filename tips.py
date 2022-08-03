import math
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
path = '/home/varvara/ds_bootcamp/ds-phase-0/learning/datasets/tips.csv'
tips = pd.read_csv(path, index_col=0)





st.write("""
#### Total bill histogram
# """)
fig, ax = plt.subplots()
ax.hist(tips['total_bill'], rwidth=0.8, facecolor='salmon')

fig.set_figwidth(20)
fig.set_figheight(12)

plt.xlabel("Total bill, $", size=20)
plt.ylabel("Bills quantity", size=20)

ax.bar_label(ax.containers[0], size = 20, padding = 3)
ax.set_title('Total bill hist', fontsize = 30, color = 'darkgrey')

st.pyplot(fig)





st.write("""
#### Connection between total bill and tips
# """)

fig, ax = plt.subplots()
scatter = ax.scatter(tips['total_bill'], tips['tip'], s=tips['size'], facecolor='salmon');

fig.set_figwidth(15)
fig.set_figheight(15)

plt.xlabel("Total bill, $", size=20)
plt.ylabel("Tips", size=20)
plt.grid()

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

ax.set_title('Total bill vs Tip', fontsize = 20, color = 'darkgrey')

st.pyplot(fig)



st.write("""
#### Bills distribution by weekday
# """)

total_bill_by_weekday = pd.DataFrame(tips.groupby('day')['total_bill'].mean()).reset_index()
total_bill_by_weekday['total_bill'] = round(total_bill_by_weekday['total_bill'])

# ручная сортировка
sorter = ['Thur', 'Fri', 'Sat', 'Sun']
sorterIndex = dict(zip(sorter, range(len(sorter))))
total_bill_by_weekday['day_num'] = total_bill_by_weekday['day'].map(sorterIndex)
total_bill_by_weekday.sort_values(['day_num'], ascending = True, inplace = True)
total_bill_by_weekday.drop('day_num', 1, inplace = True)

order=['Thur', 'Fri', 'Sat', 'Sun']

fig, ax = plt.subplots()
ax.bar(total_bill_by_weekday['day'], total_bill_by_weekday['total_bill'], alpha=0.7, color = 'salmon')

fig.set_figwidth(20)
fig.set_figheight(12)

plt.xlabel("Weekday", size=20)
plt.ylabel("Total bill, $", size=20)

ax.bar_label(ax.containers[0], size = 20, padding = 3);
ax.set_title('Bills by weekday', fontsize = 30, color = 'darkgrey');

st.pyplot(fig)


st.write("""
#### Connection between tips weekdays and sex
# """)

tips_male = tips.loc[tips['sex'] == 'Male']
tips_female = tips.loc[tips['sex'] == 'Female']

fig, ax = plt.subplots()
scatter1 = ax.scatter(tips_male['tip'], tips_male['day'], facecolor='blue', label='Male')
scatter2 = ax.scatter(tips_female['tip'], tips_female['day'], facecolor='salmon', label='Female')

plt.legend()

fig.set_figwidth(10)
fig.set_figheight(10)

plt.xlabel("Tips", size=20, alpha=0.3)
plt.ylabel("Weekday", size=20)
plt.grid()

ax.set_title('Tip by weekday', fontsize = 20, color = 'darkgrey')

st.pyplot(fig)