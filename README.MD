# Campus Fee Risk Analysis System

A backend data-driven system designed to analyze student fee payment records, assess financial risk levels, and generate structured intervention recommendations.

This system focuses on ethical, non-harassing financial planning support for educational institutions.

---

## Overview

Educational institutions often face delayed fee payments, leading to administrative complexity and increased student stress.

This system provides a structured, rule-based risk assessment model that:

- Calculates pending fee balances
- Classifies students into financial risk categories
- Generates responsible and ethical payment plan suggestions
- Stores and manages structured fee records using MySQL

The architecture is designed to be modular, scalable, and extendable for future ML-based prediction models.

---

## System Architecture

The project follows a layered backend structure:

1. Data Layer (MySQL)
   - Stores student profiles
   - Stores fee payment records
   - Maintains calculated risk categories

2. Business Logic Layer (Python Risk Engine)
   - Computes outstanding balances
   - Applies rule-based classification logic
   - Assigns risk level (Low / Medium / High)

3. Recommendation Layer
   - Generates structured payment plan suggestions
   - Ensures ethical, non-harassing communication principles

---

## Database Design

Example Tables:

### students
- student_id (Primary Key)
- name
- department
- year

### fee_records
- record_id (Primary Key)
- student_id (Foreign Key)
- total_fee
- amount_paid
- due_date

### risk_status
- student_id (Foreign Key)
- pending_amount
- risk_level
- recommendation

The schema is normalized to avoid redundancy and maintain data integrity.

---

## Risk Classification Logic

Risk level is determined based on:

- Percentage of fee unpaid
- Delay duration
- Historical payment consistency

Example logic:

- Low Risk → Minor delay, low pending percentage
- Medium Risk → Moderate delay or mid-level pending amount
- High Risk → Large unpaid amount or long overdue duration

The classification system is rule-based but structured in a way that can be replaced by ML models in future versions.

---

## Features

- Rule-based financial risk scoring
- SQL-Python integration
- Structured database schema
- Ethical recommendation engine
- Modular backend structure

---

## Future Improvements

- Machine Learning–based risk prediction
- Automated email/SMS reminders
- Admin dashboard
- Student self-service dashboard
- Data visualization of payment trends

---

## Tech Stack

- Python
- MySQL
- SQL
- VS Code

---

## Security

- Database credentials are securely managed and not exposed.
- Designed with separation between logic and configuration.

---

## Author

Neha Mhatre  
Backend & Data Systems Enthusiast  
Focused on building structured, scalable decision systems.
