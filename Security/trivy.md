# Trivy

```bash
# Install Trivy
$ wget https://github.com/aquasecurity/trivy/releases/download/v0.16.0/trivy_0.16.0_Linux-64bit.deb
$ sudo dpkg -i trivy_0.16.0_Linux-64bit.deb

$ trivy fs frontend/ > trivy_frontend_fs.txt
$ trivy <DOCKER_IMAGE> > trivy_image.txt
```
