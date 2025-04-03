import asyncio
from time import sleep
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import classonlymethod

# Synchronous Views
def ping(request):
    return JsonResponse({"message": "pong"})


def cpu_bound(request):
    count = 0
    for _ in range(1_000_000):
        count += 1
    return JsonResponse({"message": "CPU Bound"})


def io_bound(request):
    sleep(0.1)
    return JsonResponse({"message": "IO Bound"})


async def async_ping(request):
    return JsonResponse({"message": "pong"})


async def async_cpu_bound(request):
    count = 0
    for _ in range(1_000_000):
        count += 1
    return JsonResponse({"message": "CPU Bound"})


async def async_io_bound(request):
    await asyncio.sleep(0.1)
    return JsonResponse({"message": "IO Bound"})
