import os


URL = os.environ.get('MAILGUN_DOMAIN')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = "Do-Not-Reply@sandbox51d3a75be9f5412b8436320839512271.mailgun.org"
ALERT_TIMEOUT = 10
COLLECTION = "alerts"
