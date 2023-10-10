#!/usr/bin/env python3

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
# apt install python3-gi
# apt install libgirepository1.0-dev
# pip install pygobject

# $ apt-get install ca-certificates curl apt-transport-https lsb-release gnupg
# $ curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null
# $ echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | tee /etc/apt/sources.list.d/azure-cli.list
# $ apt update
# $ apt install azure-cli
# az login

KVUri = f"https://project-dev-kv.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

retrieved_secret = client.get_secret("rg-name")

print(f"Your secret is '{retrieved_secret.value}'.")
