## Welcome to my Github.io
This is the repository for my little project: **ETL Pipeline**

The pipeline includes:
- **Extract** stage: I extract data logs from my app server. This can be done easily with **Google Logs Explorer** tool when deploying on Google Kubernetes Engine. For simplicity, I will store them in the '/logs' folder
- **Transform** stage: I use **pandas** to process and transform data to expected format, and query only necessary columns
- **Load** stage: Here, I use **MySQL** database to store my processed data

**How can I improve this?**

I will deploy a ETL pipeline on GCP, basing on Dataflow and Big Query. That will automate lots of stuffs, and sound more interesting


