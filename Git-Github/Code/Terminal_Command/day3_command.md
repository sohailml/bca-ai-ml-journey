# merge conflict


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git branch
* master


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git switch -c ui
Switched to a new branch 'ui'

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (ui)
$ git branch
  master
* ui

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (ui)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (ui)
$ git commit -m "commit A"
[ui 53c99ca] commit A
 1 file changed, 2 insertions(+)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (ui)
$ git log --oneline
53c99ca (HEAD -> ui) commit A
55ee521 (master) Merge branch 'ui'
c0166d1 added e
6b02c5e commit D
012b5af commict c
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (ui)
$ git switch master
Switched to branch 'master'

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git commit -m "commit B"
[master b60eba3] commit B
 1 file changed, 1 insertion(+)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git log --oneline
b60eba3 (HEAD -> master) commit B
55ee521 Merge branch 'ui'
c0166d1 added e
6b02c5e commit D
012b5af commict c
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git merge ui
Auto-merging dummyB.txt
CONFLICT (content): Merge conflict in dummyB.txt
Automatic merge failed; fix conflicts and then commit the result.

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master|MERGING)
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   dummyB.txt

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master|MERGING)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master|MERGING)
$ git commit -m "merging"
[master 1df7891] merging

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git log --oneline
1df7891 (HEAD -> master) merging
b60eba3 commit B
53c99ca (ui) commit A
55ee521 Merge branch 'ui'
c0166d1 added e
6b02c5e commit D
012b5af commict c
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$

# stashing

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git branch -d ui
Deleted branch ui (was 53c99ca).

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git branch
* master

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   dummyA.txt
        modified:   dummyB.txt
        modified:   style.css

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   dummyA.txt
        modified:   dummyB.txt
        modified:   style.css

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git stash
Saved working directory and index state WIP on master: 1df7891 merging

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git stash list
stash@{0}: WIP on master: 1df7891 merging

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    photo.jpg

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        logo.jpg

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git commit -m "rename photo to logo"
[master 204cf28] rename photo to logo
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename photo.jpg => logo.jpg (100%)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git log --onelien
fatal: unrecognized argument: --onelien

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git log --oneline
204cf28 (HEAD -> master) rename photo to logo
1df7891 merging
b60eba3 commit B
53c99ca commit A
55ee521 Merge branch 'ui'
c0166d1 added e
6b02c5e commit D
012b5af commict c
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git stash pop
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   dummyA.txt
        modified:   dummyB.txt
        modified:   style.css

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (ac87742dd8d382b593febb5d7e057e5541577f00)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   dummyA.txt
        modified:   dummyB.txt
        modified:   style.css

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git stash list

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git commit -m "commit"
[master 984e33d] commit
 4 files changed, 5 insertions(+), 1 deletion(-)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$


# git tags


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   style.css

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git commit -m "release 1"
[master 38fa979] release 1
 1 file changed, 1 insertion(+), 1 deletion(-)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git tag

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git tag -a v1.0 -m "my release 1"

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git tag
v1.0

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git log --oneline
38fa979 (HEAD -> master, tag: v1.0) release 1
984e33d commit
204cf28 rename photo to logo
1df7891 merging
b60eba3 commit B
53c99ca commit A
55ee521 Merge branch 'ui'
c0166d1 added e
6b02c5e commit D
012b5af commict c
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   dummyB.txt

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git commit -m "release 2"
[master 5cfb919] release 2
 1 file changed, 1 insertion(+), 1 deletion(-)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git tag
v1.0

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git log --oneline
5cfb919 (HEAD -> master) release 2
38fa979 (tag: v1.0) release 1
984e33d commit
204cf28 rename photo to logo
1df7891 merging
b60eba3 commit B
53c99ca commit A
55ee521 Merge branch 'ui'
c0166d1 added e
6b02c5e commit D
012b5af commict c
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git tag v2

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git tag
v1.0
v2

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$ git log --oneline
5cfb919 (HEAD -> master, tag: v2) release 2
38fa979 (tag: v1.0) release 1
984e33d commit
204cf28 rename photo to logo
1df7891 merging
b60eba3 commit B
53c99ca commit A
55ee521 Merge branch 'ui'
c0166d1 added e
6b02c5e commit D
012b5af commict c
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/Code/ecom-electronics (master)
$
