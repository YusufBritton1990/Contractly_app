from django.shortcuts import render
from django.conf import settings #Needed to get enviromental variable
from django.http import HttpResponse

import requests
import datetime
import json #was able to work without it, but filter isn't working

"""Testing pulling contracts"""

# https://open.gsa.gov/api/get-opportunities-public-api/

BETA_API = settings.BETA_SAM_API



url = "https://api.sam.gov/prod/opportunities/v1/search"
limit_url = f"{url}?limit=10"
api_key = BETA_API
postedFrom = "12/01/2019"
postedTo = "12/18/2019"
posted = f"postedFrom={postedFrom}&postedTo={postedTo}"
beta_url = f"{limit_url}&api_key={api_key}&{posted}"
# https://api.sam.gov/prod/opportunities/v1/search?limit=10&api_key={User’s Public API Key}&postedFrom=01/01/2018&postedTo=05/10/2018

def contracts(request):
    # TODO: Need to add dates
    r = requests.get(
        beta_url
        # headers = {'Content-type': 'application/json'}
    )

    return HttpResponse(r)
