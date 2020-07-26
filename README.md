# Github's Extensive Extension - GithubExstension

GithubExstension is a web application that helps you analyze and track all the important changes and processes that are going in your repository.

Using our data analytics module, we fetch data from Github, analyze and visualize it so that it's simple and helpful. 

If you use GithubExstension, you will easily observe week's top contributors, most changed files, weekly code and commit frequency and so on.

![homepage view](https://i.ibb.co/bP4tsTW/Screenshot-from-2020-07-26-22-54-28.png)

## Installation and setup
First of all make sure you have `npm` and `node` version is up to `6.0.0` and `12.0.0` respectively. After that for linux based systems just clone the repository and after starting terminal in the base directory run command below:

    ./setup.sh
  
This makes sure all the needed environment is setup. After execution is done for running server get to `src/server` directory run:

    python3 manage.py runserver
    
For every new run of server keep order of the command, first in base directory run `source bin/activate` and after that run command above.
