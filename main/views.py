from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
import requests
import json

@login_required
@permission_required('main.index_viewer', raise_exception=True)
def index(request):
    current_url = request.build_absolute_uri()
    url = current_url + '/api/v1/landing'
    response_http = requests.get(url)
    response_dict = json.loads(response_http.content)

    total_responses = len(response_dict.keys())
    responses = response_dict.values()

    data = {
        'title': 'Landing - Dashboard',
        'total_responses': total_responses,
        'responses': responses,
        'primero': list(responses)[0],
        'ultimo': list(responses)[-1],
    }
    # return HttpResponse(b"Hello, World!")
    return render(request, 'main/index.html', data)
