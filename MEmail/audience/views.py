from django.shortcuts import render #Processes HTML
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse, JsonResponse #needed to show a response in browser

import json
import requests

# Mailchimp credentials, defined in settings.py
MC_API = settings.MAILCHIMP_API_KEY
MD_DC = settings.MAILCHIMP_DATA_CENTER
MC_AUD = settings.MAILCHIMP_AUD_ID
MC_USER = settings.USER_EMAIL

# URL endpoint
url =  f"https://{MD_DC}.api.mailchimp.com/3.0/"
aud_endpoint = f"{url}/lists/{MC_AUD}"


"""MailChimp Campaigns REST request functions"""

def list_retreive_all(request):

    # # Used to post to user endpoint. Data is converted to a JSON
    # r = requests.get(
    #     campaign_url,
    #     auth = (MC_USER,MC_API)
    # )
    #
    # return HttpResponse(r)
    pass
