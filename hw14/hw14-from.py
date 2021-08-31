# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.

import pickle
from Employee import Employee

alice = Employee('Alice Wonderland', '+7(999)999-9999', 19999)
with open('alice', 'wb') as f:
    # Протокол 3 используется по умолчанию, но лучше указывать явно 
    pickle.dump(alice, f, protocol=3)

alice.print_salary_info()
print(alice.phone)
