# Wander Data Platform

A production-oriented end-to-end data engineering platform built on Databricks.

This project demonstrates how to design, develop, test, deploy, and operate a modern data platform using Databricks, Lakeflow, Unity Catalog, GitHub, and automated CI/CD.

------------------------------------------------------------------------------------

## Project Objective

The goal of the Wander Data Platform is to build a production-style data engineering platform from source to analytics.

The platform will ingest data from the Databricks Wanderbricks data product, process it through a governed Medallion Architecture, apply automated data quality controls, and publish analytics-ready data products.

The project is designed to demonstrate production engineering practices including:

- Git-based development
- Pull request workflows
- Automated testing
- CI/CD with GitHub Actions
- Environment-specific deployments
- Data quality and validation
- Unity Catalog governance
- Lakeflow pipelines
- Databricks Declarative Automation Bundles
- Monitoring and operational readiness

------------------------------------------------------------------------------------

## Architecture

The platform follows a layered Medallion Architecture implemented with Databricks Lakeflow.

```text
Databricks Wanderbricks Data Product
                │
                ▼
          Source / Ingestion
                │
                ▼
             Bronze
        Raw source-aligned data
                │
                ▼
             Silver
     Validated and standardized data
                │
                ▼
              Gold
       Business-ready data products
                │
          ┌─────┴─────┐
          ▼           ▼
   Databricks SQL   Analytics


------------------------------------------------------------------------------------

## 2. Environment Strategy

```markdown
## Environment Strategy

The platform is designed with three deployment environments:

- DEV — active development and testing
- STAGE — pre-production validation
- PROD — production workloads

Environment-specific configuration is managed through Databricks Declarative Automation Bundles.

The current implementation uses Databricks Free Edition, which provides a single workspace. Therefore, environment isolation is initially implemented through deployment targets and environment-specific catalogs within the available workspace.

The project architecture is intentionally designed so that the same deployment model can later be promoted to separate Databricks workspaces when additional environments are available.

------------------------------------------------------------------------------------


## 3. Data Architecture

The platform uses a Medallion Architecture consisting of three primary layers.

### Bronze

The Bronze layer contains source-aligned data with minimal transformation.

Responsibilities:

- Source ingestion
- Schema preservation
- Ingestion metadata
- Initial technical validation
- Traceability to source data

### Silver

The Silver layer contains validated and standardized datasets.

Responsibilities:

- Data cleansing
- Schema enforcement
- Data quality validation
- Deduplication
- Referential integrity
- Standardization
- Business-independent transformations

### Gold

The Gold layer contains business-ready analytical datasets.

Responsibilities:

- Dimensional modeling
- Business transformations
- Aggregations
- Analytical metrics
- Data products for downstream consumption

------------------------------------------------------------------------------------

## 4.Source Data

The primary source is the Databricks Wanderbricks dataset provided through a Databricks data share.

The source contains entities related to a travel marketplace, including:

- Users
- Bookings
- Properties
- Hosts
- Cities
- Amenities
- Property amenities
- Property images
- Employees

The shared source data is treated as read-only. All transformations are performed within the platform's managed data layers.

------------------------------------------------------------------------------------

## 5. Data Model

The analytical model will be designed around the core business domains of the travel marketplace.

### Core domains

- Customer
- Property
- Host
- Booking
- Revenue

The Gold layer is expected to contain a combination of fact and dimension tables.

### Candidate fact tables

- `fact_bookings`
- `fact_revenue`

### Candidate dimension tables

- `dim_customer`
- `dim_property`
- `dim_host`
- `dim_city`
- `dim_amenity`
- `dim_date`

The final model will be defined after completing source data profiling and business-rule analysis.

------------------------------------------------------------------------------------

## 6. Data Quality

Data quality is treated as a first-class component of the platform.

Expected validation categories include:

- Completeness
- Uniqueness
- Referential integrity
- Validity
- Consistency
- Business rule validation
- Schema validation

Example booking rules include:

- `booking_id` must not be null
- `booking_id` must be unique
- `user_id` must reference an existing user
- `property_id` must reference an existing property
- `check_out` must not precede `check_in`
- `guests_count` must be greater than zero
- `total_amount` must not be negative
- `updated_at` must not precede `created_at`

Invalid records will be handled according to the severity of the quality rule, including quarantine, drop, or pipeline failure where appropriate.

------------------------------------------------------------------------------------


## 7. CI/CD

All application and data pipeline code is version-controlled in GitHub.

The target development lifecycle is:

```text
Feature Branch
      │
      ▼
Pull Request
      │
      ▼
Continuous Integration
      │
      ├── Code Quality
      ├── Unit Tests
      ├── SQL Validation
      └── Bundle Validation
      │
      ▼
     DEV
      │
      ▼
Integration Testing
      │
      ▼
    STAGE
      │
      ▼
Production Approval
      │
      ▼
     PROD

------------------------------------------------------------------------------------


## 8. Repository Structure

```markdown
## Repository Structure

```text
wander-data-platform/
│
├── .github/
│   └── workflows/
│
├── src/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── common/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── resources/
│
├── sql/
│
├── docs/
│   ├── architecture/
│   ├── data-model/
│   ├── data-contracts/
│   ├── decisions/
│   └── runbooks/
│
├── conf/
│
├── databricks.yml
├── pyproject.toml
├── README.md
└── .gitignore

------------------------------------------------------------------------------------


## 9. Technology Stack

```markdown
## Technology Stack

### Data Platform

- Databricks
- Lakeflow
- Unity Catalog
- Apache Spark
- PySpark
- Databricks SQL

### Development

- Python
- SQL
- Git
- GitHub

### CI/CD

- GitHub Actions
- Databricks Declarative Automation Bundles

### Testing and Quality

- pytest
- Python linting
- SQL validation
- Data quality expectations

### Governance and Security

- Unity Catalog
- Role-based access control
- Least-privilege principles
- Environment isolation

------------------------------------------------------------------------------------

## 10. Engineering Principles

The project follows the following engineering principles:

1. Everything possible should be version controlled.
2. Infrastructure and deployment configuration should be defined as code.
3. Production changes should go through pull requests.
4. Automated tests should run before deployment.
5. Data quality should be enforced as part of the pipeline.
6. Source data should remain immutable.
7. Production workloads should use least-privilege access.
8. Development, staging, and production concerns should remain isolated.
9. Pipelines should be observable and operationally supportable.
10. Deployments should be reproducible.

------------------------------------------------------------------------------------

## Project Status

🚧 **Active Development**

### Completed

- [x] Local development environment
- [x] Databricks CLI configuration
- [x] Databricks workspace authentication
- [x] Source data discovery
- [x] Medallion architecture
- [x] Bronze booking pipeline
- [x] Silver validation pipeline
- [x] Quarantine handling
- [x] Data quality expectations
- [x] Booking data contract
- [x] Gold daily booking metrics
- [x] Databricks Declarative Automation Bundle
- [x] DEV deployment
- [x] Unit tests
- [x] Databricks SQL analytics dashboard

### Planned

- [ ] GitHub Actions CI
- [ ] GitHub Actions CD
- [ ] STAGE deployment
- [ ] Production deployment
- [ ] Integration tests
- [ ] Monitoring and observability
- [ ] Additional source entities
- [ ] Expanded analytical data model
