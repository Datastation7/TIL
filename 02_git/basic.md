# git 기초

## git의 학습 이유와 개념
### 1. git의 학습 이유
* 각 버전의 파일이 어느 것이 가장 최근의 파일인지 알아보기 어렵고, 효율적이지 못해서 git이 필요하다.

### 2. git의 개념
* 주로 여러명의 개발자가 하나의 소프트웨어 개발 프로젝트에 참여할 때, `소스 코드를 효과적으로 관리`할 수 있는 `Free Software` 중 하나이다.
* `개발 프로젝트에서 버전 관리를 돕는 시스템`이다.


## git의 장점

* 여러 서버 저장소와 여러 로컬 저장소에 분산해서 저장할 수 있다.

### VCS

### Working Directory

### Stage

### Commit

## git 사용법



|명령어|설명|
|-|-|
|`git init`|현재 디렉토리를 기준으로 git 저장소가 생성.|
|`git add .`|생성, 수정된 모든 파일을 스테이지에 올림.|
|`git add <파일/디렉토리 경로>`|생성, 수정된 일부 파일을 스테이지에 올림.|
|`git commit`|스테이지에 올려진 파일을 기록하는 것.|
|`git status`|파일 상태 확인하는 것.|
|`git log`|커밋한 기록을 보는 것|

## ※ WARNING
1. **현재 위치를 잘 확인한다.**
2. **Repo 안에서 repo (master)를 만들지 않는다. (Master 떠있으면 `git init` X)**
    1). 이미 git init을 한 곳 안에
    2). 하위 폴더를 만들고
    3). 그 하위 폴더에서 git init을 하지 않는다.

3. **Home(`~`)에서 init 하지 않는다.**
4. **(지금은) github에서 직접 수정하지 않는다.**

## 프로젝트 초기화 진행

### 계정 세팅

```sh
# (계정당 1회) 서명이 등록되지 않았다면, 계정용 서명 등록
$ git config --global user.name '내이름'
$ git config --global user.email 'github에서@쓸메일주소'
# 서명이 정상적으로 등록되었는지 확인
$ cat ~/.gitconfig  
```

### 프로젝트 생성부터 push까지

```sh
# 프로젝트 폴더 생성
$ mkdir new_project

# 프로젝트 폴더로 이동
$ cd new_project

# README 파일 & .gitignore 생성
$ touch README.md .gitignore

# gitignore.io 에 접속하여 필요한 내용 복-붙

# 폴더를 리포로 초기화
$ git init

# README & .gitignore 파일 add(tracking)
$ git add .

# commit
$ git commit -m 'first commit'

# github에서 원격 저장소 직접 생성

# 생성한 원격 저장소 등록  (origin 은 별명)
$ git remote add origin <URL>

# 등록된 저장소 확인
$ git remote -v

# 지금까지의 commit들 모아서 push
$ git push origin master
```
---

## 명령어 정리

1. 리포 초기화 시점에 1회 입력

```sh
$ git init 
```

2. 작업 후 스테이징

```sh
# 특정 파일만 add 할 때
$ git add <filename>
# 현재 폴더 전체를 add 할 때
$ git add .
```

3. 커밋 진행

```sh
# 메시지는 짧고 정확하게
$ git commit -m 'MESSAGE'
```


4. 모니터링 명령어

```sh
# 현재 Working Dir 과 Stage 상황 확인 (주기적으로 확인하자!)
$ git status

# commit 로그 
$ git log     
# commit 로그 짧게
$ git log --oneline
```

5. github 에 원격 저장소 생성하기 (github site에서 `New Repository`)
  
6. 원격 저장소(remote repo) 추가하기

```sh
$ git remote add origin <URL>
```

7. 원격 저장소 확인하기

```sh
$ git remote -v
```

8. 원격 저장소에 지금까지의 commit 들 PUSH 하기

```sh
$ git push origin master
```

9. 새로운 컴퓨터에서 기존 원격 저장소 복제하기
```sh
$ git clone <URL>
```

10. 원격 저장소의 내용 받아오기
```sh
$ git pull origin master
```

|상황|명령어|
|--|--|
|집에서 새로운 프로젝트 시작|`$ mkdir project`|
|프로젝트 폴더로 이동|`$ cd project`|
|리포 초기화|`$ git init`|
|README, .gitignore 생성|`$ touch README.md .gitignore`|
|파일 스테이징|`$ git add .`|
|커밋|`$ git commit -m 'first commit'`|
|원격저장소 생성|github 사이트에서 진행|
|원격 저장소 등록|`$ git remote add origin <URL>`|
|원격 저장소 PUSH|`$ git push origin master`|
|다른 컴퓨터에서 원격저장소 복제|`$ git clone <URL>`|
|작업|`add`, `commit`|
|귀가 직전|`$ git push origin master`|
|집 도착 이후|`$ git pull origin master`|
|작업|`add`, `commit`|
|작업 종료|`$ git push origin master`|
|다른 컴퓨터에서 반복|`$ git pull origin master`|


---

# code ~/.bash_profile

# alias gl='git log --oneline --graph'
# alias jn= 'jupyter notebook'

# $ git branch b1

# $ git switch b1

# $ git switch master

블랜치는 스티커와 비슷하다.

$ touch b1.txt

$ git switch b1

$ git add b1.txt

$ git switch master

$ git commit -m 'add b1.txt'

$ gl
$ code ~/.bash_profile
$ code ~/.bash_history

$ git branch b1
$ git switch master
$ git switch b1

$ touch b1.txt

$ git switch master

$ git add b1.txt
$ git switch master

$ git commit -m 'add b1.txt'

$ gl

$ git switch master 

$ gl

$ git switch b1

$ git add b1.txt

$ git commit -m 'more b1.txt'

$ git switch master

# $ git merge b1

$ git add .

$ git commit -m 'b1-1'

$ git branch b2

$ git switch b2

# $ git switch -c b2


$ rm b2.txt

# 충돌은 같은 파일에 같은 줄 건드릴 때 충돌이 일어남

Auto-merging master.txt
CONFLICT (content): Merge conflict in master.txt
Automatic merge failed; fix conflicts and then commit the result.

$ git merge b1
$ git add .
$ git commit -m 'Merge'


$ git branch -d b1 b2 c1

$ git branch -D b1 b2 c1 