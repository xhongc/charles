from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'charles.chat'

    def ready(self):
        import charles.chat.receivers
