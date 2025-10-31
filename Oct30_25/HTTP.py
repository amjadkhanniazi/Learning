import urllib.request
import json

def simple_get_request(url):
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        res_code = response.getcode()
        data = json.loads(content)
        return {
            "Status": res_code,
            "Data": data,
        }
    except urllib.error.HTTPError as e:
        return {
            "Status": e.code,
            "Message": e.reason,
        }


result = simple_get_request("https://api.github.com/users/github")
print(result)
# print(result["login"])  # Should print 'github' if successful
# print(result["followers"])  # Number of followers
# print(result["public_repos"])  # Number of public repositories