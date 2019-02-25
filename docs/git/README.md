Working with Genume repository
==================================

#### Get the code for the first time

```sh
git clone https://github.com/CSD-FOSS-Team/genume.git
```

Branches
---------

* Don't commit your changes directly to master.
  It will make the collaborative workflow messy.
* Checkout a new local branch from `master` for every change you want to make (bugfix, feature).
* Use lowercase-with-dashes for naming.
* Follow [Linus' recommendations][Linus] about history.
    - "People can (and probably should) rebase their _private_ trees (their own work). That's a _cleanup_. But never other peoples code. That's a 'destroy history'...
    You must never EVER destroy other peoples history. You must not rebase commits other people did.
    Basically, if it doesn't have your sign-off on it, it's off limits: you can't rebase it, because it's not yours."

* **master** is the branch with the latest and greatest changes.
  It could be unstable.

#### Sync your local repo

Use **git rebase** instead of **git merge** and **git pull**, when you're updating your feature-branch.

```sh
# fetch updates all remote branch references in the repo
# --all : tells it to do it for all remotes (handy, when you use your fork)
# -p : tells it to remove obsolete remote branch references (when they are removed from remote)
git fetch --all -p

# rebase on origin/master will rewrite your branch history
git rebase origin/master
```

#### More complex scenarios

Covering all possible git scenarios is behind the scope of the current document.
Git has excellent documentation and lots of materials available online.

We are leaving few links here:

[Git pretty flowchart](http://justinhileman.info/article/git-pretty/): what to do, when your local repo became a mess.

[Linus]:https://wincent.com/wiki/git_rebase%3A_you're_doing_it_wrong




Recommended Git configurations
==============================

We highly recommend these configurations to help deal with whitespace,
rebasing, and general use of Git.

> Auto-corrects your command when it's sure (`stats` to `status`)
```sh
git config --global help.autoCorrect -1
```

> Refuses to merge when pulling, and only pushes to branch with same name.
```sh
git config --global pull.ff only
git config --global push.default current
```

> Shows shorter commit hashes and always shows reference names in the log.
```sh
git config --global log.abbrevCommit true
git config --global log.decorate short
```

> Ignores whitespace changes and uses more information when merging.
```sh
git config --global apply.ignoreWhitespace change
git config --global rerere.enabled true
git config --global rerere.autoUpdate true
git config --global am.threeWay true
```
