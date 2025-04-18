FROM python:3.9.1

RUN apt-get update

WORKDIR /app

RUN pip install pandas sqlalchemy psycopg2

COPY ingest_data.py .

# Downloaded from: https://www.kaggle.com/datasets/tiagoadrianunes/imdb-top-5000-tv-shows
COPY imdb_top_5000_tv_shows.csv .

CMD [ "python","ingest_data.py", \
    "--user=root", \
    "--password=root", \
    "--host=pg_database", \
    "--port=5432", \
    "--db=imdb_tv_shows", \
    "--table_name=tv_shows", \
    "--csv_name=imdb_top_5000_tv_shows.csv"]
