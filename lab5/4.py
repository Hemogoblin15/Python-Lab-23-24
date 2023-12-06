class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def assign_tasks(self):
        print(f"Manager {self.name} is assigning tasks to the team in the {self.department} department")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def code(self):
        print(f"Engineer {self.name} is coding in {self.programming_language}")


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_quota):
        super().__init__(name, employee_id, salary)
        self.sales_quota = sales_quota

    def meet_quota(self):
        print(f"Salesperson {self.name} is working to meet the sales quota of ${self.sales_quota}")


manager_instance = Manager("George", "M123", 80000, "Sales")
engineer_instance = Engineer("Mihai", "E456", 90000, "Python")
salesperson_instance = Salesperson("Marius", "S789", 75000, 100000)

manager_instance.assign_tasks()
engineer_instance.code()
salesperson_instance.meet_quota()

print(f"{manager_instance.name}'s salary: ${manager_instance.salary}")
print(f"{engineer_instance.name}'s employee ID: {engineer_instance.employee_id}")
print(f"{salesperson_instance.name}'s sales quota: ${salesperson_instance.sales_quota}")
