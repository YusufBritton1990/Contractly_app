from django.shortcuts import render #Processes HTML
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse, JsonResponse #needed to show a response in browser

import json
import requests

# Mailchimp credentials, defined in settings.py
MC_API = settings.MAILCHIMP_API_KEY
MD_DC = settings.MAILCHIMP_DATA_CENTER
MC_AUD = settings.MAILCHIMP_AUD_ID #AKA List ID
MC_USER = settings.USER_EMAIL

# URL endpoint
url =  f"https://{MD_DC}.api.mailchimp.com/3.0/"
list_url = f"{url}/lists"
partial_url = f"{list_url}?fields=lists.name,lists.id"
segment_url = f"{list_url}/{MC_AUD}/segments"

# print(MC_AUD)

"""MailChimp List REST request functions"""

def list_retreive_all(request):

    r = requests.get(
        list_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)

def partial_retreive_all(request):

    # See if there is a way to return back IDs to use, in general
    r = requests.get(
        partial_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)

"""MailChimp Segment REST request functions"""
def segment_retreive_all(request):

    r = requests.get(
        segment_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)
