## Individual Project3: Databricks ETL (Extract Transform Load) Pipeline

### Purpose:
* This repository hosts a comprehensive ETL (Extract, Transform, Load) pipeline project, designed to showcase the integration and utilization of Databricks, Delta Lake, and Spark SQL for efficient and scalable data processing. The primary purpose is to provide a practical framework for extracting data from various sources, transforming it using advanced Spark SQL techniques, and loading it into Delta Lake for optimized storage and retrieval. It serves as an educational and operational resource for data professionals and organizations seeking to enhance their data infrastructure and analytics capabilities.
* ETL-Query:  [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query
For the ETL-Query lab:
  * [E] Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well.
  * [T] Transform the data by cleaning, filtering, enriching, etc to get it ready for analysis.
  * [L] Load the transformed data into a SQLite database table using Python's sqlite3 module.
  * [Q] Write and execute SQL queries on the SQLite database to analyze and retrieve insights from the data.

### Setup Instructions:
1. Create a Databricks Cluster:
* Log into Databricks workspace, clone the repository with the github url to Databricks
* Navigate to `Compute` and create a new cluster, selecting the appropriate configuration for your needs.

2. Link GitHub Account:
* In the Databricks workspace, go to `User Settings`.
* Link your GitHub account for repository access with personal access token generated from Github
* Create secrets in Github to store the SERVER_HOSTNAME,ACCESS_TOKEN, JOB_ID
<img width="764" alt="Screen Shot 2023-11-16 at 01 52 49" src="https://github.com/nogibjj/IDS706_individualproject3_xk10/assets/143849077/91b35d0b-fbc5-4b46-9d4c-56717a639bbb">

3. Set Global Init Scripts:
* Go to `Admin Console` in Databricks.
* In the 'Global Init Scripts' section, add two environment variables: SERVER_HOSTNAME and ACCESS_TOKEN.

4. Configure Job Runs:
* Create a new job in Databricks.
* Add three tasks corresponding to the ETL stages.
* Ensure dependencies are included from `requirements.txt`.
* Run the pipeline to test whether it works

5. Data Preparation and Table Creation:
* Upload two datasets to Databricks File System (DBFS).
* click `create table with UI`
<img width="953" alt="Screen Shot 2023-11-16 at 01 31 22" src="https://github.com/nogibjj/IDS706_individualproject3_xk10/assets/143849077/0f5d930b-24d2-4414-9a27-f7eae3b43a13">
6. Testing the Setup:
* Run `make install` in workspace to install necessary dependencies from requirements.txt.
* Run `make test` in workspace to execute the test suite and validate the setup.
<img width="1426" alt="Screen Shot 2023-11-16 at 01 59 51" src="https://github.com/nogibjj/IDS706_individualproject3_xk10/assets/143849077/bf2f9de3-8006-4419-89da-0c3e9915344a">

### Query Visualization:
<img width="901" alt="qv1 (2)" src="https://github.com/nogibjj/IDS706_individualproject3_xk10/assets/143849077/3d6fc092-7fae-4bc1-bf8e-2fbd54445934">

### Recommendations to management team:
1. Leverage Insights: Use the processed data for informed decision-making, identifying key areas for growth and improvement.
2. Expand Data Capabilities: Plan for scaling the data infrastructure as needs grow, ensuring sustainability and performance.
Iterative Development: Continuously refine and update the ETL process to stay aligned with evolving data and business requirements.
3. Skill Development: Invest in training staff on Databricks, Delta Lake, and Spark SQL to build internal expertise and foster innovation.





