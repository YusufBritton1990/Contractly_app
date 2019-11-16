from django.shortcuts import render
from django.http import HttpResponse

import requests

# API Endpoints
url = f"https://api.usaspending.gov/api/v2"

def dept_spending(request):
    visual_url = f"{url}/search/spending_by_category/"

    data = {
        'category': 'awarding_agency'
    }

    r = requests.post(
        visual_url,
        data = data
    )

    return HttpResponse(r)
