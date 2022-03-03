# GIT-BASH LA GI?
- https://www.bkns.vn/git-bash-la-gi.html


# LAM VIEC VOI GIT
## Cac lenh co ban

- https://viblo.asia/p/lam-viec-co-ban-voi-git-RQqKL2zrl7z
- https://www.codehub.vn/Cai-Dat-va-Cau-Hinh-Git 

## Xoa nhanh trong GIT
- https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/

## GIT undo-merge
- https://www.datree.io/resources/git-undo-merge

## Lam viec voi nhanh trong GIT
- https://xuanthulab.net/lam-viec-voi-nhanh-branch-tao-nhanh-gop-nhanh-trong-git.html

## GIT-COMMANDS

### **git-revert**

`git revert -m 1 hash_of_merge_commit`
`git reset --hard <commit id>`

### **git-branch**

1. `git branch --merged master` : **This prints the branches merged into master**
2. `git branch --merged lists`  : **This prints the branches merged into HEAD (i.e. tip of current branch)**
3. `git branch --no-merged`     : **This prints the branches that have not been merged**

_**By default this applies only to local branches.**_

_We can use `-a` flag to show both local and remote branches._
_Or we can use `-r` flag to show only the remote branches._


### **remove o/branches fr. VSc**

`git fetch --prune`