# Server Side

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

Python Commands:


