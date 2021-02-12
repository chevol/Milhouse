import secrets
from twilio.rest import Client

class twilio:
    def send_notification(self,url):
        twilio_client = self.setup_twilio_client()
        twilio_client.messages.create(
            body="Your item is now available!" + url,
            from_=secrets.twilio_from_number,
            to=secrets.twilio_send_sms_to
        )

    def setup_twilio_client(self):
        account_sid = secrets.twilio_sid
        auth_token = secrets.twilio_token
        return Client(account_sid, auth_token)
