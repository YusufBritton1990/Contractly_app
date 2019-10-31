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
campaign_url = f"{url}/campaigns"

"""HTML Templates functions"""
# Index, used in Bootstrap
def index(request):
    return render(request, 'index.html')

# >>> requests.post('https://httpbin.org/post', data={'key':'value'})
# >>> requests.put('https://httpbin.org/put', data={'key':'value'})

"""MailChimp Campaigns REST request functions"""

def campaign_retreive_all(request):

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.get(
        campaign_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)
    # return JsonResponse({r}, safe=False)


def campaign_creation(request):

    data = {
        "type": "regular",
        "settings":
        {
            "subject_line": 'test Django',
            "from_name": 'Yusuf',
            "reply_to": MC_USER
        }
    }

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.post(
        campaign_url,
        auth = ("",MC_API),
        data = json.dumps(data)
    )

    return HttpResponse(r)

def campaign_update(request):

    # Still having issues with this
    #https://mailchimp.com/developer/reference/campaigns/campaign-content/#put_/campaigns/-campaign_id-/content

    campaign_id = 'c2df2c2e25'
    update_url = f"{campaign_url}/{campaign_id}/content"

    data = {
        "html": "<h1>Hello, my guy</h1>",
    }

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.put(
        update_url,
        auth = ("",MC_API),
        data = json.dumps(data)
    )

    return HttpResponse(r)
