# Manage Subscriptions

## Roles

```bash
az role assignment create --assignee ADMXXX@email.com --role "Network Contributor" --scope "/subscriptions/1b4fc5bf-1549-49ae-94e3-d90667c245d2/resourceGroups/RG-infrastructure/providers/Microsoft.Network/virtualNetworks/e-art-aks-prod-green-we"
az role assignment create --assignee ADMXXX@email.com --role "Network Contributor" --scope "/subscriptions/1b4fc5bf-1549-49ae-94e3-d90667c245d2/resourceGroups/RG-infrastructure/providers/Microsoft.Network/virtualNetworks/e-art-aks-prod-blue-we"
az role assignment create --assignee ADMXXX@email.com --role "Network Contributor"

az role assignment delete --assignee ADMXXX@email.com --role "Network Contributor" --scope "/subscriptions/1b4fc5bf-1549-49ae-94e3-d90667c245d2/resourceGroups/RG-infrastructure/providers/Microsoft.Network/virtualNetworks/e-art-aks-prod-green-we"
az role assignment delete --assignee ADMXXX@email.com --role "Network Contributor" --scope "/subscriptions/1b4fc5bf-1549-49ae-94e3-d90667c245d2/resourceGroups/RG-infrastructure/providers/Microsoft.Network/virtualNetworks/e-art-aks-prod-blue-we"
az role assignment delete --assignee ADMXXX@email.com --role "Network Contributor"
```

## Accounts

```bash
$ az login
$ az account list
$ az account show
$ az account set --subscription <name|ID>
```

## Key Vault

```bash
$ az account set --subscription <name|id>
$ az keyvault show --name <kv-name> --query "properties.accessPolicies[*].objectId"
$ az keyvault set-policy --name <kv-name> --object-id <GUID> --key-permissions all --secret-permissions all --certificate-permissions all --storage-permissions all
$ az keyvault show --name <kv-name> --query "properties.accessPolicies[*].objectId"

$ az keyvault set-policy --name <kv-name> --subscription <name|id> --resource-group <name|id> --object-id <GUID> --certificate-permissions all
$ az keyvault set-policy --name <kv-name> --subscription <name|id> --resource-group <name|id> --object-id <GUID> --certificate-permissions all --secret-permissions all --key-permissions backup create delete get import list recover release restore update
```

## Query

```bash
# the query i used to find all Web Apps in a subscription and its kind
$ az webapp list --query "[].{hostName: defaultHostName, kind: kind}" --subscription E-ART
```
