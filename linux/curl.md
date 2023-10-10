# Curl

### Measure response time
```
curl -o /dev/null -s -w %{time_total}\\n  http://compare.cbs.dtu.dk:444/

curl -Ik -X GET --header "Authorization:JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJlbmNobWFya2luZyIsInVzZXJfaWQiOjE3LCJlbWFpbCI6ImJlbmNobWFya2luZzAzZW5nYWdlQGdtYWlsLmNvbSIsImV4cCI6MTQ3Njk2NjI1OH0.zAnv2KpP4No1GLDeaKICLwp19PYKU7gLvdm5dNBRVUY" https://compare.cbs.dtu.dk:444/app/api/v1/user/samples

curl -k -X GET --header "Authorization:JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJlbmNobWFya2luZyIsInVzZXJfaWQiOjE3LCJlbWFpbCI6ImJlbmNobWFya2luZzAzZW5nYWdlQGdtYWlsLmNvbSIsImV4cCI6MTQ3Njk2NjI1OH0.zAnv2KpP4No1GLDeaKICLwp19PYKU7gLvdm5dNBRVUY" -o /dev/null -s -w %{time_total}\\n https://compare.cbs.dtu.dk:444/app/api/v1/user/samples
```


### Post data as a json
```
curl -v -H "Content-Type: application/json" -X POST -d '{"username":"ldynia","password":"123123"}' http://compare.cbs/api/v1/user/login
```
