import urllib.request
import urllib.parse

def make_http_request(url, method="POST", data=None, headers={}):
    if headers is None:
        headers = {}
    if data and method == "POST":
        data = urllib.parse.urlencode(data).encode('utf-8')
    
        headers['content-type'] = 'application/x-www-form-urlencoded'
    else:
        encoded_data = None
    req = urllib.request.Request(
        url,
        data=data if method == "POST" else None,
        headers=headers,
        method=method
    )

    try:
        with urllib.request.urlopen(req) as response:
           return {
               "status_code": response.getcode(),
                "data": response.read().decode('utf-8')
           }
        
    except urllib.error.HTTPError as e:
        return {
            "status_code": e.code,
            "data": str(e)
        }
# Example usage:
result = make_http_request("https://api.github.com/users/github")
print(result)