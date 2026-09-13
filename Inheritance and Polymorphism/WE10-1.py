class Employee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # This method is intended to be overridden by subclasses to calculate the weekly wage based on hours worked.
    def get_weekly_wage(self, hours_worked=None):
        raise NotImplementedError("Subclasses must implement this method.")

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate):
        super().__init__(name)
        self._hourly_rate = hourly_rate

    def get_weekly_wage(self, hours_worked=None):
        if hours_worked is None:
            raise ValueError("Hours worked is required.")
        elif hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        elif hours_worked < 40:
            return self._hourly_rate * hours_worked
        else:
            overtime_hours = hours_worked - 40
            return (self._hourly_rate * 40) + (self._hourly_rate * 1.5 * overtime_hours)

class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self._salary = salary

    def get_weekly_wage(self,hours_worked=None):
        week =  52
        return self._salary / week

class Manager(SalariedEmployee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self._bonus = bonus


    def get_weekly_wage(self, hours_worked=None):
        return super().get_weekly_wage() + self._bonus  # Example wage for a manager plus bonus

staff = []
staff.append(HourlyEmployee("Alice", 20))
staff.append(HourlyEmployee("Alex", 50))
staff.append(SalariedEmployee("Bob", 52000))
staff.append(Manager("Charlie", 104000, 500))

for employee in staff:
    hours = int(input(f"Enter hours worked for {employee.get_name()}: "))
    pay = employee.get_weekly_wage(hours) 
    print(f"{employee.get_name()} earned ${pay:.2f} this week.")