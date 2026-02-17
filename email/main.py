import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import abort

def send_email(request):
    if request.method != 'POST':
        abort(405)

    bearer_token = request.headers.get('Authorization').split()[1]
    secret_key = os.environ.get('ACCESS_KEY')
    print(f"Bearer Token: {bearer_token}")
    print(f"secret Key:{secret_key}")
    if bearer_token != secret_key:
        abort(401)

    request_json = request.get_json(silent=True)
    parameters = ('sender', 'receiver', 'subject', 'message')
    sender, receiver, subject, message = '', '', '', ''

    if request_json:
    #if request_json and all(k in request_json for k in parameters):
        print("Testing")
        sender = request_json['sender']
        receiver = request_json['receiver']
        subject = request_json['subject']
        message = request_json['message']
        print(f"Sender:{sender}")
        print(f"Receiver:{receiver}")
        print(f"Subject:{subject}")
        print(f"message:{message}")
        email_message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=message)
        #return 'OK', 200
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            # sg.set_sendgrid_data_residency("eu")
            # uncomment the above line if you are sending mail using a regional EU subuser
            print(f"Sending email")
            sg.send(email_message)
            return 'OK', 200
        except Exception as e:
            return e, 400
    else:
        abort(400)

