from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from django.http.response import JsonResponse
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import EmployeeForm
# Create your views here.
def isValidJson( data):
    try:
        json.loads(data)
        return True
    except:
        return False
class Employeeparticular(View):
    def get(self, request,id, *args, **kwargs):
        try:
            emp = Employee.objects.get(empid=id)
        except:
            response = {"resp": "requested resource not persent"}
            return JsonResponse(response, status=500)
        else:
            response = serialize('json', [emp,])
            return HttpResponse(response, content_type='application/json', status=200)
    def put(self, request,empid, *args, **kwargs):
        try:
            emp = Employee.objects.get(empid=empid)
        except Employee.DoesNotExist:
            response = {"resp": "resource  to be updated doesnotexist"}
            return JsonResponse(response, status=500)
        else:
            isjson = isValidJson(request.body)
            if not isjson:
                err_message = {"msg": "give json data only"}
                return HttpResponse(json.dumps(err_message), content_type='application/json', status=400)
            valid_data = json.loads(request.body)
            json_data = serialize("json", [emp, ])
            json_data = json.loads(json_data)
            original = {
                "empid": json_data[0]["pk"],
                "empname": json_data[0]["fields"]["empname"],
                "empage": int(json_data[0]["fields"]["empage"]),
                "empexp": int(json_data[0]["fields"]["empexp"])
            }
            original.update(valid_data)
            form =EmployeeForm(original, instance=emp)
            form.save(commit=True)
            response = {"msg": "resource updated successfully"}
            return HttpResponse(json.dumps(response), content_type='application/json', status=200)

class EmployeeList(View):

    def get(self, request, *args, **kwargs):
        try:
            emplist = Employee.objects.all()
        except:
            response = {"resp": "requested resource not persent"}
            return JsonResponse(response, status=500)
        else:
            response = serialize('json', emplist)
            return HttpResponse(response, content_type='application/json', status=200)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        given_data = request.body
        valid_json = isValidJson(given_data)
        if not valid_json:
            err_message = {"msg": "give json data only"}
            return HttpResponse(json.dumps(err_message), content_type='application/json', status=400)
        valid_data = json.loads(given_data)
        form = EmployeeForm(valid_data)
        try:
            form.save(commit=True)
            response = {"msg": "resource created successfully"}
            return HttpResponse(json.dumps(response), content_type='application/json', status=200)
        except:
            error = {"msg": "Error in resource creation"}
            return HttpResponse(json.dumps(error), content_type='application/json', status=200)
