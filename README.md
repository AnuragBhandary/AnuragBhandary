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
<img src="https://skillicons.dev/icons?i=fastapi" width="48" alt="FastAPI" /><br>
<sub><b>FastAPI</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=spring" width="48" alt="Spring Boot" /><br>
<sub><b>Spring Boot</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=react" width="48" alt="React" /><br>
<sub><b>React</b></sub>
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
</tr>
<tr>
<td align="center">
<img src="https://skillicons.dev/icons?i=mysql" width="48" alt="MySQL" /><br>
<sub><b>MySQL</b></sub>
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
<img src="https://skillicons.dev/icons?i=aws" width="48" alt="AWS (S3)" /><br>
<sub><b>AWS (S3)</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=githubactions" width="48" alt="GitHub Actions" /><br>
<sub><b>GitHub Actions</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=pytorch" width="48" alt="PyTorch" /><br>
<sub><b>PyTorch</b></sub>
</td>

<td align="center">
<img src="https://skillicons.dev/icons?i=sklearn" width="48" alt="scikit-learn" /><br>
<sub><b>scikit-learn</b></sub>
</td>
</tr>
</table>

<p align="center"><code>idempotency</code> · <code>backpressure</code> · <code>leases &amp; fencing</code> · <code>exactly-once effects</code> · <code>CDC</code> · <code>RAG</code> · <code>out-of-time validation</code></p>

---

## 🏆 LeetCode

<a href="https://leetcode.com/u/anuragb2901/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/leetcode-dark.svg">
  <img src="assets/leetcode-light.svg" alt="LeetCode stats for anuragb2901" width="100%">
</picture>
</a>

