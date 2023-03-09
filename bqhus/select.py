from google.cloud import bigquery
from jinja2 import Template, Environment, FileSystemLoader


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


def select_with_template(
    client, template_dir, template_name, template_parameters={}, query_parameters=[]
):
    env = Environment(loader=FileSystemLoader(template_dir, encoding="utf8"))
    tmpl = env.get_template(template_name)
    query = tmpl.render(template_parameters)

    return select(client, query, query_parameters)
