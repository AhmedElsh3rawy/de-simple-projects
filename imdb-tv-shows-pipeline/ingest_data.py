from time import time
import argparse
import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    csv_name = params.csv_name

    df = pd.read_csv(csv_name, nrows=100)

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    print(pd.io.sql.get_schema(df, table_name, con=engine))

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=500)
    df = next(df_iter)

    df.head(0).to_sql(name=table_name, con=engine, if_exists="replace")
    df.to_sql(name=table_name, con=engine, if_exists="append")

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df.to_sql(name=table_name, con=engine, if_exists="append")

            t_end = time()
            print("inserted another chunk..., took %.3f sec" % (t_end - t_start))

        except StopIteration:
            print("No more chrunks...!")
            break

        except Exception as e:
            print("An error accured: ", e)
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Insert a CSV data to postgres")
    parser.add_argument("--user", help="username for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")
    parser.add_argument(
        "--table_name", help="table name that we will write the data into"
    )
    parser.add_argument("--csv_name", help="name of the CSV file")

    args = parser.parse_args()
    main(args)
