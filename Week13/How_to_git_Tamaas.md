We plan to contribute our solver to open-source [Tamaas project](https://tamaas.readthedocs.io/en/latest/) by creating [merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html#new-merge-request-from-a-fork).

We can start to learn how to play with git, especially how to merge branches, we have installed GitLab Workflow extension for [VS Code](https://docs.gitlab.com/ee/editor_extensions/visual_studio_code/). 

We also installed blender, we will try to learn this rendering skill as well.

To initiate our work on GitLab, we follow the steps in [3]. We have been added in Tamaas project as developer, so we plan to play with our branch. Here we first clone from **master** branch of Tamaas[1].

#### Useful commands

Some useful commands are listed:

```bash
git remote set-url origin git@gitlab.com:tamaas/tamaas.git
git fetch --all
git remote --verbose
git checkout -b maxwell_viscoelastic-branch 
git branch -a
```

##### Recommended Workflow

Ensure your local `master` branch is up to date, and create new feature branches from the latest `master` branch:

1. Fetch All Remote Updates
```bash
git fetch --all
```
*If you want to temporarily save your local changes before merging:*
```bash
git stash
```
2. Merge Updates into Local `master`
```bash
git checkout master
git merge origin/master
```
3. Switch to Your Feature Branch
```bash
git checkout mybranch
git merge master  # For existing branches
```
4. Alternatively, Create a New Feature Branch
```bash
git checkout -b newbranch
git merge master  # For existing branches
```

*If you stashed your changes earlier, apply them back to your feature branch:*
```bash
git stash pop
```
*Resolve conflicts:*

- Resolve manually
- Mark as resolved:

```bash
git add <resolved-files>
git commit -m "Resolved merge conflicts"
```

##### Summary

Make sure your local master branch is synchronized with the remote master branch, then create or update your feature branches based on the latest master to ensure your development branch includes the most recent changes.



#### Configure GitLab

Before everything started, we should deal with SSH:

```bash
(base)  lizichen@lizichendeMacBook-Air  ~/Tamaas/tamaas   maxwell_viscoelastic-branch  cat ~/.ssh/id_rsa.pub 
```
And add this public key to our GitLab webpage.(Just like what we have done for Github)

Then we will be informed to set a passphrase for this key by typing:

```bash
(base)  lizichen@lizichendeMacBook-Air  ~/Tamaas/tamaas   maxwell_viscoelastic-branch  git fetch 
```

With the help of ssh-agent(integrated on macOS since Leopard, version 10.5 in 2007)[4], we don't need to type our passphrase every time when we push local to remote.

Start the SSH agent and add our private key to the SSH agent:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

List all keys loaded into ssh-agent:
```bash
ssh-add -l
```
If everything is set up correctly, we will see a welcome message stating that our SSH connection is now set up by typing:
```bash
ssh -T git@gitlab.com
```

**origin** is the default name of the remote repository. Establish a tracking relationship between the local branch and the remote branch, so that subsequent git push and git pull commands on this branch do not need to specify the remote repository name and branch name. The following command is usually used when we push a new branch to the remote repository for the first time to set up this tracking relationship:

```bash
git remote set-url origin git@gitlab.com:tamaas/tamaas.git
```

#### Deal with branches

When we talk about git, we should be clear with local and remote repo, for GitLab, we can easily create a New branch by clicking **New branch** on GitLab webpage, or use command:

```bash
(base)  lizichen@lizichendeMacBook-Air  ~/Tamaas/tamaas   master  git checkout -b maxwell_viscoelastic-branch               
Switched to a new branch 'maxwell_viscoelastic-branch'
```
If we already link our local repo and remote repo with SSH, then a new branch will be automatic generated when we push our local repo to remote:

```bash
git push -u origin maxwell_viscoelastic-branch
```

When we need to develop on our branch, we can just switch to this branch using the following command:

```bash
git checkout maxwell_viscoelastic-branch
```
#### Deal with potential conflict

Additionally, using `git stash` is a handy way to temporarily shelve (or stash) changes you've made to your working directory so you can work on something else, and then come back and re-apply them later on. Here's a step-by-step guide on how you can use this feature in conjunction with merging:

1. **Stash Your Changes**:
   - Before merging, make sure you're on the branch where you've made your changes. If you have any uncommitted changes that you don't want to commit yet, you can stash them.
   - Run `git stash` to stash your changes. This command saves your modifications and reverts the working directory to match the HEAD commit.
   - Optionally, you can use `git stash push -m "Your message"` to add a description to your stash for easier identification later.

2. **Merge the Changes**:
   - Switch to the branch where you want to merge the changes. For instance, if you're merging into your current branch from `master`, you'd stay on your current branch.
   - Run `git merge master` to merge changes from the master branch into your current branch. Resolve any conflicts if they arise.

3. **Reapply Your Stashed Changes**:
   - Once the merge is complete and you're ready to get back to your work, run `git stash pop`. This command applies the stashed changes back to your working directory and removes them from the stash list.
   - If you want to keep the stash in your stash list, you can use `git stash apply` instead. This re-applies the changes but does not remove them from the stash.

4. **Handle Merge Conflicts**:
   - If your stashed changes conflict with the changes from the merge, you'll need to resolve these conflicts manually. Git will prompt you to fix the conflicts before completing the `git stash pop`.
   - After resolving any conflicts, if you used `git stash pop`, make sure to commit these resolved changes to finalize the merge process.

Using `git stash` is particularly useful when you need to quickly switch contexts. For example, if you do not want to discard changes before merging, and don't want to create a commit either, you can `git stash` before the merge, `git merge master` then `git stash pop` to re-apply your old changes. It allows for a clean workflow without losing any of your work.



#### Reference:

[1] https://tamaas.readthedocs.io/en/latest/

[2] https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html#new-merge-request-from-a-fork

[3] https://yang-xijie.github.io/LECTURE/Git/git/#_10

[4] https://en.wikipedia.org/wiki/Ssh-agent