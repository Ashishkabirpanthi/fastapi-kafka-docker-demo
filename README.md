# termtrix-kafka-demo

# Kafka Docker FastAPI Demo

A complete **Kafka setup using Docker Compose** with **FastAPI producer and consumer** services.

This repository demonstrates how to run **Apache Kafka with Docker**, connect it to a **FastAPI application**, and implement a basic **Kafka producer and consumer** workflow.

This project is intended as a **Kafka Docker demo and reference setup**.


This is **only a demo/reference implementation**, intended for learning and experimentation.

---

## ✨ Features

- FastAPI-based producer and consumer services
- Apache Kafka + Zookeeper
- Fully Dockerized using Docker Compose
- Simple event publish/consume flow
- Clean and minimal project structure

---

## 🧱 Tech Stack

- Python
- FastAPI
- Apache Kafka
- Docker & Docker Compose

---

## 📁 Project Structure

```text
.
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── producer.py      # Kafka producer logic
│
|-- worker/
|  └── consumer.py      # Kafka consumer logic   
├── Dockerfile
├── Dockerfile.consumer
├── docker-compose.yml
├── pyproject.toml
└── README.md
