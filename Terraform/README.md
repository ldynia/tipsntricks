# Installation

## Terraform

https://learn.hashicorp.com/tutorials/terraform/install-cli

```bash
$ sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
$ curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
$ sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
$ sudo apt-get update && sudo apt-get install terraform
```

## Terraform Env

https://github.com/tfutils/tfenv

```bash
$ git clone https://github.com/tfutils/tfenv.git ~/.tfenv
$ echo 'export PATH="$HOME/.tfenv/bin:$PATH"' >> ~/.bash_profile
$ source ~/.bash_profile
```
## Terraform Switch

```bash
curl -L https://raw.githubusercontent.com/warrensbox/terraform-switcher/release/install.sh | sudo bash
export PATH=$PATH:/home/$USER/bin
tfswitch
terraform version
```
