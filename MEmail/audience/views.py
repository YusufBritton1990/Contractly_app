from django.shortcuts import render #Processes HTML
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse, JsonResponse #needed to show a response in browser

import json
import requests
import hashlib #hexidex needed to update contacts

# Mailchimp credentials, defined in settings.py
MC_API = settings.MAILCHIMP_API_KEY
MD_DC = settings.MAILCHIMP_DATA_CENTER
MC_AUD = settings.MAILCHIMP_AUD_ID #AKA List ID
MC_USER = settings.USER_EMAIL

# IDs
#This is used to make the users in the test segment recipients
testing_seg_id = 152241

# Hash encrpytion of email, needed to update contact
result = hashlib.md5(MC_USER.encode())
email_hexa = result.hexdigest()

# URL endpoint
url =  f"https://{MD_DC}.api.mailchimp.com/3.0/"
list_url = f"{url}/lists"
partial_url = f"{list_url}?fields=lists"
segment_url = f"{list_url}/{MC_AUD}/segments"
merge_url = f"{list_url}/merge-fields"
members_url = f"{segment_url}/{testing_seg_id}/members"

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

"""MailChimp Merge fields REST request functions"""
def merge_retreive_all(request):
    r = requests.get(
        segment_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)

"""MailChimp members fields REST request functions"""

#interacting with members
# https://mailchimp.com/developer/guides/manage-subscribers-with-the-mailchimp-api/

# members API directory
# https://mailchimp.com/developer/reference/lists/list-segments/list-segment-members/#post_/lists/-list_id-/segments/-segment_id-/members

def members_retreive_all(request):
    r = requests.get(
        members_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)
