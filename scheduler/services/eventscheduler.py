from services.events.aps import AdvancedPythonScheduler

class EventScheduler(object):
    
    def __init__(self):
        self.scheduler = AdvancedPythonScheduler()
    
    def schedule_interval_task(self, action, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        self.scheduler.schedule_interval_task(action, weeks, days, hours, minutes, seconds)


