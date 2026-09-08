# Snowflake Engineer Study Plan (Beginner → Job-Ready)

**Total duration:** ~28 weeks (7 months), assuming 8-10 hours/week of study
**Adjust pace as needed** — the important thing is consistency, not speed.

---

## PHASE 1: Tech & Computer Basics (Weeks 1-2)

### Week 1 — Getting comfortable with a computer
- Learn to navigate your file system via terminal/command line (cd, ls/dir, mkdir, mv, rm)
- Install a code editor (VS Code — free and widely used)
- Learn what "the cloud" means: on-demand servers, storage, compute (watch a few intro videos on AWS/Azure/GCP basics)
- Create free accounts: GitHub, Snowflake trial (don't start using it yet)

### Week 2 — Data fundamentals
- Learn the difference between a database and a spreadsheet
- Understand rows, columns, tables, primary keys, foreign keys
- Learn what a "data type" is (string, integer, date, boolean)
- Install a free database tool locally (or just use Snowflake's web UI later) to poke around

**Milestone:** You can open a terminal, navigate folders, and explain what a table/row/column is.

---

## PHASE 2: SQL Mastery (Weeks 3-10) — the most important phase

### Week 3 — SELECT basics
- SELECT, FROM, WHERE, ORDER BY, LIMIT
- Comparison operators, AND/OR/NOT
- Practice: SQLBolt (free, interactive) — complete all basic lessons

### Week 4 — Filtering & sorting deeper
- LIKE, IN, BETWEEN, IS NULL
- Multiple sort conditions
- Practice: 20+ problems on LeetCode SQL (Easy tier)

### Week 5 — Aggregation
- COUNT, SUM, AVG, MIN, MAX
- GROUP BY, HAVING (vs WHERE)
- Practice: build 5 small "reports" from a sample dataset (e.g. total sales by category)

### Week 6 — JOINs (the hard part — go slow)
- INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN
- Joining 3+ tables
- Practice: draw joins on paper before writing SQL — visualize which rows match

### Week 7 — Subqueries & CTEs
- Subqueries in WHERE, FROM, SELECT
- Common Table Expressions (WITH clause)
- When to use a CTE vs a subquery vs a temp table

### Week 8 — Window functions
- ROW_NUMBER, RANK, DENSE_RANK
- LAG, LEAD
- Running totals with SUM() OVER()
- Practice: LeetCode SQL Medium problems

### Week 9 — Data modification & modeling basics
- INSERT, UPDATE, DELETE
- CASE WHEN statements
- Star schema vs snowflake schema (fact tables, dimension tables)
- OLTP vs OLAP — when each is used

### Week 10 — SQL review & assessment
- Take a full SQL assessment (Mode Analytics or StrataScratch free tier)
- Redo any problem types you struggled with
- **Gate check:** if joins and window functions still feel shaky, spend an extra week here before moving on

**Milestone:** You can write multi-table joins, aggregations, and window functions confidently without looking up syntax constantly.

---

## PHASE 3: Data Warehousing Concepts (Weeks 11-12)

### Week 11 — Warehousing theory
- What a data warehouse is and why it differs from an operational database
- ETL vs ELT — the shift toward ELT in modern cloud warehouses
- Batch vs streaming data
- Data lake vs data warehouse vs lakehouse

### Week 12 — Cloud platform basics
- Pick one cloud provider (AWS is most common) and learn basics of S3 (object storage)
- Understand IAM concepts (users, roles, permissions) at a high level
- Learn what an API is and how data pipelines typically connect systems

**Milestone:** You can explain to someone else why companies use a data warehouse instead of just querying production databases directly.

---

## PHASE 4: Snowflake Fundamentals (Weeks 13-16)

### Week 13 — Snowflake architecture & interface
- Sign up / return to your Snowflake free trial
- Learn the 3-layer architecture: storage, compute (virtual warehouses), cloud services
- Navigate Snowsight (the web UI)
- Create databases, schemas, and tables manually

### Week 14 — Virtual warehouses & compute
- Create and resize virtual warehouses
- Understand auto-suspend/auto-resume
- Run queries and inspect the Query Profile
- Learn about caching (result cache, warehouse cache)

### Week 15 — Roles & access control
- Understand RBAC: roles, grants, ownership
- Create custom roles and assign privileges
- Learn the default roles (ACCOUNTADMIN, SYSADMIN, SECURITYADMIN)

### Week 16 — Micro-partitions & clustering (intro)
- Learn how Snowflake automatically partitions data
- Understand clustering keys at a conceptual level
- Explore Time Travel and Zero-Copy Cloning hands-on

**Milestone:** You can create a database/schema/warehouse from scratch, write and tune basic queries, and explain Snowflake's architecture.

---

## PHASE 5: Data Loading & Ingestion (Weeks 17-19)

### Week 17 — Bulk loading
- Learn COPY INTO for loading CSV files from a stage
- Create internal and external stages
- Load a sample CSV dataset (e.g. from Kaggle) into a Snowflake table

### Week 18 — Semi-structured data
- Work with JSON using the VARIANT data type
- Use FLATTEN to unnest JSON arrays
- Load a Parquet file into Snowflake

### Week 19 — Snowpipe & continuous ingestion
- Set up Snowpipe for auto-ingestion from an S3 bucket
- Understand the difference between batch loads and Snowpipe
- (Optional) explore Snowflake connectors: Python connector basics

**Milestone:** You've loaded at least 2 different file formats (CSV + JSON or Parquet) into Snowflake tables using both COPY INTO and a stage.

---

## PHASE 6: Transformation & Automation (Weeks 20-23)

### Week 20 — Views & stored procedures
- Regular views vs materialized views
- Write basic stored procedures (SQL scripting)
- When to use a view vs a procedure vs a task

### Week 21 — Streams & Tasks
- Learn Streams for change data capture (CDC)
- Build a Task to automate a transformation on a schedule
- Chain Streams + Tasks together for a simple pipeline

### Week 22 — Intro to dbt
- Install dbt and connect it to your Snowflake trial account
- Learn dbt models, sources, and the ref() function
- Build your first dbt model transforming raw data into a clean table

### Week 23 — dbt deeper + testing
- Learn dbt tests (unique, not_null, relationships)
- Build a small dbt project with 3-5 models and a staging/marts structure
- Learn dbt documentation generation

**Milestone:** You have a working dbt project connected to Snowflake with at least one full pipeline: raw data → staging → transformed mart table.

---

## PHASE 7: Performance, Cost & Governance (Weeks 24-25)

### Week 24 — Performance & cost
- Read and interpret Query Profile output
- Learn warehouse sizing trade-offs (bigger ≠ always better)
- Set up Resource Monitors to control credit usage
- Learn about clustering keys and when they matter

### Week 25 — Security & governance
- Dynamic data masking policies
- Row access policies
- Object tagging for data classification
- Review Time Travel, Fail-safe, and Zero-Copy Cloning use cases

**Milestone:** You can look at a slow query and identify at least 2 possible causes/fixes, and explain how to control Snowflake costs.

---

## PHASE 8: Portfolio & Certification (Weeks 26-28)

### Week 26 — Build project #1
- Pick a public dataset (Kaggle, data.gov, etc.)
- Build a full pipeline: load raw data → transform with dbt → create final reporting tables
- Push the project to GitHub with a clear README

### Week 27 — Build project #2 + SnowPro prep
- Build a second project showcasing something different (e.g. semi-structured JSON handling, or a Streams/Tasks automation pipeline)
- Start studying for SnowPro Core Certification (use Snowflake's official study guide)

### Week 28 — Certification & job search prep
- Take the SnowPro Core Certification exam
- Polish your GitHub projects and resume
- Start applying to Data Engineer / Analytics Engineer roles that list Snowflake

**Milestone:** 2 portfolio projects on GitHub, SnowPro Core certification (or exam scheduled), and applications going out.

---

## Free resources to use throughout
- **SQL practice:** SQLBolt, LeetCode SQL, StrataScratch, Mode Analytics SQL Tutorial
- **Snowflake:** Snowflake free trial, Snowflake official documentation, Snowflake Quickstarts (guided hands-on labs)
- **dbt:** dbt Learn (free courses), dbt official docs
- **Datasets:** Kaggle, data.gov, Snowflake's sample datasets (included in trial)

## Tips for staying on track
- Don't skip the SQL phase even if it feels slow — it's the foundation everything else depends on
- Build something hands-on every week, even small — reading alone won't make it stick
- If a week's topic doesn't click, repeat it before moving forward rather than pushing through confused
- Join a community (r/snowflake, dbt Slack community) to ask questions when stuck
