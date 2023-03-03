from google.cloud import bigquery


def select_as_dicts(client, query, query_parameters=[]):
    job_config = bigquery.QueryJobConfig(query_parameters=query_parameters)
    query_job = client.query(query, job_config=job_config)
    return [dict(row) for row in query_job]
