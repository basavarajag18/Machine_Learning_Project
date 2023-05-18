## Start Machine Learning Project

## Software and account Requirements
1. [Github Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS-code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/download)

Creating conda environment
...

conda create -p venv python==3.7 -y
...

conda activate venv/
....
or

conda activate venv
....

pip install -r requirements.txt

To add files ti git
...
git add .
....
or
git add <file_name>
...

> To ignore file or folder from git, we can write the name of the file/folder in .gitignore file

To check the git status
...
To check all version maintained by git
...
git log
....

To create version/commit  all changes by git
...
git commit -m "Message"
...

To send version/chenges to github
...
git push origin main
...
To check remote url
....
git remote -v
