from django.http import HttpResponse,HttpResponseBadRequest
from .models import ImageForm
from django.views.decorators.http import etag
import hashlib

def index(request):
    return HttpResponse('Hello World')

def generate_etag(request,width,height):
    content = 'Placeholder: {0} x {1}'.format(width,height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()
@etag(generate_etag)
def placeholder(request,width,height):
    # urlから渡されたheightとwidthをImageFormに渡す
    form = ImageForm({'height':height,'width':width})
    # validationがうまく行けばImageFormのgenerateで画像生成
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image,content_type='image/png')
    else :
        return HttpResponseBadRequest('Invalid Image Request')

