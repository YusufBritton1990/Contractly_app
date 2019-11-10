# Contractly_app

Steps:

Testing with Mailchimp to include contract data using mail tags


Links

My project url, which is including the campaign app's urls
C:\Users\Youth\Desktop\Django\MailChimp Campaign test\MEmail\MEmail\urls.py

My campaign urls, which triggers my GET, PUSH, and PUT calls. GET is retrieving the campaign, PUSH is creating it, and PUT is supposed to update it with content
C:\Users\Youth\Desktop\Django\MailChimp Campaign test\MEmail\campaign\urls.py

This has my function definitions that invoke with the url calls.
C:\Users\Youth\Desktop\Django\MailChimp Campaign test\MEmail\campaign\views.py


MEmail/MEmail/settings.py

# Used to make connection for REST API requests
MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
74a46a82bdcac8c8ccef706697382480-us20

#last 4 digits of API Key
MAILCHIMP_DATA_CENTER = os.environ['MAILCHIMP_API_KEY'][-4:]
us20

# Access Audience in Mailchimp
MAILCHIMP_AUD_ID = os.environ['MAILCHIMP_AUD_ID']
7ebe092403

USER_EMAIL = os.environ['BUSN_EMAIL']
ybritton@ykbanalytics.com

MailChimp password
M1$$ymama

Let me know if you are logging in
