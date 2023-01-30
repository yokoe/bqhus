# bqhus
BigQuery helper utils for Python

## How to use
### Create table from query
```
bqhus.create_table("foo.bar.sample", "SELECT * FROM `some.source.table`", project="my-project")
```

### Create temp table from query
```
bqhus.create_temp_table("foo.bar.sample", "SELECT * FROM `some.source.table`", days=1, project="my-project")
```

### Export table to GCS as csv
```
bqhus.extract_table_to_gcs_as_csv("foo.bar.sample", "my-bucket", "exported-table.csv.gz", gzip=True)
```
