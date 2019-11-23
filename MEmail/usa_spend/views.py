from django.shortcuts import render
from django.http import HttpResponse

import requests
import datetime
import json #was able to work without it, but filter isn't working

# API Endpoints
url = f"https://api.usaspending.gov/api/v2"
visual_url = f"{url}/search/spending_by_category/"
naics_url = f"{url}/autocomplete/naics/"

# Dates
# Fiscal year is 10/1/prior year to 09/30/current year. The most current could be 10/1/cuurent to 09/30/current year after 9/30
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

FY = 2020

start_date = f'{FY - 1}-10-01'
end_date = f'{year}-{month}-{day}'

def dept_spending(request):
    payload = {
        'category': 'awarding_agency',
        'filters' : {
            'time_period':[{
                'start_date': start_date,
                'end_date': end_date
            }],
            'place_of_performance_locations' : [{
                'country' : 'USA',
                'state' : 'NJ'
            }],
            'naics_codes':['518210']
        },
        'limit': 3
    }

    r = requests.post(
        visual_url,
        data = json.dumps(payload),
        headers = {'Content-type': 'application/json'}
    )

    # return HttpResponse(r.headers)
    # return HttpResponse(r.status_code)
    return HttpResponse(r)
