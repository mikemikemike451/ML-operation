class Appointment:
    def __init__(self, date, description):
        self.date = date
        self.description = description
    # abstract method
    def occursOn(self,date):
        raise NotImplementedError("Subclasses must implement this method")
    def getDescription(self):
        return self.description
    def newAppointment(self, date, description):
        self.date = date
        self.description = description

class Onetime(Appointment):
    def __init__(self, date, description):
        super().__init__(date, description)
    def occursOn(self, date):
        return self.date['year'] == date['year'] and self.date['month'] == date['month'] and self.date['day'] == date['day']

class Daily(Appointment):
    def __init__(self, date, description):
        super().__init__(date, description)
    def occursOn(self, date):
        return True

class Monthly(Appointment):
    def __init__(self, date, description):
        super().__init__(date, description)
    def occursOn(self, date):
        return self.date['day'] == date['day']

year = int(input('Enter the year of the appointment (YYYY):'))
month = int(input('Enter the month of the appointment (MM):'))
day = int(input('Enter the day of the appointment (DD):'))
date = {'year': year, 'month': month, 'day': day}

appointments = []
appointments.append(Onetime({'year': 2026, 'month': 9, 'day': 24}, 'Doctor Appointment'))
appointments.append(Daily({'year': 2026, 'month': 9, 'day': 23}, 'Daily Exercise'))
appointments.append(Monthly({'year': 2026, 'month': 9, 'day': 24}, 'Monthly Meeting'))

for appointment in appointments:
    if appointment.occursOn(date):
        print(f"Appointment: {appointment.getDescription()} occurs on {date['year']}-{date['month']}-{date['day']}")
        