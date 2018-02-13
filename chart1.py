import numpy as np
import matplotlib.pyplot as plt

languages= ['Python', 'Javascript', 'Java', 'GO', 'Swift']
median_salary= (71354, 69226, 70009, 74558, 75310)

y_pos = np.arange(len(languages))
plt.title("Median Salaries for Prograaming Languages")
y_pos = np.arange(len(languages))

plt.bar(y_pos, median_salary)
plt.xticks(y_pos, languages)
plt.show()