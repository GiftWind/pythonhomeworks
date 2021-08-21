# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.

import pickle
from Employee import Employee

alice = Employee('Alice Wonderland', '+7(999)999-9999', 19999)
f = open('alice', 'wb')
pickle.dump(alice, f)
f.close()
alice.print_salary_info()
