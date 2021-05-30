#!/usr/bin/python3

from joblib import load
import sys

model = load('salarypred.pk1')
print()

if sys.argv[1] == 'None':
    while True:
        exp = float(input("\nPlease Enter Years of Experience: "))
        salary = round(*model.predict([[exp]]), 2)
        print("Estimated Salary: {0}\n".format(salary))
        choice = input("Want to Predict More (Y/N): ").lower()
        if (choice == "y" or choice == 'yes'):
            pass
        else:
            break
else:
    for exp in sys.argv[1:]:
        salary = round(*model.predict([[float(exp)]]), 2)
        print("Estimated Salary for {0} Experience: {1}".format(exp, salary))

print()