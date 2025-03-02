---
id: misc
aliases: []
tags: []
---

# Set a separate ssh key for one or more repo

While adding your machine to github via ssh, we followed [github's guide line](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

However, we can also set up one or more ssh keys for one or more repos. 

This can be handy in different scenarios. For example, say for the default setup I have
generated ssh key with a passkey. So, for every push/pull action I have to authenticate
using that passkey. Now I have a specific repository where I don't want this behavior, rather
don't use any passkey at all. To achieve this we can do this:


Run:

```sh
ssh-keygen -t ed25519 -f ~/.ssh/id_newID -N ""
```

- This creates a new key (`id_newID`) with no passphrase.
- The private key is stored in `~/.ssh/id_newID`.
- The public key is stored in `~/.ssh/id_newID.pub`. 

Now, to `push` / `pull` do:

```bash
GIT_SSH_COMMAND="ssh -i ~/.ssh/id_newID" git pull
```

To parsist this behavior, in the repo, do:
```bash
git config core.sshCommand "ssh -i ~/.ssh/id_newID"
```





