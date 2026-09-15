
Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   index.html
        new file:   style.css


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   index.html
        new file:   style.css


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "added base file"
[master (root-commit) 42b8f29] added base file
 2 files changed, 14 insertions(+)
 create mode 100644 index.html
 create mode 100644 style.css

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   index.html


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "Added nav bar and a container"
[master 6f2c276] Added nav bar and a container
 1 file changed, 6 insertions(+), 1 deletion(-)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log --oneline
6f2c276 (HEAD -> master) Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        assets/

nothing added to commit but untracked files present (use "git add" to track)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   assets/login.svg
        new file:   assets/photo.jpg


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "added asstes"
[master 05c5d07] added asstes
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 assets/login.svg
 create mode 100644 assets/photo.jpg

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log -- oneline

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log --oneline
05c5d07 (HEAD -> master) added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "Added .gitignore"
[master a902597] Added .gitignore
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log --oneline
a902597 (HEAD -> master) Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "added builds in gitignore"
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .gitignore


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "added buids in gitignore"
[master 1946154] added buids in gitignore
 1 file changed, 1 insertion(+)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log --oneline
1946154 (HEAD -> master) added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        img/
        info/

nothing added to commit but untracked files present (use "git add" to track)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   img/.gitkeep
        new file:   info/.gitkeep


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "added img and info directories"
[master 04543c6] added img and info directories
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 img/.gitkeep
 create mode 100644 info/.gitkeep

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
nothing to commit, working tree clean

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log --oneline
04543c6 (HEAD -> master) added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add dummy1
fatal: pathspec 'dummy1' did not match any files

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add dummy1.txt

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "added A"
[master 1e80235] added A
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 dummy1.txt

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "added B"
[master 25b7f8b] added B
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 dummy2.txt

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log --oneline
25b7f8b (HEAD -> master) added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git branch ui

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git branch
* master
  ui

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git switch ui
Switched to branch 'ui'

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (ui)
$ git branch
  master
* ui

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (ui)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (ui)
$ git commit -m "commict c"
[ui 012b5af] commict c
 3 files changed, 16 deletions(-)
 delete mode 100644 index.html
 rename assets/login.svg => login.svg (100%)
 rename assets/photo.jpg => photo.jpg (100%)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (ui)
$ git log --oneline
012b5af (HEAD -> ui) commict c
25b7f8b (master) added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (ui)
$ git switch master
Switched to branch 'master'

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git add .

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    dummy1.txt -> dummyA.txt
        renamed:    dummy2.txt -> dummyB.txt


Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git commit -m "commit D"
[master 6b02c5e] commit D
 2 files changed, 0 insertions(+), 0 deletions(-)
 rename dummy1.txt => dummyA.txt (100%)
 rename dummy2.txt => dummyB.txt (100%)

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git log --oneline
6b02c5e (HEAD -> master) commit D
25b7f8b added B
1e80235 added A
04543c6 added img and info directories
1946154 added buids in gitignore
a902597 Added .gitignore
05c5d07 added asstes
6f2c276 Added nav bar and a container
42b8f29 added base file

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (master)
$ git switch ui
Switched to branch 'ui'

Dell@Arbaaz MINGW64 /c/startup-project/bca-aiml/git-github/ecom-electronics (ui)
$
