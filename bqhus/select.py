from google.cloud import bigquery
from jinja2 import Template, Environment, FileSystemLoader
from .create_table import create_table


class SelectTask:
    def __init__(self, client, query):
        self.client = client
        self.query = query
        self.query_parameters = []

    def params(self, params):
        self.query_parameters = params
        return self

    def job(self):
        job_config = bigquery.QueryJobConfig(query_parameters=self.query_parameters)
        return self.client.query(self.query, job_config=job_config)

    def as_dicts(self):
        query_job = self.job()
        return [dict(row) for row in query_job]

    def first_as_dict(self):
        return self.as_dicts()[0]

    def to_table(self, table_id, overwrite=False):
        return create_table(
            table_id,
            self.query,
            self.query_parameters,
            overwrite=overwrite,
            client=self.client,
        )


def select(client, query, query_parameters=[]):
    return SelectTask(client, query).params(query_parameters)


def select_with_template(client, template_dir, template_name, template_parameters={}):
    env = Environment(loader=FileSystemLoader(template_dir, encoding="utf8"))
    tmpl = env.get_template(template_name)
    query = tmpl.render(template_parameters)

    return select(client, query)
