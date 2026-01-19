# 📊 AI-Assisted SQL Database Chat Assistant

## Overview

This project is an **AI-assisted SQL chat application** that allows users to interact with a relational database using **plain English instead of writing SQL manually**.

The core idea is simple:  
**make database querying accessible to non-technical users without hiding SQL itself.**

Every user question is converted into a **real SQL query**, executed on a **MySQL database**, and the results are returned in a readable format with optional visualizations.  
The project focuses on **practical SQL usage backed by AI**, not AI replacing SQL.

---

## What This Project Demonstrates

This project shows hands-on work with:

- SQL and relational databases  
- Backend development using Python and Flask  
- Natural language → SQL conversion  
- Data analysis and visualization  

---

## What the Project Does

The system allows users to:

1. Ask questions in plain English  
2. Automatically generate valid **SQL SELECT queries**  
3. Execute those queries on a **MySQL database**  
4. View results as structured tables  
5. Generate charts such as:
   - Bar graphs  
   - Pie charts  
   - Line plots  
   - Histograms  

The emphasis is not just on AI responses, but on **how AI drives SQL-based data analysis**.

---

## How It Works (High-Level Flow)

1. The user enters a question in natural language  
2. The backend sends the question to an LLM configured for SQL generation  
3. The model generates a SQL query based on the database schema  
4. The query is executed using SQLAlchemy  
5. Results are loaded into a Pandas DataFrame  

### The response returned to the user includes:

- The generated SQL query  
- A short, human-readable summary  
- A table of results  
- A chart (if visualization is requested)

---

## Example

**User Question**



<img width="1833" height="925" alt="image" src="https://github.com/user-attachments/assets/708d0258-e729-4fc0-b1a5-73c6b2588f96" />
<img width="1714" height="956" alt="image" src="https://github.com/user-attachments/assets/94b9c099-a435-460c-948d-f365e4212b91" />
<img width="982" height="852" alt="image" src="https://github.com/user-attachments/assets/1414afba-c902-43a9-bb62-51b9ccd1a9cb" />
<img width="775" height="804" alt="image" src="https://github.com/user-attachments/assets/8ffa5f8e-8ea5-4b80-9eb7-bfaae8f1a21b" />


Why This Project Is Useful

Shows real SQL usage, not mock data

Demonstrates how AI can be used practically with databases

Makes data accessible to non-technical users

Combines backend, SQL, and data visualization in one project

Easy to explain in interviews and easy to extend

Possible Improvements

Support for multiple databases (PostgreSQL, SQLite)

User authentication

Query history and exports

Better SQL explanations for learning purposes

Deployment on a cloud platform

Author

Sakshi Gopal Shinde
Computer Engineering Student

Satara, Maharashtra
Email: sakshishinde0808@gmail.com

LinkedIn: https://tinyurl.com/ykhnd9d7
