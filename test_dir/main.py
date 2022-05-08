import requests
import seturl

params = seturl.set_url();
url = "http://3.35.141.241:5000/" + params;
r = requests.get(url)
result = r.json()
print(params +"  "+result)
