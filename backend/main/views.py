from django.http import HttpResponse

from rest_framework.views import APIView

class testView(APIView):
    def get(self, request):
        return HttpResponse(status=200)
