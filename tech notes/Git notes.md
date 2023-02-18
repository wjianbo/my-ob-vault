tags:: #tech/git

# Git notes
## Using ssh
When using HTTPS, username and password is needed for every push. Better to use ssh to save the trouble. Follow these steps.

1. Generate ssh key pair.
```shell
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```
2. Add the public key to GitHub settings.
3. If already using HTTPS, change the `url` property in `.git/config` file.