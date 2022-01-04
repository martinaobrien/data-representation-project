# GMIT-Data Representation: Project 2021

![alt text](https://github.com/martinaobrien/data-representation-project/blob/main/staticpages/GMIT-LOGO.jpg)

#### GMIT Higher Diploma in Data Analytics
#### Data Representation and Querying
#### Author: Martina O'Brien

## Overview of the Repository:
This repository contains the Data Representation and Querying Project submitted as part of the requirements of the higher Diploma in Data Analytics 2021/2022

## Purpose of the Project:
The purpose of this project is to create a Web Application in Flask that has a RESTful API that connects to a database table. The Web Application must include a Web Page that can consume the API (create,read, update and delete operations. 

The Web application created:
- displays information on films already stored in the database
- allows interaction to update, create or delete film entries already in the database
- implements error recognition if the wrong input is received in the table


## Contents of the Repository:
The repository contains the following files: 
- README.md - overview of the repository and implementation of the programme
- FilmDAO.py - the implementation of the code for the local host interface
- application.py - server for the programme
- create_database.py - creating the neccessary database for implementation by user (## only needed if you don't have a database called 'datarepresentation' already in your mysql)
- create_tables.py - creating the neccessary table for films for implementation by user
- dbconfig.py - contains username and password (this will not be uploaded to Github)
- dbconfigtemplate.py - this is the setting up for dbconfig.py (this is to be manipulated by users to access their mysqls)
- requirements.txt - contains neccessary packages
- index.html - browswer interface for the database
- .gitignore - files and applications that are ignored by Github to ensure implementation without errors
- License - License of the Repository
- staticpages folder - contains all static pages and images contained in the repositor


## Preparing to run the web application

### Prerequisites for this programme

- Python - can be downloaded from https://www.anaconda.com/
- My SQL - can be downloaded from https://www.mysql.com/
- Flask - can be installed through the command line with the following command: pip install Flask

### Downloading the repository
Under the repository name, click clone or download
You have an option to clone the repository to your machine or clone with HTTPs and using the URL, open Git Bask and redirect to the location where you are able to implement the code.


## Running the Web Application
- Navigate to your command line
- If needed, run the create_database.py as indicated in the Contents section
- Run the create_table.py to create the necessary table in your database
- Open application.py 
- Run application.py to initiate the web application

## License:
The repository is for use within the GNU General Public License 3.0. To find more on the license: https://www.gnu.org/licenses/gpl-3.0.en.html

  


