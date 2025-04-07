'''
Write a Python class named Calendar that manages scheduled appointments. The class should:
Store appointments that keep track of: the date, start time, end time, and appointment name.
Include methods to check if a time slot is free (is_free), check if a time slot is busy (is_busy), schedule an appointment (schedule_time), and delete an event by name (delete_event).
Comment the code and write code as efficiently as possible.
'''
class Calendar:
    def __init__(self):
        # Stores scheduled as tuples (date, start, end, name)
        self.appointments = []

    def is_free(self, date, time_start, time_end):
        """Check if a time slot is free on a given date."""
        for appt_date, start, end, _ in self.appointments:
            if appt_date == date and not (time_end <= start or time_start >= end):
                return False  # Overlapping time slot found
        return True

    def is_busy(self, date, time_start, time_end):
        """Check if a time slot is busy on a given date."""
        return not self.is_free(date, time_start, time_end)

    def schedule_time(self, date, time_start, time_end, name):
        """Schedule a new time slot if available on a given date."""
        if self.is_free(date, time_start, time_end):
            self.appointments.append((date, time_start, time_end, name))
            # Sort by date, then start time
            self.appointments.sort(key=lambda appt: (appt[0], appt[1]))
            return True
        return False

    def delete_event(self, name):
        """Delete an event by name."""
        initial_count = len(self.appointments)
        self.appointments = [
            appt for appt in self.appointments if appt[3] != name]
        if len(self.appointments) == initial_count:
            return f"Event '{name}' not found."
        return f"Event '{name}' deleted successfully."