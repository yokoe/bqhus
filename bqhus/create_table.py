from google.cloud import bigquery
from datetime import date, timedelta, datetime, timezone
from google.cloud.bigquery import Table


def create_table(
    table_id, query, query_parameters=[], overwrite=False, project=None, client=None
):
    c = client
    if c is None:
        c = bigquery.Client(project=project)

    write_disposition = bigquery.WriteDisposition.WRITE_EMPTY
    if overwrite:
        write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    job_config = bigquery.QueryJobConfig(
        destination=table_id,
        write_disposition=write_disposition,
        query_parameters=query_parameters,
    )
    query_job = c.query(query, job_config=job_config)
    query_job.result()


def create_temp_table(
    table_id,
    query,
    query_parameters=[],
    days=1,
    overwrite=False,
    project=None,
    client=None,
):
    c = client
    if c is None:
        c = bigquery.Client(project=project)
    create_table(
        table_id=table_id,
        query=query,
        query_parameters=query_parameters,
        overwrite=overwrite,
        project=project,
        client=c,
    )

    table = c.get_table(Table.from_string(table_id))
    expiration = datetime.now(timezone.utc) + timedelta(days=days)
    table.expires = expiration
    table = c.update_table(table, ["expires"])
