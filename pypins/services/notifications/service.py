from pypins.services.notifications.plugins.twitter import TwitterNotifier
from pypins.dao.services.models import Notification

class NotificationsService(object):
    def __init__(self):
        pass
    
    def register(self, package, user):
        try:
            self.notifications[package.name].users.append(user)
        except KeyError:
            notification = Notification()
            notification.package = package
            notification.users.append(user)
            self.notifications[package.name] = notification

    def __enter__(self):
        self.notifications = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        notifications = self.notifications
        
        plugins = [TwitterNotifier()]
        
        for key in notifications:
            notification = notifications[key]
            for plugin in plugins:
                plugin(notification)
        
        return True