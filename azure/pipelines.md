# Azure Pipelines

## Build

## Submodules with system token

```bash
pool :
    vmImage : "ubuntu-latest"
  
  stages :
    - stage : Build
      jobs :
        - job : build_docker
          steps :
            - script: |
                git -c http.extraheader="AUTHORIZATION: bearer $(System.AccessToken)" \
                    submodule update --init --recursive
              displayName: Fetch Submodules
```

### Checkout submodules without PAT

```yaml
pool :
  vmImage : "ubuntu-latest"

resources:
  repositories:
  - repository: repo-name
    name: Some Project Within Organization/repo-name
    type: git
 
  - repository: RepoOne
    name: Some Project Within Organization/Repo One
    type: git
  
  - repository: RepoTwo
    name: Some Project Within Organization/Repo Two
    type: git

stages :
  - stage : Build
    jobs :
      - job : Build
        steps :
          - checkout: self
            submodules: false
            path: "s/"
            
          - checkout: repo-name
            path: "s/libs/repo-name/"
            
          - checkout: RepoOne
            path: "s/libs/DataLakeTransform/"
            
          - checkout: RepoTwo
            path: "s/libs/DataLakeEnvironment/"

          - script: |
              ls -l 
            displayName: Prepare File System

```


### Checkout submodules with PAT

```yaml
pool :
    vmImage : "ubuntu-latest"
  
variables :
  - group: project-dev-secrets

stages :
    - stage : Build
      jobs :
        - job : Build
          steps :
            - checkout: self
              submodules: false
  
            - script: |
                echo "Checkout using submodules"
                git -c http.https://energy@dev.azure.com/genergy/Data%20Lake/_git/repo-name.extraheader="AUTHORIZATION: basic $(PAT_TOKEN)" \
                    -c http.https://energy@dev.azure.com/genergy/Data%20Lake/_git/Data%20Transform.extraheader="AUTHORIZATION: basic $(PAT_TOKEN)" \
                    -c http.https://energy@dev.azure.com/genergy/Data%20Lake/_git/Data%20Environment.extraheader="AUTHORIZATION: basic $(PAT_TOKEN)" \
                    submodule update --init --recursive
              displayName: Fetch Submodules With PAT Token
```
