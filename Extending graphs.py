import matplotlib.pyplot as plt

#Split the figure into 2 subplots

fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121) #121 means to split into 1 row, 2 columns, and put in 1st part

ax2 = fig.add_subplot(122) #122 means split into 1 row, 2 columns and put in 2nd part

labels = ['Adrian', 'Monica', 'Jared']
num = [230, 100, 98]
ax1.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
ax1.set_title('Piechart (Subplot 1)')

#Plot Bar Chart (Subplot 2)

plt.bar(labels, num, color=['lightblue', 'lightgreen', 'yellow'])
ax2.set_title('Bare Chart (Subplot 2)')
ax2.set_xlabel('Candidate')
fig.suptitle('Voting Results', size=14)

plt.show()
