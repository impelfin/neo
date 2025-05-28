import requests

where_value = 'nexearch'
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'UTF-8'
query_value = 'python'

baseurl = 'https://search.naver.com/search.naver'
parameters = "?where={0}&sm_value={1}&fbm_value={2}&ie_value={3}&query_value={4}".format(where_value, sm_value, fbm_value, ie_value, query_value)

url_parameters = baseurl + parameters
res = requests.get(url_parameters)
print(res.url)