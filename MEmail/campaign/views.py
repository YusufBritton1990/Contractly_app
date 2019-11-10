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
campaign_url = f"{url}/campaigns"
templates_url = f"{url}/templates"

# IDs
# campaign_id_reg = 'c2df2c2e25' #Deleted from MC
# campaign_id_plain = 'ee666a8d2e' #Deleted from MC
temp_id = 78517
aud_seg_id = 152241

"""HTML Templates functions"""
# Index, used in Bootstrap
def index(request):
    return render(request, 'index.html')

# >>> requests.post('https://httpbin.org/post', data={'key':'value'})
# >>> requests.put('https://httpbin.org/put', data={'key':'value'})

"""MailChimp Campaigns REST request functions"""

# See all campaigns
def campaign_retreive_all(request):
    r = requests.get(
        campaign_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)

# View content of campaign
def campaign_content(request):
    content_url = f'{campaign_url}/{campaign_id_reg}/content'

    r = requests.get(
        campaign_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)

# Create a new campaign
def campaign_creation(request):

    # Documentation
    # https://mailchimp.com/developer/reference/campaigns/#post_/campaigns
    data = {
        "type": "regular",
        "recipients":
        {
            "list_id": MC_AUD,
            "segment_opts" : {
                "saved_segment_id" : aud_seg_id
            }
        },
        "settings":
        {
            "subject_line": 'test Django - regular',
            "preview_text" : 'Preview text for *|FNAME|*',
            "to_name" : "*|FNAME|*",
            "from_name": 'Yusuf',
            "reply_to": MC_USER,
            "template_id" : temp_id
        }
    }

    r = requests.post(
        campaign_url,
        auth = ("",MC_API),
        data = json.dumps(data)
    )

    return HttpResponse(r)

def campaign_update(request):
    # Template ID
    temp_id = 78517

    update_url = f"{campaign_url}/{campaign_id_reg}/content"

    data = {
        "template": {"id": temp_id}
    }

    r = requests.put(
        update_url,
        auth = ("",MC_API),
        data = json.dumps(data)
    )

    return HttpResponse(r)

"""MailChimp Templates REST request functions"""
# Currently not in use, but can look into it if I want to use editable fields

def get_template(request):

    temp_id = '78517'
    temp_id_url = f'{templates_url}/{temp_id}'

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.get(
        temp_id_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)

def template_content(request):
    # Look at making editable sections to make campaigns. May need the 14.99 plan to do it
    # https://www.google.com/search?q=mailchimp+editable+sections+in+template&rlz=1C1CHBF_enUS779US779&sxsrf=ACYBGNTDIWSeskGbsrKAyWLg5Vf4pB55dA:1573218331421&source=lnms&tbm=vid&sa=X&ved=0ahUKEwi8pbH-1trlAhWGTN8KHXkOBIMQ_AUIEygC&biw=1707&bih=813&dpr=1.13

    temp_id = '78517'
    temp_id_url = f'{templates_url}/{temp_id}/default-content'

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.get(
        temp_id_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)
    # return JsonResponse({r}, safe=False)
