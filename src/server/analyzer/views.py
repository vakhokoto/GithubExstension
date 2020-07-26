from django.http import HttpResponse
from analytic import Fetcher, RepoAnalyzer, Homepage
import logging, os, magic
from github import Github

logger = logging.getLogger(__name__)

def token_initialize_view(request):
    token = request.GET['token']
    user = Github(token)
    print('this is token')
    response = HttpResponse('Account identified successfully')
    response.status_code = 200
    response.set_cookie("user", user)

    return response

def any_view(request, url):
    try:
        file = open('../my-app/build/' + url, 'rb')
        mime = magic.Magic(mime=True)

        response = HttpResponse(file.read(), content_type=mime.from_file('../my-app/build/' + url))
        logger.info("responsed to " + url)
        return response
    except:
        response = HttpResponse("Internal server error")
        response.status_code = 500
        return response