class TwitterNotifier(object):

    def __call__(self, notification):
        print notification.package.name
        for user in notification.users:
            print user.name