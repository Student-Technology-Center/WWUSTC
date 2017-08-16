from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from login.models import Shift, ShiftForm

@require_http_methods(['GET'])
def get_user_shifts(request):

    shift_info = [{
        "start": str(i.start_time),
        "end": str(i.end_time),
        "day": i.day_of_week
        }
                  for i in request.user.shift_set.all()
                 ]

    return JsonResponse(shift_info, safe=False)

@require_http_methods(['POST'])
def add_shift(request):
    if request.POST.get('shift'):
        shift_form = ShiftForm(request.POST)
        if shift_form.is_valid():
            new_shift = shift_form.save(commit=False)
            new_shift.user = request.user
            new_shift.save()

    return redirect('/')