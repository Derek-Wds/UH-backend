## Step 1
Run `docker build -t nerd/server .`

## Step 2
Run `docker run -d -p 13306:3306 --name=mysql-server --env="MYSQL_ROOT_HOST=%" nerd/server`

## Step 3
Run `./import.sh`