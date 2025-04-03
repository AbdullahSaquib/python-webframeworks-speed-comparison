from django.urls import path
from .views import ping, cpu_bound, io_bound, async_ping, async_cpu_bound, async_io_bound

urlpatterns = [
    path("sync-ping", ping, name="sync_ping"),
    path("sync-cpu-bound", cpu_bound, name="sync_cpu_bound"),
    path("sync-io-bound", io_bound, name="sync_io_bound"),

    # Async versions
    path("async-ping", async_ping, name="async_ping"),
    path("async-cpu-bound", async_cpu_bound, name="async_cpu_bound"),
    path("async-io-bound", async_io_bound, name="async_io_bound"),
]
