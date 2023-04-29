# Use an official Python runtime as a parent image
FROM apache/airflow:2.4.1

USER root

# Create the airflow group and add the airflow user to it
RUN groupadd airflow && usermod -aG airflow airflow

# Install git
RUN apt-get update && \
    apt-get install -y git

RUN git config --global pull.rebase true 

# Install Rust
RUN apt-get update && \
    apt-get install -y curl && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Move .cargo directory to a location accessible by the airflow user
RUN mv /root/.cargo /home/airflow/.cargo

# Change the owner of .cargo directory to airflow
RUN chown -R airflow:airflow /home/airflow/.cargo

# Add Rust to the PATH
ENV PATH="/home/airflow/.cargo/bin:${PATH}"

COPY requirements.txt /opt/airflow/requirements.txt

USER airflow

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
