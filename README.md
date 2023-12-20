The project was structured as follows:

global_varibales.py: contains the variables shared by some/all scripts for reusability.
main.py: contains the API end point logic.
record_transactions.py: contains the logic for fetching the blockchain transactions, finding the largest one and inserting it in the db.
query_db.py: script used to display the content of the table unconfirmed_transactions of transaction records.

PostgreSQL was used in this project on a MacOS (with Postgres.app) with conda environment (please refer to the yml file).


To test the code:
1. run the script record_transactions.py; this has a while loop that will take care of recording the largest transaction every 5min with a sleep.
2. run main.py to launch the Flask app, then navigate to http://127.0.0.1:5000/api/largest_transaction in your browser to see the largest transaction recorded to date.
3. running query_db.py will display the content of the table unconfirmed_transactions to make sure we're adding to it every 5min.

In all script runs, you need to set the following env variables for the DB: USERNAME, PASSWORD
