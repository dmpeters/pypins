from apscheduler.scheduler import Scheduler

class AdvancedPythonScheduler(object):
    
    def __init__(self):
        self.scheduler = Scheduler()
        self.scheduler.start()

    def schedule_interval_task(self, action, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        self.scheduler.add_interval_job(action, weeks, days, hours, minutes, seconds)