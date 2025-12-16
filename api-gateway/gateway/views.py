import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def proxy_request(request, service, path=''):
    service_url = settings.SERVICE_URLS.get(service)
    
    if not service_url:
        return JsonResponse({'error': 'Service not found'}, status=404)
    
    url = f"{service_url}/{path}"
    
    # Forward headers
    headers = {}
    if 'HTTP_AUTHORIZATION' in request.META:
        headers['Authorization'] = request.META['HTTP_AUTHORIZATION']
    if 'CONTENT_TYPE' in request.META:
        headers['Content-Type'] = request.META['CONTENT_TYPE']
    
    try:
        # Forward request
        if request.method == 'GET':
            response = requests.get(url, headers=headers)
        elif request.method == 'POST':
            response = requests.post(url, headers=headers, data=request.body)
        elif request.method == 'PUT':
            response = requests.put(url, headers=headers, data=request.body)
        elif request.method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
        
        # Return response
        return HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type', 'application/json')
        )
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def health(request):
    return JsonResponse({
        'status': 'healthy',
        'service': 'API Gateway',
        'port': 8080
    })