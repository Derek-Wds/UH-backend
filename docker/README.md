## Step 1
Run `docker build -t nerd/server .`

## Step 2
Run `docker run -d -p 15432:5432 --name=post-server nerd/server`

## Step 3
Run `./import.sh`