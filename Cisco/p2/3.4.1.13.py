class WeekDayError(ValueError):
    pass

class Weeker:
    days=["Lun","Mar","Mie","Jue","Vie","Sab","Dom"]

    def __init__(self, day):
        try:
            self.d=Weeker.days.index(day)
        except:
            raise WeekDayError

    def __str__(self):
        return Weeker.days[self.d]

    def add_days(self, n):
        self.d=(self.d+n)%7

    def subtract_days(self, n):
        self.d=(self.d-n)%7


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('NotLun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
