# Links

- https://docs.microsoft.com/en-us/powershell/module/dnsserver/add-dnsserverresourcerecord?view=windowsserver2022-ps#examples

## A Record

### Get

```powershell
powershell> Get-DnsServerResourceRecord -ComputerName activepdc.live.com -ZoneName "live.com" -Name "test-opticab-engineering-tools"
```
### Create

```powershell
Add-DnsServerResourceRecord -A -ZoneName "live.com" -Name "Host201.admin" -IPv4Address "10.155.1.10"
Add-DnsServerResourceRecordA -Name "dev-app" -IPv4Address "10.80.200.9" -ZoneName "live.com" -ComputerName activepdc.live.com -TimeToLive “00:01:00”
```

### Delete

```powershell
Remove-DnsServerResourceRecord -ZoneName "live.com" -RRType "A" -Name "dev.app" -RecordData "10.80.3.110"
```

## CName

### Create

```powershell
Add-DnsServerResourceRecordCName -Name "staging.app1" -HostNameAlias "cluster-blue-aks-dev.live.com." -ZoneName "example.com" -ComputerName activepdc.live.com -TimeToLive "00:02:00"
Add-DnsServerResourceRecordCName -Name "staging.app2" -HostNameAlias "cluster-blue-aks-dev.live.com." -ZoneName "live.com" -ComputerName activepdc.live.com -TimeToLive "00:02:00"
```
