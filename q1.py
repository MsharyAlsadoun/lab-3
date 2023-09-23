employee_data = {}

while True:
    name = input("Enter employee name or 'q' to exit: ")
    if name == "q":
        break

    salary = float(input("Enter employee salary: "))
    employee_data[name] = salary
    
print("\nEmployee Dictionary:")
for name, salary in employee_data.items():
    print(f"Name: {name}, Salary: {salary}")