# ETL pipeline on GCP

This ETL is deployed on Google Cloud, using Dataflow and BigQuery

This pipeline will:
- Ingest data file from Google Cloud Storage
- Convert the lines read to dictionary object
- Transform the data to a format that BigQuery can understand (date)
- Load the rows to BigQuery

**Prerequisites**:
- gcloud CLI is installed
- A project with billing account on GCP
- A Service Account with approriate permission (Editor)
- Enabled Dataflow API

## Create Cloud Storage Bucket
Storage Bucket is where we save all data for processing later. All data is saved as object. To create a bucket, use command:

`gsutil mb -c regional -l asia-southeast1 gs://linux-etl`

Here, we create a bucket name `linux-etl`

![bucket](img/bucket.png)

For convenient, we will export project name to `PROJECT` variable:

`export PROJECT=<your-project-ID>`

## Create a BigQuery dataset
Here, we will create a BigQuery dataset named `lake` with the command:

`bq mk lake`

## Build a Dataflow Pipeline
Firstly, install Apache Beam with pip:

`pip install apache-beam[gcp]==2.24.0`

Then, create `data_transform.py` file that will ingest data from Storage Bucket, transform date with Apache Beam pipeline and write result to BigQuery table 

To execute the pipeline, use the following command:

```python dataflow_python_examples/data_transformation.py --project=$PROJECT --region=us-central1 --runner=DataflowRunner --staging_location=gs://linux-etl/test --temp_location gs://linux-etl/test --input gs://linux-etl/data_files/head_usa_names.csv --save_main_session```

To check status of the job, On Google Cloud Console, we can navigate to Dataflow (Navigation Menu -> Dataflow). Here, we can see all job and their status

When our job's status is **Succeeded**, we can navigate BigQuery to see th result table


