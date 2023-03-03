from google.cloud import bigquery


class Select:
    def __init__(self, query_job):
        self.query_job = query_job

    def as_dicts(self):
        return [dict(row) for row in self.query_job]

    def first_as_dict(self):
        return self.as_dicts[0]


def select(client, query, query_parameters=[]):
    job_config = bigquery.QueryJobConfig(query_parameters=query_parameters)
    query_job = client.query(query, job_config=job_config)
    return Select(query_job=query_job)
