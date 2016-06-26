# Api Docs

## Signup and getting api_token 

##### Check for available usernames
```
GET /check_existing/<username>
```
###### Example
```python
import requests
response = requests.get('http://wingify-challenge.herokuapp.com/check_existing/ishankhare07')
response.json()
{'message': 'ishankhare07 unique', 'status': 'success'}
```

##### Signing up with this unique username
```
POST /signup
```
##### JSON
| Name | Type | Description |
|------|-------|------------|
| firstname | string | firstname of the user |
| lastname | string | lastname of the user |
| username | string | desired username|
| password | string | desired password|

##### Response
```json
{
  "api_token": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwaXJlcyI6MTQ2Njk4MTIxMi4yODA0MjMsInVzZXJuYW1lIjoiaXNoYW5raGFyZTA3In0.cRlM0w2u6DSj6wUVLJi6Hyv2-x6ezRPVdpbFgWnX1os", 
  "status": "signup succesful"
}
```

###### Example
```python
import requests
response = requests.post('http://wingify-challenge.herokuapp.com/signup', json=dict(firstname='ishan',
                lastname='khare', username='ishankhare07', password='*****'))
response.json()
{
  'api_token': 'eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwaXJlcyI6MTQ2Njk4MTIxMi4yODA0MjMsInVzZXJuYW1lIjoiaXNoYW5raGFyZTA3In0.cRlM0w2u6DSj6wUVLJi6Hyv2-x6ezRPVdpbFgWnX1os',
  'status': 'signup succesful'
}
```
