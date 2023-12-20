from flask import Flask, jsonify
from sqlalchemy import BigInteger, Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.orm import Session

from global_variables import DB_NAME, PASSWORD, PORT, USERNAME

app = Flask(__name__)

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


@app.route("/api/largest_transaction", methods=["GET"])
def get_largest_transaction():
    with Session(engine) as session:
        latest_transaction = (
            session.query(unconfirmed_transactions).order_by(unconfirmed_transactions.c.total.desc()).first()
        )

        if latest_transaction:
            result = {
                "hash": latest_transaction.hash,
                "total": latest_transaction.total,
                "fees": latest_transaction.fees,
                "inputs": eval(latest_transaction.inputs),
                "outputs": eval(latest_transaction.outputs),
            }
            return jsonify(result)
        else:
            return jsonify({"message": "No unconfirmed transactions recorded"})


if __name__ == "__main__":
    app.run()
