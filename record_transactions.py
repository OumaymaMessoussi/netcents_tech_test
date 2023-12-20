from time import sleep
from blockcypher import get_broadcast_transactions
from sqlalchemy import BigInteger, Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.orm import Session

from global_variables import DB_NAME, PASSWORD, PORT, USERNAME

# PostgreSQL DB setup
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

unconfirmed_transactions = Table(
    "unconfirmed_transactions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("hash", String),
    Column("total", BigInteger),
    Column("fees", Integer),
    Column("inputs", String),
    Column("outputs", String),
)

# Create table if it does not exist
metadata.create_all(engine)


def record_unconfirmed_transactions():
    transactions = get_broadcast_transactions(limit=100)  # Max allowed is 100 in the documentation

    largest_transaction = max(transactions, key=lambda tx: tx["total"])

    # Check if the transaction is already recorded
    with Session(engine) as session:
        existing_entry = (
            session.query(unconfirmed_transactions)
            .filter(unconfirmed_transactions.c.hash == largest_transaction["hash"])
            .first()
        )

        if existing_entry is None:  # Record the largest transaction in the database
            session.execute(
                unconfirmed_transactions.insert().values(
                    hash=largest_transaction["hash"],
                    total=largest_transaction["total"],
                    fees=largest_transaction["fees"],
                    inputs=str(largest_transaction["inputs"]),
                    outputs=str(largest_transaction["outputs"]),
                )
            )
            session.commit()


if __name__ == "__main__":
    while True:
        record_unconfirmed_transactions()
        sleep(30)
