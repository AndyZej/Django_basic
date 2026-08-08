import random
from django.http import HttpResponse


def random_number(request):
    number = random.randint(0, 100)

    return HttpResponse(f"Drawn number: {number}"