#!/bin/bash

python3 ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=imdb_tv_shows \
    --table_name=tv_shows \
    --csv_name=imdb_top_5000_tv_shows.csv
