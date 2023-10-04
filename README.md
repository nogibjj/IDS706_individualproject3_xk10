[![CI/CD Workflow](https://github.com/nogibjj/IDS706_miniproject5_xk10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_miniproject5_xk10/actions/workflows/cicd.yml)
## Python Script interacting with SQL Database⚽️📊
![4 17-etl-sqlite-RAW](https://github.com/nogibjj/sqlite-lab/assets/58792/b39b21b4-ccb4-4cc4-b262-7db34492c16d)

### Purpose:
* This repository offers a python-based solution for automating the extraction, transfomation and loading (ETL) process of the fifa countries and audience dataset (https://github.com/fivethirtyeight/data/blob/master/fifa/fifa_countries_audience.csv). The pipeline begins by extracting data from a CSV file and then structures and inserts it into a local SQLite3 database.
* ETL-Query:  [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query
For the ETL-Query lab:
  * [E] Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well.
  * [T] Transform the data by cleaning, filtering, enriching, etc to get it ready for analysis.
  * [L] Load the transformed data into a SQLite database table using Python's sqlite3 module.
  * [Q] Write and execute SQL queries on the SQLite database to analyze and retrieve insights from the data.

### Preparation:
* This project was forked from nogibjj/sqlite-lab
* The project incorporates an automated workflow managed through a Makefile, which efficiently handles various tasks. These tasks encompass installation (via "make install"), testing (via "make test"), code formatting (via "make format"), and code quality checks (via "make lint")
<img width="881" alt="Screen Shot 2023-10-04 at 12 03 52" src="https://github.com/nogibjj/IDS706_miniproject5_xk10/assets/143849077/1ebb6e7d-d801-4b8a-8663-817a77233eeb">
<img width="589" alt="Screen Shot 2023-10-04 at 12 04 54" src="https://github.com/nogibjj/IDS706_miniproject5_xk10/assets/143849077/4135b5a1-2e14-4915-861e-783fe9a58763">
* The data file fifa_countries_audience.csv includes the following variables:
  * country: IFA member country
  * confederation: Confederation to which country belongs
  * population_share: Country's share of global population (percentage)
  * tv_audience_share: Country's share of global world cup TV Audience (percentage)
  * gdp_weighted_share: Country's GDP-weighted audience share (percentage)

### This repo contains:
* external data (fifa data)
* `mylib`:
    * `extract.py`：contains functions that manage the data extraction process from the external datasource
    * `query.py`：facilitate the execution of SQL queries(supports custom SQL queries), offering CRUD operations (Create, Read, Update, Delete) to interact with the database
    * `transform_load.py`：handles the transformation of the extracted data to fit our desired schema, and then loads this transformed data into the SQLite3 database
* `main.py`: the primary script driving the project. It utilizes argparse to interpret user commands and facilitates the full ETL process, as well as further database interactions, by calling the relevant functions from the mylib directory.
* `test_main.py`: Contains unit tests for the functionalities offered in main.py. It ensures that the extraction, transformation, loading, and other database operations work as expected.



