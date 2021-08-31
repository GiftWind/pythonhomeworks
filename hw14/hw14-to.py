import Employee
import pickle

with open('alice', 'rb') as f:
    alice = pickle.load(f)

alice.print_salary_info()
print(alice.phone)