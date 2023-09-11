from twilio.rest import Client

class Sender:
    def __init__(self, account_sid , auth_token):
        import pdb; pdb.set_trace()
        self.client = Client(account_sid, auth_token)
    
    def send(self, sender_number, card_path, receiver_number):
        message = self.client.messages.create(
        body='Choudhary Family Cordially Invites you',
        from_='whatsapp:+91'+sender_number,  # Your Twilio WhatsApp number
        media_url=[card_path],  # URL of the document to send
        to='whatsapp:+91'+receiver_number  # Recipient's WhatsApp number
        )

if __name__ == "__main__":
    phone_number = '7014556915'
    receiver_number = '8005696966'
    card_path = "D:\Sakshi\weddinginvitation\output\Mool Chand Dinesh Chand Ji Sa Shrimal.pdf"
    sid = 'ACa8f61ed047d8c24bf920ba56050c1763'
    token = 'a13764ebac2b21e0da35fb133c9eac04'
    obj = Sender(sid, token)
    obj.send(phone_number, card_path, receiver_number)

