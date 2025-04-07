'''
Write a Python class named Calendar that manages scheduled appointments. The class should:
Store appointments that keep track of: the date, start time, end time, and appointment name.
Include methods to check if a time slot is free (is_free), check if a time slot is busy (is_busy), schedule an appointment (schedule_time), and delete an event by name (delete_event).
Comment the code and write code as efficiently as possible.
'''
class Calendar:
    def __init__(self):
        # Stores scheduled appointments as tuples (date, start, end, name)
        self.appointments = []

    def is_free(self, date, time_start, time_end):
        # Check for free timeslot
        for appt_date, start, end, _ in self.appointments:
            if appt_date == date and not (time_end <= start or time_start >= end):
                return False
        return True