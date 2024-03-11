# Bitcoin Wallet API

The Bitcoin Wallet API is a Flask-based application that allows users to manage Bitcoin transactions and balances. This README provides instructions on how to set up, run, and test the application.

## Features

- **Transaction Management**: Users can list all transactions, showing amounts transferred and whether the amount has been spent.
- **Balance Inquiry**: Provides the current balance in BTC and its equivalent in EUR.
- **Transfer Functionality**: Allows the creation of new transfers, simulating the movement of BTC between wallets.
- **Database Seeding**: Includes a script for initial seeding of the database with transactions for testing purposes.
- **Unit Testing**: Contains unit tests for utility functions to ensure the reliability of the application.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher installed
- pip for installing Python packages
- A virtual environment manager (optional, but recommended)

## Installation

1. Clone the repository to your local machine: git clone https://github.com/thomasabrina/bitcoin_wallet_api.git
2. Navigate to the project directory: cd bitcoin_wallet_api
3. Create a virtual environment (optional): python -m venv venv
4. Activate the virtual environment:
   - On Windows: .\venv\Scripts\activate
   - On Unix or MacOS: source venv/bin/activate
5. Install the required packages: pip install -r requirements.txt

## Initial Database Setup

To initialize the database with the necessary tables, run the following command: flask db upgrade


### Seeding the Database

A script named `seed.py` is provided to seed the database with initial data. Execute the script by running: python seed.py
This will populate the database with initial transactions and balances for testing purposes.

## Running the Application

To run the Bitcoin Wallet API, use the following command: flask run
The application will be accessible at `http://127.0.0.1:5000/`, where you can interact with the API endpoints.

## Running Unit Tests

Unit tests are an essential part of ensuring the reliability of the application. To run the unit tests for utility functions, execute the `test_utils.py` file directly with Python. This can be done as follows: python test_utils.py
This command will run the tests defined in the `test_utils.py` file. Ensure you are in the root directory of the project when running this command.

## API Endpoints

The following are the main endpoints provided by the Bitcoin Wallet API:

- `GET /transactions` - List all transactions.
- `GET /balance` - Show the current balance.
- `POST /transfer` - Create a new transfer.

Refer to the API documentation for detailed information on request and response formats.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.