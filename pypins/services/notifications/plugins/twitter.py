class TwitterNotifier(object):

    def __call__(self, notification):
        print(notification.package.name)
        for user in notification.users:
            # send twitter notification here
            print(user.name)