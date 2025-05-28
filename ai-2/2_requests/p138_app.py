import requests

where_value = 'nexearch'
sm_value = 'top_hty'
fbm_value = 1
ie_value = 'UTF-8'
query_value = 'python'

baseurl = 'https://search.naver.com/search.naver'
parameters = {
    "where": where_value,
    "sm": sm_value,
    "fbm": fbm_value,
    "ie": ie_value,
    "query": query_value
}

res = requests.get(baseurl, params=parameters)
print(res.url)