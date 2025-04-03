import subprocess
import time
import sys


if len(sys.argv) > 1:
    BASE_URL = sys.argv[1]
else:
    BASE_URL = "http://127.0.0.1:8000"
ENDPOINTS = [
    "/sync-ping", "/sync-cpu-bound", "/sync-io-bound",
    "/async-ping", "/async-cpu-bound", "/async-io-bound",
]
WRK_COMMAND_TEMPLATE = "wrk -t1 -c200 -d10s {url}"


def run_wrk(endpoint):
    url = f"{BASE_URL}{endpoint}"
    command = WRK_COMMAND_TEMPLATE.format(url=url)
    print(f"Running wrk for endpoint: {endpoint}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Response for {endpoint}:")
    print(result.stdout)
    print("-" * 50, flush=True)


if __name__ == "__main__":
    for endpoint in ENDPOINTS:
        run_wrk(endpoint)
        print("Sleeping for 5 seconds...", flush=True)
        time.sleep(5)
