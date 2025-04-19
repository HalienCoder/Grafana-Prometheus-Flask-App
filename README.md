# Flask Notes App with Prometheus & Grafana Monitoring

This repository contains a **Flask Notes Application** integrated with **Prometheus** for metrics scraping and **Grafana** for visualizing those metrics. The application is containerized using Docker, with all services running in isolated containers, and uses a custom Docker network for communication between the services.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [How to Set Up and Run](#how-to-set-up-and-run)
6. [Running the App with Docker](#running-the-app-with-docker)
7. [Grafana Dashboard Setup](#grafana-dashboard-setup)

---

## 1. Introduction

This repository provides a simple **Flask Notes App** for managing notes, which includes features like user authentication, note creation, and deletion. To monitor the application’s performance, we have integrated **Prometheus** to scrape metrics such as request count and latency, and **Grafana** to visualize these metrics in a dashboard.

This setup is containerized with **Docker**, enabling the entire application (Flask app, Prometheus, Grafana) to run in isolated environments. By using these tools together, developers can monitor the health of the application, ensuring smooth operation in production.

---

## 2. Technologies Used

- **Flask (Python)**: For building the web application and handling routing, user authentication, and database operations.
- **Prometheus**: For collecting and scraping metrics about the Flask application’s performance (request count, latency, memory usage, etc.).
- **Grafana**: For visualizing the metrics collected by Prometheus, allowing users to monitor the health of the Flask app.
- **Docker**: For containerizing the entire application stack, ensuring isolation and easy portability.
- **Docker Compose** (optional): For managing multi-container Docker applications, though not used in this basic setup.

---

## 3. Project Structure

Here’s the folder structure for the application:

```
├── instance/
│   └── database.db            # SQLite database for storing user data and notes
├── website/
│   ├── static/
│   │   └── index.js           # JavaScript for handling dynamic frontend
│   ├── templates/
│   │     ├── base.html        # Base HTML template
│   │     ├── home.html        # Home page template
│   │     ├── login.html       # Login page template
│   │     └── signup.html      # Signup page template    
│   ├──  __init__.py           # Initializes the Flask app
│   ├── auth.py                # Handles authentication (login, signup)
│   ├── models.py              # Defines the database models
│   ├── views.py               # Handles the main routes and views
│   └── __pycache__/
├── .env                        # Environment variables (e.g., Flask secret key)
├── .gitignore                  # Ignores unwanted files and folders (e.g., __pycache__)
├── main.py                     # Main entry point to run the Flask app
├── requirements.txt            # Python dependencies
├── prometheus.yml              # Prometheus configuration file for scraping metrics
├── start.sh                    # Shell script to start the entire application stack
└── stop.sh                     # Shell script to stop and clean up the entire stack
```

---

## 4. Prerequisites

Before you begin, ensure that you have the following tools installed:

- **Docker**: To containerize the Flask app, Prometheus, and Grafana.
- **Docker Compose** (optional): For managing multi-container applications.
- **Git**: To clone the repository.
- **WSL (Windows Subsystem for Linux)**: If using Windows for a Linux-like experience.

---

## 5. How to Set Up and Run

### Step 1: Clone the Repository

To get started, you need to clone the repository. Run the following command:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Step 2: Install Docker and Docker Compose

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose** (if using): [Install Docker Compose](https://docs.docker.com/compose/install/)

### Step 3: Build Flask App Docker Image

Once the repository is cloned, you'll need to build the Flask app Docker image. This is done automatically in the `start.sh` script, but you can do it manually with:

```bash
docker build -t flask-notes-app .
```

### Step 4: Run the Application Stack

To start the Flask app, Prometheus, and Grafana, run the `start.sh` script:

```bash
chmod +x start.sh
./start.sh
```

This will:

- Build the Flask app Docker image.
- Start containers for the Flask app, Prometheus, and Grafana, each running in isolation.
- Set up the necessary networking between the containers.

You can access the following services:

- Flask app: [http://localhost:5000](http://localhost:5000)
- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3100](http://localhost:3100)

---

## Monitoring with Prometheus & Grafana

### 📊 6. Running the App with Docker

The `start.sh` script runs the entire application stack. Here's a breakdown of what it does:

- **Creates a custom Docker network** to allow containers to communicate.
- **Builds the Flask app Docker image** and starts it in a container named `notes-app`.
- **Starts Prometheus** with the configuration defined in `prometheus.yml` for scraping the metrics from the Flask app.
- **Starts Grafana**, allowing you to visualize the scraped metrics.

---

### 🖥️ 7. Grafana Dashboard Setup

After you’ve run the `start.sh` script and everything is up, follow these steps to visualize the Flask app metrics using **Grafana**:

#### 1. Log in to Grafana

- Open [http://localhost:3100](http://localhost:3100) in your browser.
- Log in with the default credentials:
  - **Username:** `admin`
  - **Password:** `admin` (you’ll be prompted to change it on the first login).

#### 2. Add Prometheus as a Data Source

- In the **left sidebar**, click the **gear icon** (⚙️) and select **Data Sources**.
- Click **Add data source** and select **Prometheus**.
- Set the **URL** as: `http://prometheus:9090`.
- Click **Save & Test** to confirm the connection.

#### 3. Create a Dashboard

- In the **left sidebar**, click the **plus icon** (➕) and choose **Dashboard**.
- Click **Add new panel** to begin creating your first panel.
- Choose **Prometheus** as the data source.
- In the **Query** section, you can start adding Prometheus queries, for example:
  - **Request Count**: `app_requests_total`
  - **Request Latency**: `app_request_latency_seconds`
  - **Memory Usage**: `container_memory_usage_bytes`

#### 4. Customize the Dashboard

- Customize the visual appearance (e.g., graphs, legends, etc.).
- Set the time range, units, and labels.
- Save the dashboard by clicking the **disk icon** in the top-right corner and providing a name (e.g., “Flask App Monitoring”).

Now, you should see the Flask app metrics being scraped and displayed in Grafana!
