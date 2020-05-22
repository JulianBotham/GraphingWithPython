#Plotting
import matplotlib.pyplot as plt

labels = ['Monica', 'Adrian', 'Jared']
num = [230, 100, 98] #These numbers do not have to be percentages

plt.title('Voting Results: Club President', fontdict={'fontsize': 20})
plt.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
plt.show()
