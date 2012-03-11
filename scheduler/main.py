import time
from services.pypi.actions import FetchCatalog
from services.pypi.actions import FetchChangeLog
from services.eventscheduler import EventScheduler

def main():
    scheduler = EventScheduler()
    FetchCatalog().execute()
    #scheduler.schedule_interval_task(FetchCatalog(), seconds=5)
    #scheduler.schedule_interval_task(FetchChangeLog(), seconds=10)

    #while True:
    #    time.sleep(1)

if __name__ == "__main__":
    main()