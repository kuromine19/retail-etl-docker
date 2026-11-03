"""Load retail CSV files from /data into PostgreSQL."""
import os


def get_engine():
    """TODO: build a SQLAlchemy engine from the POSTGRES_* environment variables."""
    raise NotImplementedError


def extract(path: str):
    """TODO: read the CSV into a pandas DataFrame."""
    raise NotImplementedError


def transform(df):
    """TODO: clean the data – drop bad rows, fix types, compute revenue = quantity * unit_price."""
    raise NotImplementedError


def load(df, engine):
    """TODO: write to postgres so that running twice does NOT duplicate rows."""
    raise NotImplementedError


if __name__ == "__main__":
    data_dir = os.environ.get("DATA_DIR", "/data")
    # TODO: loop over CSV files in data_dir and run extract -> transform -> load
