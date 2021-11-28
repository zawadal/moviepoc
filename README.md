###  Objective
This project is meant to deliver command for getting movie rattings from http://www.omdbapi.com website 

### Language
POC is prepared with Python version 3.9 - no additional libraries required. Project can be run using docker as a container. Docker is using python:3.9 as base.

### Preparations
In order to execute API query towards movie DB we need to have valid API key. Key can be requested under: https://www.omdbapi.com/apikey.aspx. 

Under root directory there is a file .env-example. Rename it to .env and fill with right API key in order to have fully operational application. 

### Build
In order to execute project we need to build docker image. This step is automatically performed when using docker-compose command. 

When using regular docker command to build project we need to issue following docker command:

`docker build -t <image tag> .`

### Execution
To execute  command and get Rotten Tomatoes rating for particular movie we can execute docker-compose command as follows:

`docker-compose run rotten --movie "Tomorrow never dies"`

Using regular docker command: 

`docker run --env-file .env rotten --movie "Dune"`

 