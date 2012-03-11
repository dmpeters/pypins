import sys
# so we can include the pypins package in the search path
sys.path.append("../")


import time
from services.pypi.actions import FetchCatalog
from services.pypi.actions import FetchChangeLog
from services.eventscheduler import EventScheduler


def main():
    scheduler = EventScheduler()

    #scheduler.schedule_interval_task(FetchCatalog(), hours=24)
    #scheduler.schedule_interval_task(FetchChangeLog(), seconds=10)

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()