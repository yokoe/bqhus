from google.cloud import bigquery
from datetime import date, timedelta, datetime, timezone
from google.cloud.bigquery import Table


def create_temp_table(table_id, query, query_parameters=[], days=1):
    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
        destination=table_id,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        query_parameters=query_parameters,
    )
    query_job = client.query(query, job_config=job_config)
    query_job.result()

    table = client.get_table(Table.from_string(table_id))
    expiration = datetime.now(timezone.utc) + timedelta(days=days)
    table.expires = expiration
    table = client.update_table(table, ["expires"])
