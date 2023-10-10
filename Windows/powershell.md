# PowerShell

```powershell
powershell> net user admxldyn /domain
powershell> dsquery user -samid xldyn | dsget user -memberof | dsget group -samid | sort
powershell> Get-ADPrincipalGroupMembership xldyn | select name | Sort-Object -Property name
```

# Get Azure Serices Namespace

```powershell
powershell> Get-AzResource | select ResourceGroupName,ResourceType,Name | sort ResourceType | Format-Table
```

