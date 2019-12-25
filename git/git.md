# git笔记

## 查看历史提交记录

- git reflog

  ![image-20191224225834314](/Users/fanding/gitProjects/notes/git/img/image-20191224225834314.png)

- git log --oneline

  ![image-20191224225926694](/Users/fanding/gitProjects/notes/git/img/image-20191224225926694.png)

- git log --pretty=oneline

  ![image-20191224230028463](/Users/fanding/gitProjects/notes/git/img/image-20191224230028463.png)

- git log

  ![image-20191224230135618](/Users/fanding/gitProjects/notes/git/img/image-20191224230135618.png)

## 回滚命令

- git reset —hard +  版本号

  ![image-20191224231040534](/Users/fanding/gitProjects/notes/git/img/image-20191224231040534.png)

- —hard、—soft、—mix的区别

  ```
  --hard：工作区、缓存区、本地库同时回滚
  --soft：仅本地库回滚
  --mix： 仅本地库和缓冲区回滚，工作区保持不变
  ```

## 比较差异

- git diff 版本号 文件名 

  ```
  和某个版本号下的文件对比差异
  ```

## 解决冲突

- git pull
- 打开有冲突的文件，进行解决冲突
- git add 文件名
- git commit -m "merage"
- 