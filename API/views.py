# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from API.models import APIModel
from API.serializer import APISerializer
import logging
import traceback
# Create your views here.
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log.log',
    format='%(name)s - %(levelname)s - %(message)s',
    level='ERROR'
)
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def API_resource(request):
    logger.debug('{} - {}'.format(request.method, request.path))
    try:
        if request.method == 'GET':
            data = APIModel.objects.all()
            serializer = APISerializer(data, many=True)
            return JSONResponse(serializer.data)
    
        elif request.method == 'POST':
            data = JSONParser().parse(request)
        logger.debug('data: {}'.format(data))
        serializer = APISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    except:
        logger.error(traceback.format_exc())
        return HttpResponse(status=500)

@csrf_exempt
def API_resource_id(request, id):
    logger.debug('{} - {}'.format(request.method, request.path))
    try:
        try:
            data_property = APIModel.objects.get(id=id)
        except:
            logger.error('Error in ID: {}'.format(id))
            return HttpResponse(status=404)
    
        if request.method == 'GET':
            serializer = APISerializer(data_property)
            return JSONResponse(serializer.data)
    
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            logger.debug('data: {}'.format(data))
            serializer = APISerializer(data_property, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)
    
        elif request.method == 'DELETE':
            data_property.delete()
            return HttpResponse(status=204)
    except:
        logger.error(traceback.format_exc())
        return HttpResponse(status=500)