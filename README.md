# Airflow Docker Setup

This repository contains a Docker Compose setup for running Airflow locally.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/).

## Running Airflow Locally

To run Airflow locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone <your-repo-link>
    ```

2. Navigate to the repository's root directory:

    ```bash
    cd <your-repo-name>
    ```

3. Build the Docker image:

    ```bash
    docker-compose build
    ```

4. Start the Docker containers:

    ```bash
    docker-compose up -d
    ```

Airflow should now be running at `localhost:8080`.

To stop Airflow, run the following command in the terminal:

```bash
docker-compose down
```