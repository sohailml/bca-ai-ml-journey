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

