## Start Machine Learning Project

## Software and account Requirements
1. [Github Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS-code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/download)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)

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

To setup CI/CD pipeline in heroku, we need 3 information
1. HEROKU_EMAIL= basavarajag17@gmail.com
2. HEROKU_API_KEY= 2c62b2e4-1fa6-4896-86ac-4286c7b858b6
3. HEROLU_APP_NAME= regression_applicatio

BUILD DOCKER IAMGE
...
docker build -t <image_name>:<tagname> .
...
> NOte: Image name for docker must be lower case

To list docker image
...
docker images
...

Run docker image
...

docker run -p 5000:5000 -e PORT=5000
...

To check running container in docker
...
docker ps
...

To stop docker container
...
 docker stop <container_id>
...


...
python setup.py install
