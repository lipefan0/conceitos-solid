from .notificator_interface import NotificatorInterface

class NotificatorSms(NotificatorInterface):
    def send_notification(self, message: str):
        print(f"Sending sms notification: {message}")