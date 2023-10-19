# Gspread in Airflow

<img src="https://img.shields.io/badge/gspread-5.10.0-blue"/> <img src="https://img.shields.io/badge/python-3.10.2-blue"/> <img src="https://img.shields.io/badge/airflow-2.5.1-blue">

## 1. Description

This project was constructed in order to create an Airflow DAG to send data to a Google Spreadsheet. 


## 2. What you need to know 

In order to use this project, you have to create your own Google Service Account on [Google Cloud Platform](https://console.cloud.google.com/). 


## 3. Installation

You can clone this repository using the code below: 

```
git clone https://github.com/camila-marquess/airflow-gspread-dag.git
```

Before running Airflow, make sure you have installed docker in your OS. If you do not, follow this steps based on your OS: [Installing Docker Compose](https://docs.docker.com/desktop/install/windows-install/).

In order to start Airflow you have to run: 

```
docker-compose up -d
```

Then you can visualize the Airflow UI by accessing `localhost:8080` on your browser. The default login and password are: `airflow`.

In order to stop the containers, you can run: 

```
docker-compose down
```

If you prefer, I've explained all the installation process with more details here: [Gspread in Airflow](https://medium.com/@camila-marquess/gspread-in-airflow-3728abe4b617).
