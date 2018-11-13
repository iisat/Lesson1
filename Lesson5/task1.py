from collections import namedtuple

Company = namedtuple('Company', 'name, q1, q2, q3, q4')

companies = (int(input('Какое количество компаний оценить?: ')))
all_companies = []

for i in range(companies):
    name = input('Имя компании: ')
    q1 = int(input('Прибыль Q1: '))
    q2 = int(input('Прибыль Q2: '))
    q3 = int(input('Прибыль Q3: '))
    q4 = int(input('Прибыль Q4: '))
    all_companies.append(Company(name, q1, q2, q3, q4))

allprofit = 0

for i in range(companies):
    allprofit += all_companies[i].q1 + all_companies[i].q2 + all_companies[i].q3 + all_companies[i].q4

avgprofit = allprofit / companies

print('Компании с прибылью ниже среднего: ')
for i in range(companies):
    if (all_companies[i].q1 + all_companies[i].q2 + all_companies[i].q3 + all_companies[i].q4 < avgprofit):
        print(all_companies[i].name)
print('Компании с приыблью выше среднего: ')
for i in range(companies):
    if (all_companies[i].q1 + all_companies[i].q2 + all_companies[i].q3 + all_companies[i].q4 > avgprofit):
        print(all_companies[i].name)