def avg(marks):
    assert len(marks) != 0
    return round(sum(marks)/len(marks), 2)

sem_1marks = [62, 65, 75]
print("Average marks for semester 1:",avg(sem_1marks))

ranks = []
print("Avg of marks for semester 1:", avg(ranks))
