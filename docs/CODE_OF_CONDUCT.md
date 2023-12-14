# Project Structure

```
resemolnet-ai-assistatn-backend
├── .github
|   ├── development_actions.yml
|   ├── staging_actions.yml
|   ├── production_actions.yml
├── apps
|   ├── authentication
|   ├── book
|   ├── code
|   ├── user
|   ├── many_more
├── config
|   ├── settings
|   |   ├── __init__.py
|   |   ├── _sub_settings
|   |   |   ├── __init__.py
|   |   |   ├── _env_variables.py
|   |   |   ├── _logger.py
|   |   |   ├── _jwt.py
|   |   |   ├── _api.py
|   |   |   ├── _security.py
|   |   ├── base.py
|   |   ├── development.py
|   |   ├── local.py
|   |   ├── production.py
|   |   ├── stage.py
|   ├── __init__.py
|   ├── asgi.py
|   ├── urls.py
|   ├── wsgi.py
├── docs
|   ├── CHANGELOG.md
|   ├── CODE_OF_CONDUCT.md
|   ├── CONTRIBUTING.md
├── scripts
|   ├── nginx
|   |   ├── default.conf
├── .env
├── .gitignore
├── docker-compose-dev.yml
├── docker-compose-stage.yml
├── docker-compose.yml
├── Dockerfile
├── example.env
├── manage.py
├── requirements.txt
├── README.md

```

## .github
 This directory contains GitHub Actions configuration files. It includes two files, development_actions.yml and staging_actions.yml, which likely define automated actions and workflows to be executed during development and staging phases, respectively.

## apps
 This directory contains individual Django applications that represent distinct components of the project. Each app is a self-contained module with its models, views, templates, and tests.

## config
The config directory contains configuration settings for the Django project. It helps to keep the settings organized and allows customization for different environments. Key files and directories within this folder are:

### settings
 A package containing different environment-specific settings files, like base.py, development.py, local.py, production.py, and stage.py, each representing settings for different deployment environments (development, local, production, and staging).

### _sub_settings
 A sub-package containing specific settings files divided by purpose, like _env_variables.py for environment variables configuration, _logger.py for logging settings, rest_framework.py for Django REST framework configuration, and _security.py for security-related settings like access_keys.

We are importing this all sub settings to base.py, so that we could keep clean the base.py settings file.


## docs
This directory contains documentation related to the project. It includes files such as CHANGELOG.md, which lists changes and updates to the project over time, CODE_OF_CONDUCT.md, which outlines the code of conduct for contributors and community members, CONTRIBUTING.md, which provides guidelines for contributing to the project, and README.md, the main documentation file that gives an overview of the project.

## scripts
 The scripts directory contains various utility scripts for the project. In this case, it includes an nginx folder with a default.conf file. There could be other scripts as well in future.

## .env
 This file is used to store environment-specific variables, like secret keys, database credentials, and other sensitive information. It helps to keep the sensitive information separate from the codebase.

## .gitignore 
This file specifies which files and directories should be ignored by Git version control. It usually includes files and directories that don't need to be tracked, like temporary 

## docker-compose.yml
The main Docker Compose file for the project. It includes configurations for running the project in a production-like environment.
There is also docker-compose-stage.yml and docker-compose-dev.yml file which specific to stage and dev server

## Dockerfile
The Dockerfile contains instructions for building a Docker image for the project. It specifies the base image, dependencies, and commands to set up the project environment.


## example.env
This file likely contains example environment variables. It helps other contributors to understand the required environment variables and their format.


## manage.py
This is the Django project management script. It provides various commands for running development servers, managing database migrations, and other project-related tasks.


## requirements.txt
A file containing a list of Python dependencies required for the project. It ensures that all the necessary packages are installed when setting up the project.