# 🎵 Music Data Platform

An end-to-end data engineering project that ingests, cleans, transforms, and analyzes music data using **Python, PostgreSQL, Docker, dbt, and Streamlit**.

The project demonstrates a modern analytics pipeline from raw data to transformed analytical models and an interactive dashboard.

## 🏗️ Architecture

```text
Spotify Music Dataset
        │
        ▼
   Python / Pandas
        │
        ▼
  PostgreSQL (Docker)
        │
        ▼
   Raw Music Data
        │
        ▼
        dbt
        │
        ├── Staging
        │     └── stg_music_tracks
        │
        ├── Dimensions
        │     ├── dim_tracks
        │     └── dim_genres
        │
        ├── Fact
        │     └── fact_track_metrics
        │
        └── Analytics
              └── genre_performance
        │
        ▼
    Streamlit Dashboard
```

## 🛠️ Tech Stack

* **Python** — data ingestion and processing
* **Pandas** — data cleaning and transformation
* **PostgreSQL** — analytical database
* **Docker** — containerized PostgreSQL
* **dbt** — SQL transformations, modeling, and data testing
* **SQLAlchemy** — Python/PostgreSQL connection
* **Streamlit** — interactive analytics dashboard
* **Git/GitHub** — version control

## 📊 Dataset

The project uses a Spotify tracks dataset containing music metadata and audio features such as:

* Track ID
* Artists
* Album
* Track name
* Genre
* Popularity
* Danceability
* Energy
* Loudness
* Speechiness
* Acousticness
* Instrumentalness
* Liveness
* Valence
* Tempo

After cleaning and deduplication, the analytical pipeline contains approximately **89,740 unique tracks across 113 genres**.

## 🗄️ Data Models

dbt is used to transform the raw PostgreSQL data into analytics-ready models.

### Staging

**`stg_music_tracks`**

Cleans and prepares the raw music dataset for downstream transformations.

Materialized as a **view**.

### Dimensions

**`dim_tracks`**

Contains unique track-level information.

**`dim_genres`**

Contains the available music genres.

Both are materialized as **tables**.

### Fact

**`fact_track_metrics`**

Contains measurable track attributes such as popularity, energy, danceability, tempo, and other audio features.

Materialized as a **table**.

### Analytics

**`genre_performance`**

Aggregates track-level metrics by genre to answer questions such as:

* Which genres have the highest average popularity?
* Which genres are the most energetic?
* Which genres have the highest danceability?
* How many tracks exist in each genre?

Materialized as a **table**.

## 🧪 Data Quality

dbt tests are used to validate the analytical models.

Current tests include:

* `not_null` checks
* `unique` checks
* Track ID validation
* Genre validation

Example:

```bash
dbt test
```

Current pipeline:

```text
8 data tests
8 passed
0 failed
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd music-data-platform
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🐘 Start PostgreSQL with Docker

Make sure Docker Desktop is running.

Start the PostgreSQL container:

```bash
docker start music-postgres
```

The project uses the following connection:

```text
Host: localhost
Port: 5433
Database: music_db
User: music_user
```

The Docker port mapping is:

```text
5433:5432
```

This means:

```text
Windows host → Docker PostgreSQL
localhost:5433 → container:5432
```

You can verify the container:

```bash
docker ps
```

## 📥 Load the Raw Dataset

Run the project's ingestion script:

```bash
python src/<ingestion_script>.py
```

This loads the raw music data into PostgreSQL.

The raw table is:

```text
raw_music_tracks
```

## 🔧 Run dbt

Move into the dbt project:

```powershell
cd dbt_music
```

Check the database connection:

```bash
dbt debug
```

You should see:

```text
Connection test: [OK connection ok]
All checks passed!
```

### Build the models

```bash
dbt run
```

This creates:

```text
analytics.stg_music_tracks
analytics.dim_tracks
analytics.dim_genres
analytics.fact_track_metrics
analytics.genre_performance
```

### Run data quality tests

```bash
dbt test
```

### Generate dbt documentation

```bash
dbt docs generate
```

### View dbt documentation

```bash
dbt docs serve --port 8081
```

Then open:

```text
http://localhost:8081
```

The dbt documentation provides an overview of the models, columns, dependencies, and database lineage.

## 📈 Run the Dashboard

From the project root:

```powershell
cd ..
```

Start Streamlit:

```bash
streamlit run dashboard.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

The dashboard provides interactive analysis of music data, including genre performance and track metrics.

## 🔍 Example Analytics

The `genre_performance` model can be queried using:

```sql
SELECT *
FROM analytics.genre_performance
ORDER BY avg_popularity DESC
LIMIT 10;
```

Example output:

```text
track_genre | track_count | avg_popularity | avg_energy | avg_danceability
------------+-------------+----------------+------------+------------------
k-pop       | 916         | 59.42          | 0.68       | 0.64
pop-film    | 815         | 59.10          | 0.60       | 0.59
metal       | 232         | 56.42          | 0.84       | 0.48
```

## 📁 Project Structure

```text
music-data-platform/
│
├── data/
│   └── raw/
│
├── src/
│   └── ...
│
├── dbt_music/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_music_tracks.sql
│   │   │
│   │   ├── marts/
│   │   │   ├── dim_tracks.sql
│   │   │   ├── dim_genres.sql
│   │   │   └── fact_track_metrics.sql
│   │   │
│   │   └── analytics/
│   │       └── genre_performance.sql
│   │
│   ├── tests/
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   └── dbt_project.yml
│
├── dashboard.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔄 Complete Pipeline

The complete workflow is:

```bash
# 1. Start PostgreSQL
docker start music-postgres

# 2. Activate environment
.\.venv\Scripts\Activate.ps1

# 3. Load raw data
python src/<ingestion_script>.py

# 4. Run dbt transformations
cd dbt_music
dbt run

# 5. Run data quality tests
dbt test

# 6. Start dashboard
cd ..
streamlit run dashboard.py
```

## 🎯 Project Goals

This project was built to demonstrate practical data engineering concepts including:

* Data ingestion
* Data cleaning
* PostgreSQL database design
* Dockerized infrastructure
* ELT architecture
* dbt transformations
* Dimensional modeling
* Fact and dimension tables
* Data quality testing
* Analytical SQL
* Data visualization
* Reproducible development workflows

## 🔮 Future Improvements

* Add Apache Airflow for workflow orchestration
* Add automated data ingestion
* Introduce dbt incremental models
* Add more advanced data quality tests
* Add cloud storage such as AWS S3
* Move analytics to a cloud data warehouse
* Add CI/CD with GitHub Actions
* Add pipeline monitoring and logging

## 👨‍💻 Author

**Parbat Sunuwar**

Backend & Data Engineering Developer

GitHub: `<your-github-url>`

Portfolio: `<your-portfolio-url>`
