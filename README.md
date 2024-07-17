 # DocspertHealth Account Management Web App

This is a Django web application for managing accounts. It allows users to import accounts from a CSV file, list all accounts, view account information, and transfer funds between accounts. The project uses both Django templates and Django REST Framework (DRF) views, and the API is documented using Swagger.

## Features

- **Import Accounts**: Upload a CSV file to import accounts.
- **List Accounts**: View a list of all accounts.
- **Account Information**: View details of a specific account.
- **Transfer Funds**: Transfer funds between two accounts.

## Project Structure

- `import_accounts.html`: Template for importing accounts.
- `list_accounts.html`: Template for listing accounts.
- `account_info.html`: Template for viewing account information.
- `transfer_funds.html`: Template for transferring funds.
- `views.py`: Contains both Django template views and DRF views.
- `serializers.py`: Serializers for the DRF views.

## Django Template Views

- `ImportAccountsView`: Handles the import of accounts from a CSV file.
- `ListAccountsView`: Displays a list of all accounts.
- `AccountInfoView`: Displays information about a specific account.
- `TransferFundsView`: Handles the transfer of funds between accounts.

## DRF API Views

- `ImportAccountsAPIView`: API endpoint to import accounts from a CSV file.
- `ListAccountsAPIView`: API endpoint to list all accounts.
- `AccountInfoAPIView`: API endpoint to get account information.
- `TransferFundsAPIView`: API endpoint to transfer funds between accounts.

## API Documentation

The API is documented using Swagger. You can access the Swagger UI at `/swagger/`.

## Running the Project

### Prerequisites

- Docker
- Docker Compose

### Building and Running the Docker Image

1. **Build the Docker Image**:

    ```bash
    docker build -t account_management_app .
    ```

2. **Run the Docker Container**:

    ```bash
    docker run -d -p 8000:8000 account_management_app
    ```

3. **Access the Application**:

    Open your web browser and go to `http://localhost:8000`.

### Docker Compose

You can also use Docker Compose to run the application along with a PostgreSQL database.

### `docker-compose.yml`

```yaml
version: '3'

services:
  web:
    build: .
    command: gunicorn docsperthealth.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: your_db_name
      POSTGRES_USER: your_db_user
      POSTGRES_PASSWORD: your_db_password

volumes:
  postgres_data:
