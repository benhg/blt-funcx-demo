# Server Side

### Log In / Configure
```
funcx-endpoint configure
### FOLLOW PROMPT ###
```

### Create Endpoint:
```
funcx-endpoint configure <ENDPOINT NAME>
nano ~/.funcx/<ENDPOINT NAME>/endpoint_config.py
#### PUT IN THE CONFIG FROM THE OTHER FILE ###
```

### Show endpoints:

```
[glick@mayo ~]$ funcx-endpoint list
+---------------+--------+--------------------------------------+
| Endpoint Name | Status |             Endpoint ID              |
+===============+========+======================================+
| default       | Active | None                                 |
+---------------+--------+--------------------------------------+
| blt_endpoinnt | Active | 91ac17bf-1b31-49d0-abd4-95af6a9bdc94 |
+---------------+--------+--------------------------------------+
```

Start Endpoint:
```
[glick@mayo ~]$ funcx-endpoint start blt_endpoinnt
2020-09-08 20:23:12 funcx.sdk.client.FuncXClient:89 [INFO]  [instance:140342883910096] Creating client of type <class 'funcx.sdk.client.FuncXClient'> for service "funcX"
2020-09-08 20:23:13 funcx:256 [INFO]  Starting endpoint with uuid: 91ac17bf-1b31-49d0-abd4-95af6a9bdc94
```

# Client Side

### (Optional) Create and Start Venv:
```
pip3 install virtualenv
virtualenv funcx
source funcx/bin/activate
```

### Install Funcx:
```
pip[3] install funcx
```

### Python Commands:
```
(funcx) ben@benbox:20:36:48[/Users/ben]$ python3                                          
Python 3.7.6 (default, Dec 30 2019, 19:38:28) 
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from funcx.sdk.client import FuncXClient
>>> fxc = FuncXClient()
Please paste the following URL in a browser:
https://auth.globus.org/v2/oauth2/authorize?client_id=4cf29807-cf21-49ec-9443-ff9a3fb9f81c&redirect_uri=https%3A%2F%2Fauth.globus.org%2Fv2%2Fweb%2Fauth-code&scope=https%3A%2F%2Fauth.globus.org%2Fscopes%2Ffacd7ccc-c5f4-42aa-916b-a0e270e2c2a9%2Fall+urn%3Aglobus%3Aauth%3Ascope%3Asearch.api.globus.org%3Aall+openid&state=_default&response_type=code&code_challenge=lxc99L__ZorA-O-AH2WCqAWzkHG2x--Dbothg9SJvis&code_challenge_method=S256&access_type=offline&prefill_named_grant=FuncX+SDK+Login
Please Paste your Auth Code Below: 
tUH70lbYDue7LJd07MqcohmaazUnyS
>>> def hello_world():
...     return "Hello World!"
... 
>>> func_uuid = fxc.register_function(hello_world)
print(func_uuid)

>>> print(func_uuid)
22d61ba7-2531-42d7-9dcd-d3fe50310b3a
>>> 
>>> blt_ep = "8e1bc858-feda-42b3-8b7a-5a058c0ef6ec" # Configured this earlier
>>> res = fxc.run(endpoint_id=blt_ep, function_id=func_uuid)
```



