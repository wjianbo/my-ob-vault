## Generate an SSH key pair

If you do not have an existing SSH key pair, generate a new one.

1.  Open a terminal.
    
2.  Type `ssh-keygen -t` followed by the key type and an optional comment. This comment is included in the `.pub` file that's created. You may want to use an email address for the comment.
    
    For example, for ED25519:
    
    ```
    ssh-keygen -t ed25519 -C "<comment>"
    ```