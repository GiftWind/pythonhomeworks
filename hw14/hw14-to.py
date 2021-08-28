from Employee import Employee
import pickle

f = open('alice', 'rb')
alice = pickle.load(f)
f.close()

alice.print_salary_info()