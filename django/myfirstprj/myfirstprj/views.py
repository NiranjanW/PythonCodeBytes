
from django.http import HttpResponse
from django.http.request import HttpRequest

def sum_odd_numbers(request: HttpRequest , n: int) -> HttpResponse:
    v = 0

    for i in range(n):
        if  i% 2 == 1:
            v += 1
    return HttpResponse(v)