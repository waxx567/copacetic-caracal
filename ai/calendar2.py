'''
Write a Python class named Calendar that manages scheduled appointments. The class should:
Store appointments that keep track of: the date, start time, end time, and appointment name.
Include methods to check if a time slot is free (is_free), check if a time slot is busy (is_busy), schedule an appointment (schedule_time), and delete an event by name (delete_event).
Comment the code and write code as efficiently as possible.
'''
class Calendar:
    def __init__(self):
        self.appts = []

    def is_free(self, date, start, end):
        free = True
        for d, s, e, _ in self.appts:
            if d == date and (end > s or start < e):
                free = False
        return free

    def is_busy(self, date, start, end):
        return not self.is_free(date, start, end)

    def schedule_time(self, date, start, end, name):
        if self.is_free(date, start, end):
            self.appts.append((date, start, end, name))
            self.appts.sort(key=lambda x: (x[0], x[1]))
            return True
        return False

    def delete_event(self, name):
        count = len(self.appts)
        self.appts = [a for a in self.appts if a[3] != name]
        if len(self.appts) == count:
            return f"Event '{name}' not found."
        else:
            return f"Event '{name}' deleted successfully."