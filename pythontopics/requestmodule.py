import requests

# Fetching the data from URL using requests module
#requests get, post, put, delete, head, options, patch
 # status code : 200 success , 400 bad request, 404 not found, 500 server error
response = requests.get('https://api.github.com/events')
print(response)
print(response.status_code) 
print(response.text)

