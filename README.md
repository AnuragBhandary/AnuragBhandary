<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" alt="Anurag Navin Bhandary, backend engineer: systems that survive failure" width="100%">
</picture>

Most of my projects start with a simple question: what happens when a worker crashes, a client drops, or a node dies halfway through? So I build the system, break it on purpose, and measure what survives. Here is one of those runs, replayed from my [job scheduler](https://github.com/AnuragBhandary/Distributed-Job-Scheduler)'s benchmark:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/chaos-dark.svg">
  <img src="assets/chaos-light.svg" alt="Chaos run: 50,000 jobs with a worker killed every minute, 0 lost, 0 duplicate effects" width="100%">
</picture>

I have an M.S. in Computer Science from the University of Texas at Arlington. At **Fayble Inc.**, an early-stage AI sports startup, I built the audio pipeline that turned LLM-written play-by-play into two-voice commentary, and replayed recorded games through Kafka into FastAPI and WebSockets.

- 🔭 **Open to** backend, data and full-stack roles, happy to relocate
- 🌱 **Learning** AWS beyond S3, and system design for interviews
- 🛠️ **Latest push** <!--NOW:START-->[Fraud-Detection-MLOps](https://github.com/AnuragBhandary/Fraud-Detection-MLOps): Card-fraud detection on IEEE-CIS: out-of-time evaluation, delayed-label features, cost-based decisions… <sub>(11 Oct 2026)</sub><!--NOW:END-->

---

## 🌐 Connect With Me

<p align="left">
<a href="https://linkedin.com/in/bhandary-anurag" target="_blank">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" height="48" width="48" alt="LinkedIn"/>
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<a href="https://anuragbhandary.github.io" target="_blank">
  <img src="https://anuragbhandary.github.io/favicon.svg" height="48" width="48" alt="Portfolio"/>
</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<a href="mailto:bhandaryanurag@gmail.com">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" height="48" width="48" alt="Email"/>
</a>
</p>

---

## 🔨 What I've Built

**Backend**

| Project | What it proves |
|---|---|
| [Distributed Job Scheduler](https://github.com/AnuragBhandary/Distributed-Job-Scheduler) | Job queue with leases, retries and a dead-letter queue. Workers killed every minute over 50,000 jobs: no job lost, no duplicate side effects. |
| [Real-Time Event Streaming](https://github.com/AnuragBhandary/Real-Time-Event-Streaming) | WebSocket fan-out across instances through Redis pub/sub. 1,000 live clients and 14,000+ forced reconnects with no duplicate or out-of-order events. |
| [Event Ticketing Platform](https://github.com/AnuragBhandary/Event-Ticketing-Platform) | BookMyShow-style seat booking in Spring Boot and React. A 200-buyer rush on the same seats sold none of them twice. |
| [Cloud-Native Platform](https://github.com/AnuragBhandary/Cloud-Native-Platform) | The job queue on Kubernetes with Terraform, Helm and KEDA autoscaling. A node killed mid-load loses no jobs. |

**Data**

| Project | What it proves |
|---|---|
| [CDC Pipeline](https://github.com/AnuragBhandary/CDC-Pipeline) | MySQL to PostgreSQL through Debezium and Kafka. 1 million change events with zero lost or duplicated rows, checked by checksums. |
| [NYC Taxi Postgres Tuning](https://github.com/AnuragBhandary/NYC-Taxi-Postgres-Tuning) | 38 million taxi trips in PostgreSQL. Partitioning and indexing cut the median query from 488 ms to 19 ms. |

**AI / ML**

| Project | What it proves |
|---|---|
| [Financial RAG QA](https://github.com/AnuragBhandary/Financial-RAG-QA) | Retrieval-augmented QA over 57,000 finance documents. Fine-tuning the embedding model raised nDCG@10 from 0.25 to 0.43. |
| [Fraud Detection MLOps](https://github.com/AnuragBhandary/Fraud-Detection-MLOps) | LightGBM on 590,000 card transactions, served with SHAP reasons. A cost-based decision rule cut fraud cost by 68%. |

---

## 🛠️ Tech Stack

<table align="center">
<tr>
<td align="center">
<img src="https://skillicons.dev/icons?i=py" width="48" alt="Python" /><br>
<sub><b>Python</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=java" width="48" alt="Java" /><br>
<sub><b>Java</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=ts" width="48" alt="TypeScript" /><br>
<sub><b>TypeScript</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=js" width="48" alt="JavaScript" /><br>
<sub><b>JavaScript</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=html" width="48" alt="HTML5" /><br>
<sub><b>HTML5</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=css" width="48" alt="CSS3" /><br>
<sub><b>CSS3</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=fastapi" width="48" alt="FastAPI" /><br>
<sub><b>FastAPI</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=spring" width="48" alt="Spring Boot" /><br>
<sub><b>Spring Boot</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=flask" width="48" alt="Flask" /><br>
<sub><b>Flask</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=nginx" width="48" alt="nginx" /><br>
<sub><b>nginx</b></sub>
</td>
</tr>
<tr>
<td align="center">
<img src="https://skillicons.dev/icons?i=react" width="48" alt="React" /><br>
<sub><b>React</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=vite" width="48" alt="Vite" /><br>
<sub><b>Vite</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=tailwind" width="48" alt="Tailwind CSS" /><br>
<sub><b>Tailwind CSS</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=vitest" width="48" alt="Vitest" /><br>
<sub><b>Vitest</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=kafka" width="48" alt="Kafka" /><br>
<sub><b>Kafka</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=redis" width="48" alt="Redis" /><br>
<sub><b>Redis</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=postgres" width="48" alt="PostgreSQL" /><br>
<sub><b>PostgreSQL</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=mysql" width="48" alt="MySQL" /><br>
<sub><b>MySQL</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=sqlite" width="48" alt="SQLite" /><br>
<sub><b>SQLite</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=pytorch" width="48" alt="PyTorch" /><br>
<sub><b>PyTorch</b></sub>
</td>
</tr>
<tr>
<td align="center">
<img src="https://skillicons.dev/icons?i=sklearn" width="48" alt="scikit-learn" /><br>
<sub><b>scikit-learn</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=aws" width="48" alt="AWS (S3)" /><br>
<sub><b>AWS (S3)</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=docker" width="48" alt="Docker" /><br>
<sub><b>Docker</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=kubernetes" width="48" alt="Kubernetes" /><br>
<sub><b>Kubernetes</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=terraform" width="48" alt="Terraform" /><br>
<sub><b>Terraform</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=prometheus" width="48" alt="Prometheus" /><br>
<sub><b>Prometheus</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=grafana" width="48" alt="Grafana" /><br>
<sub><b>Grafana</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=githubactions" width="48" alt="GitHub Actions" /><br>
<sub><b>GitHub Actions</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=git" width="48" alt="Git" /><br>
<sub><b>Git</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=linux" width="48" alt="Linux" /><br>
<sub><b>Linux</b></sub>
</td>
</tr>
</table>

<table align="center">
<tr>
<td><b>Frontend & Testing</b></td>
<td>
<img src="https://img.shields.io/badge/TanStack%20Query-242938?style=for-the-badge&logo=reactquery&logoColor=FF4154" alt="TanStack Query" />
<img src="https://img.shields.io/badge/React%20Router-242938?style=for-the-badge&logo=reactrouter&logoColor=CA4245" alt="React Router" />
<img src="https://img.shields.io/badge/React%20Hook%20Form-242938?style=for-the-badge&logo=reacthookform&logoColor=EC5990" alt="React Hook Form" />
<img src="https://img.shields.io/badge/Zod-242938?style=for-the-badge&logo=zod&logoColor=3E67B1" alt="Zod" />
<img src="https://img.shields.io/badge/Playwright-242938?style=for-the-badge" alt="Playwright" />
<img src="https://img.shields.io/badge/JUnit%205-242938?style=for-the-badge&logo=junit5&logoColor=25A162" alt="JUnit 5" />
<img src="https://img.shields.io/badge/Testcontainers-242938?style=for-the-badge" alt="Testcontainers" />
<img src="https://img.shields.io/badge/k6-242938?style=for-the-badge&logo=k6&logoColor=7D64FF" alt="k6" />
</td>
</tr>
<tr>
<td><b>Backend & Cloud</b></td>
<td>
<img src="https://img.shields.io/badge/WebSockets-242938?style=for-the-badge" alt="WebSockets" />
<img src="https://img.shields.io/badge/Flyway-242938?style=for-the-badge&logo=flyway&logoColor=CC0200" alt="Flyway" />
<img src="https://img.shields.io/badge/Helm-242938?style=for-the-badge&logo=helm&logoColor=white" alt="Helm" />
<img src="https://img.shields.io/badge/KEDA-242938?style=for-the-badge" alt="KEDA" />
</td>
</tr>
<tr>
<td><b>Data</b></td>
<td>
<img src="https://img.shields.io/badge/SQL-242938?style=for-the-badge" alt="SQL" />
<img src="https://img.shields.io/badge/dbt-242938?style=for-the-badge" alt="dbt" />
<img src="https://img.shields.io/badge/Airflow-242938?style=for-the-badge&logo=apacheairflow&logoColor=017CEE" alt="Airflow" />
<img src="https://img.shields.io/badge/BigQuery-242938?style=for-the-badge&logo=googlebigquery&logoColor=669DF6" alt="BigQuery" />
<img src="https://img.shields.io/badge/Debezium-242938?style=for-the-badge" alt="Debezium" />
<img src="https://img.shields.io/badge/pgvector-242938?style=for-the-badge&logo=postgresql&logoColor=4169E1" alt="pgvector" />
<img src="https://img.shields.io/badge/pandas-242938?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Polars-242938?style=for-the-badge&logo=polars&logoColor=CD792C" alt="Polars" />
<img src="https://img.shields.io/badge/Power%20BI-242938?style=for-the-badge" alt="Power BI" />
<img src="https://img.shields.io/badge/Excel-242938?style=for-the-badge" alt="Excel" />
<img src="https://img.shields.io/badge/Metabase-242938?style=for-the-badge&logo=metabase&logoColor=509EE3" alt="Metabase" />
</td>
</tr>
<tr>
<td><b>ML & LLMs</b></td>
<td>
<img src="https://img.shields.io/badge/LightGBM-242938?style=for-the-badge" alt="LightGBM" />
<img src="https://img.shields.io/badge/Optuna-242938?style=for-the-badge&logo=optuna&logoColor=white" alt="Optuna" />
<img src="https://img.shields.io/badge/SHAP-242938?style=for-the-badge" alt="SHAP" />
<img src="https://img.shields.io/badge/MLflow-242938?style=for-the-badge&logo=mlflow&logoColor=0194E2" alt="MLflow" />
<img src="https://img.shields.io/badge/Gemini-242938?style=for-the-badge&logo=googlegemini&logoColor=4285F4" alt="Gemini" />
<img src="https://img.shields.io/badge/Groq-242938?style=for-the-badge" alt="Groq" />
<img src="https://img.shields.io/badge/Ollama-242938?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
<img src="https://img.shields.io/badge/LangGraph-242938?style=for-the-badge&logo=langgraph&logoColor=white" alt="LangGraph" />
<img src="https://img.shields.io/badge/MCP-242938?style=for-the-badge&logo=modelcontextprotocol&logoColor=white" alt="MCP" />
<img src="https://img.shields.io/badge/ElevenLabs-242938?style=for-the-badge&logo=elevenlabs&logoColor=white" alt="ElevenLabs" />
<img src="https://img.shields.io/badge/ffmpeg-242938?style=for-the-badge&logo=ffmpeg&logoColor=007808" alt="ffmpeg" />
</td>
</tr>
</table>

---

## 🏆 LeetCode

I practise every day. The card below redraws itself every 6 hours.

<a href="https://leetcode.com/u/anuragb2901/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/leetcode-dark.svg">
  <img src="assets/leetcode-light.svg" alt="LeetCode stats for anuragb2901" width="100%">
</picture>
</a>

---

## 🎮 Off the Clock

I also make games. **Dev Run** is a small action platformer I coded in plain JavaScript on a canvas, no engine. It is hidden in my portfolio: press the controller in the dock to play.

<a href="https://anuragbhandary.github.io"><img src="assets/dev-run.gif" alt="Dev Run gameplay: the hero runs, jumps and slashes through the first zone" width="100%"></a>
