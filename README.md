# Full-Stack Predictive Maintenance System

This project provides a complete, containerized system for simulating, ingesting, and retrieving IoT telemetry data. It's built with Python, FastAPI, SQLAlchemy, and MySQL, and is designed for scalability and production use.

## Features

-   **FastAPI Backend**: A high-performance, modern API for all data interactions.
-   **Telemetry Simulator**: A background service that continuously generates and stores realistic IoT data.
-   **MySQL Database**: Robust and reliable data storage for telemetry records.
-   **Dockerized Environment**: All services are containerized for easy setup and deployment.
-   **Modular & Scalable**: The codebase is organized into logical services, models, and utilities for easy maintenance and extension.

## Tech Stack

-   **Language**: Python 3.11+
-   **Framework**: FastAPI
-   **Database**: MySQL
-   **ORM**: SQLAlchemy
-   **Containerization**: Docker & Docker Compose
-   **Schema Validation**: Pydantic

## Getting Started

### Prerequisites

-   [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) must be installed on your system.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd predictive-maintenance
    ```

2.  **Create Environment File**
    Copy the example `.env.example` file to create your own local configuration. The default values are pre-configured to work with the `docker-compose` setup.
    ```bash
    cp .env.example .env
    ```

3.  **Build and Run the Services**
    Use the provided `Makefile` to start the application.
    ```bash
    make up
    ```
    This command will build the Docker images and start the `app` and `mysql` containers in the background.

### Usage

Once the services are running, you can access the following:

-   **API Interactive Docs (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
-   **Alternative API Docs (ReDoc)**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
-   **MySQL Database**: Connect on `localhost:3306` with credentials from your `.env` file.

### API Endpoints

The following endpoints are available:

-   `POST /telemetry/`: Manually insert a new telemetry record.
-   `GET /telemetry/`: Retrieve the latest telemetry data with pagination.
-   `GET /telemetry/{device_id}`: Get all telemetry records for a specific device.

You can test these endpoints directly from the interactive Swagger documentation.

## Application Management

Use the `Makefile` for easy management of the Docker environment:

-   **Stop all services**:
    ```bash
    make down
    ```
-   **View real-time logs**:
    ```bash
    make logs
    ```
-   **Rebuild the Docker images**:
    ```bash
    make build
    ```
-   **Access the application container's shell**:
    ```bash
    make shell
    ```

## Project Structure

The project is organized for clarity and scalability:
