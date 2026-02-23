import requests

# Fetching the data from URL using requests module
#requests get, post, put, delete, head, options, patch
 # status code : 200 success , 400 bad request, 404 not found, 500 server error
# response = requests.get('https://api.github.com/events')
# print(response)
# print(response.status_code) 
# print(response.text)


# data = {"name": "John", "age": 30}
# response = requests.post('https://httpbin.org/post', json=data)
# print(response.status_code)
# print(response.json())

# update = {"name": "John", "age": 31}
# response = requests.put('https://httpbin.org/put', json=update)
# print(response.status_code)
# print(response.json())

# get_response = requests.get('https://httpbin.org/get')
# print(get_response.status_code)
# print(get_response.json())

# response = requests.delete('https://httpbin.org/delete')
# print(response.status_code)
# print(response.json())

import requests
import json
list1 = [{
    
    "name": "Jagadisha Mukhopadhyay",
    "email": "jagadisha_mukhopadhyay@botsford.test",
    "gender": "female",
    "status": "active"
  },
  {
    
    "name": "Kailash Butt MD",
    "email": "butt_kailash_md@cummerata.example",
    "gender": "male",
    "status": "active"
  }]

for i in list1:
    url = "https://gorest.co.in/public/v2/users/"

    headers = {

    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(i))
    print(response.status_code)  
    print(response.text)


#  Endpoint - Gateway to communication to platform/application/service , restrict the data , secure , 1000 request limit 
# /api/user  -- name, salary, employee id ( get, post, put) 
# /api/appdata -   performance, transaction ( get, post, put)
# /api/log  - accesslog, translog (get)
# /api/{admin}/*   - (get, post,put,delete )

# API GATEWAY - security -- >  ( API endpoint ) 

# APIGEE -- google 

