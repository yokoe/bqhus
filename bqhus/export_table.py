from google.cloud import bigquery
from google.cloud.bigquery import Table


def extract_table_to_gcs_as_csv(
    table_id,
    gcs_bucket,
    object_name,
    location=None,
    field_delimiter=",",
    gzip=False,
    print_header=True,
    project=None,
):
    destination_uri = f"gs://{gcs_bucket}/{object_name}"

    client = bigquery.Client(project=project)

    job_config = bigquery.job.ExtractJobConfig()
    if gzip:
        job_config.compression = bigquery.Compression.GZIP
    job_config.field_delimiter = field_delimiter
    job_config.print_header = print_header

    extract_job = client.extract_table(
        Table.from_string(table_id),
        destination_uri,
        location=location,
        job_config=job_config,
    )

    extract_job.result()

    return destination_uri
