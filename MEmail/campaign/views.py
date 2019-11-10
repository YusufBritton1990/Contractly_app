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
templates_url = f"{url}/templates"

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

def campaign_content(request):

    campaign_id_reg = 'c2df2c2e25'
    campaign_id_plain = 'ee666a8d2e'
    content_url = f'{campaign_url}/{campaign_id_reg}/content'

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.get(
        campaign_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)


def campaign_creation(request):

    data = {
        "type": "plaintext",
        "settings":
        {
            "subject_line": 'test Django - plaintext',
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

    # Getting Message field error
    #https://mailchimp.com/developer/reference/campaigns/campaign-content/#put_/campaigns/-campaign_id-/content

    campaign_id_reg = 'c2df2c2e25'
    # campaign_id_plain = 'ee666a8d2e'
    # web_id = 333993
    update_url = f"{campaign_url}/{campaign_id_reg}/content"

    htm = "<h1>The guy, I am the guy</h1>... here a link <a href='https://www.w3schools.com/html/'>Visit our HTML tutorial</a>"

    # Template ID
    temp_id = 78517

    data = {
        # "plaintext": render(request, 'index.html')
        # "html": render(request, 'contract_template.html')
        # "html": htm
        "template": {"id": temp_id}
    }

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.put(
        update_url,
        auth = ("",MC_API),
        data = json.dumps(data)
    )

    # return HttpResponse(r)
    return HttpResponse(r)

"""MailChimp Templates REST request functions"""

def get_template(request):

    temp_id = '78517'
    temp_id_url = f'{templates_url}/{temp_id}'

    # Used to post to user endpoint. Data is converted to a JSON
    r = requests.get(
        temp_id_url,
        auth = (MC_USER,MC_API)
    )

    return HttpResponse(r)
    # return JsonResponse({r}, safe=False)

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
