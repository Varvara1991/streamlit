# Чаевые в ресторане
#Шаг 1. Импортируем библиотеки
import math
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#Шаг 2. Прочитаем датасет в переменную tips
# path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
path = '/home/varvara/ds_bootcamp/ds-phase-0/learning/datasets/tips.csv'
tips = pd.read_csv(path, index_col=0)


# Шаг 4. Нарисуйте гистограмму total_bill

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


### Шаг 5. Нарисуйте scatterplot, показывающий связь между total_bill and tip

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



ax = sns.boxplot(x="day", y="total_bill", hue="time", data=tips, order=['Thur', 'Fri', 'Sat', 'Sun'])
st.pyplot(ax)
### Шаг 7. Нарисуйте 1 график, связывающий total_bill, tip, и size
#### Подсказка: это одна функция
# plt.figure(figsize=(10,10))
    
# plot = sns.scatterplot(x=tips['total_bill'], y=tips['tip'], size = tips['size'], sizes=(10,300), alpha=0.7, color = 'salmon')

# plt.xlabel('Total bill')
# plt.ylabel('Tip')
# plt.title('Total bill vs Tip')

# plt.grid()

# plt.show()
# ### Шаг 8. Покажите связь между днем недели и размером счета
# total_bill_by_weekday = pd.DataFrame(tips.groupby('day')['total_bill'].mean()).reset_index()
# total_bill_by_weekday['total_bill'] = round(total_bill_by_weekday['total_bill'])
# total_bill_by_weekday
# plt.figure(figsize=(30, 8))
# plt.rc('xtick', labelsize=17)
# plt.rc('ytick', labelsize=15)
# plot = sns.barplot(x="day", y="total_bill", data=total_bill_by_weekday, color='pink', order=['Thur', 'Fri', 'Sat', 'Sun'])
# plot.bar_label(plot.containers[0], size = 20);
# plot.set_title('Kills by actors', fontsize = 30, color = 'darkgrey');
# ### Шаг 9. Нарисуйте scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу
# plt.figure(figsize=(10,10))
    
# plot = sns.scatterplot(x=tips['tip'], y=tips['day'], hue = tips['sex'], alpha=0.7)

# plt.xlabel('Tip')
# plt.ylabel('Weekday')
# plt.title('Tip vs Weekday')

# plt.grid()

# plt.show()
# ### Шаг 10. Нарисуйте box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)
# ax = sns.boxplot(x="day", y="total_bill", hue="time", data=tips, order=['Thur', 'Fri', 'Sat', 'Sun'])
# ### Шаг 11. Нарисуйте 2 гистограммы чаевых на обед и ланч. Расположите их рядом по горизонтали.
# dinner_tips = tips.loc[tips['time'] == 'Dinner']
# lunch_tips = tips.loc[tips['time'] == 'Lunch']
# # First create a grid of plots
# # ax will be an array of two Axes objects
# fig, ax = plt.subplots(1, 2, figsize=(20, 7))

# # Call plot() method on the appropriate object
# ax[0].hist(lunch_tips['tip'])
# ax[0].set_xlabel('Lunch time')
# ax[0].set_ylabel('Quantity')
# ax[1].hist(dinner_tips['tip'])
# ax[1].set_xlabel('Quantity')
# ax[1].set_xlabel('Dinner time')
# plt.tight_layout();
# ### Шаг 12. Нарисуйте 2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. Расположите их по горизонтали.
# men_tips = tips.loc[tips['sex'] == 'Male']
# women_tips = tips.loc[tips['sex'] == 'Female']
# fig, (ax1,ax2) = plt.subplots(1,2, figsize=(16,6))

# ax1.set_title('Men total bill')
# sns.scatterplot(x='total_bill', y='tip', hue='smoker', hue_order=['Yes','No'], data=men_tips, ax=ax1)

# ax2.set_title('Women total bill')
# sns.scatterplot(x='total_bill', y='tip', hue='smoker', hue_order=['Yes','No'], data=women_tips, ax=ax2);