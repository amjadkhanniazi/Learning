import urllib.request

def get_request_with_status(url):
    try:
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        data = response.read().decode('utf-8')
        return {
            "status_code": status_code,
            "data": data
        }
    except urllib.error.HTTPError as e:
        return {
            "status_code": e.code,
            "data": str(e)
        }

# result = get_request_with_status("http://httpbin.org/status/404")
result = get_request_with_status("https://api.github.com/users/github")
print(result)