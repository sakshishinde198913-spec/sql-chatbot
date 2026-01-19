📊 𝗔𝗜-𝗔𝘀𝘀𝗶𝘀𝘁𝗲𝗱 𝗦𝗤𝗟 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗖𝗵𝗮𝘁 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁

𝗢𝘃𝗲𝗿𝘃𝗶𝗲𝘄
This project is an AI-assisted SQL chat application that allows users to interact with a relational database using plain English instead of writing SQL manually.

The core idea is simple:
make database querying accessible to non-technical users without hiding SQL itself.

Every user question is converted into a real SQL query, executed on a MySQL database, and the results are returned in a readable format with optional visualizations. The project focuses on practical SQL usage, backed by AI — not AI replacing SQL.

𝗧𝗵𝗶𝘀 𝗽𝗿𝗼𝗷𝗲𝗰𝘁 𝗱𝗲𝗺𝗼𝗻𝘀𝘁𝗿𝗮𝘁𝗲𝘀 𝗵𝗮𝗻𝗱𝘀-𝗼𝗻 𝘄𝗼𝗿𝗸 𝘄𝗶𝘁𝗵:
  • SQL and relational databases
  • Backend development using Python and Flask
  • natural language to SQL conversion
  • Data analysis and visualization

𝗪𝗵𝗮𝘁 𝘁𝗵𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗗𝗼𝗲𝘀
  1. The system allows users to:
  2. Ask questions in plain English
  3. Automatically generate valid SQL SELECT queries
  4. Execute those queries on a MySQL database
  5. View results as structured tables
  6. Generate charts such as bar graphs, pie charts, line plots, and histograms when requested
  7. The emphasis is not just on AI responses, but on how AI drives SQL-based data analysis.

𝗛𝗼𝘄 𝗜𝘁 𝗪𝗼𝗿𝗸𝘀 (𝗛𝗶𝗴𝗵-𝗟𝗲𝘃𝗲𝗹 𝗙𝗹𝗼𝘄)
  • The user enters a question in natural language.
  • The backend sends the question to an LLM configured specifically for SQL generation.
  • The model generates a SQL query based on the database schema.
  • The query is executed using SQLAlchemy.
  • Results are loaded into a Pandas DataFrame.

𝗧𝗵𝗲 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲 𝗿𝗲𝘁𝘂𝗿𝗻𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝘂𝘀𝗲𝗿 𝗶𝗻𝗰𝗹𝘂𝗱𝗲𝘀:
The generated SQL query
A short, human-readable summary
A table of results
A chart (if the question requests visualization)

Example
User Question
𝘚𝘩𝘰𝘸 𝘵𝘰𝘵𝘢𝘭 𝘥𝘰𝘯𝘢𝘵𝘪𝘰𝘯𝘴 𝘣𝘺 𝘴𝘵𝘢𝘵𝘦 𝘢𝘴 𝘢 𝘱𝘪𝘦 𝘤𝘩𝘢𝘳𝘵
Generated SQL
𝘚𝘌𝘓𝘌𝘊𝘛 𝘴𝘵𝘢𝘵𝘦, 𝘚𝘜𝘔(𝘢𝘮𝘰𝘶𝘯𝘵) 𝘈𝘚 𝘵𝘰𝘵𝘢𝘭_𝘥𝘰𝘯𝘢𝘵𝘪𝘰𝘯𝘴
𝘍𝘙𝘖𝘔 𝘥𝘰𝘯𝘢𝘵𝘪𝘰𝘯𝘴
𝘎𝘙𝘖𝘜𝘗 𝘉𝘠 𝘴𝘵𝘢𝘵𝘦;

Output
𝘈 𝘵𝘢𝘣𝘭𝘦 𝘴𝘩𝘰𝘸𝘪𝘯𝘨 𝘴𝘵𝘢𝘵𝘦𝘴 𝘢𝘯𝘥 𝘵𝘰𝘵𝘢𝘭 𝘥𝘰𝘯𝘢𝘵𝘪𝘰𝘯 𝘢𝘮𝘰𝘶𝘯𝘵𝘴
𝘈 𝘱𝘪𝘦 𝘤𝘩𝘢𝘳𝘵 𝘷𝘪𝘴𝘶𝘢𝘭𝘪𝘻𝘪𝘯𝘨 𝘤𝘰𝘯𝘵𝘳𝘪𝘣𝘶𝘵𝘪𝘰𝘯 𝘥𝘪𝘴𝘵𝘳𝘪𝘣𝘶𝘵𝘪𝘰𝘯
𝘈 𝘴𝘩𝘰𝘳𝘵 𝘦𝘹𝘱𝘭𝘢𝘯𝘢𝘵𝘪𝘰𝘯 𝘰𝘧 𝘸𝘩𝘢𝘵 𝘵𝘩𝘦 𝘲𝘶𝘦𝘳𝘺 𝘳𝘦𝘱𝘳𝘦𝘴𝘦𝘯𝘵𝘴

SQL Focus of the Project
  • Although the interface is conversational, the system is strongly SQL-driven.
  • The project uses real SQL concepts including:
  • SELECT queries
  • GROUP BY and ORDER BY
  • Aggregation functions (SUM, COUNT, AVG)
  • Filtering and data summarization

Every answer shown to the user is backed by an actual SQL query executed on the database, making this project especially relevant for:



𝗧𝗲𝗰𝗵 𝗦𝘁𝗮𝗰𝗸
𝙱̲𝚊̲𝚌̲𝚔̲𝚎̲𝚗̲𝚍̲
Python
Flask
SQLAlchemy
PyMySQL
Pandas
𝙳̲𝚊̲𝚝̲𝚊̲𝚋̲𝚊̲𝚜̲𝚎̲
MySQL
AI / NLP
LangChain (SQLDatabase utilities)
OpenRouter LLM API
Natural language to SQL generation
Visualization
Matplotlib
Plotly (conceptual support)

Frontend
HTML
CSS
JavaScript (Fetch API)

𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗗𝗶𝗿𝗲𝗰𝘁𝗼𝗿𝘆 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲
𝗦𝗤𝗟-𝗖𝗛𝗔𝗧𝗕𝗢𝗧/
│
├── app.py                  # Main Flask application entry point
├── requirements.txt        # Python dependencies
├── render.yaml             # Deployment configuration (Render)
├── .env                    # Environment variables (not committed)
├── .gitignore              # Git ignore rules
│
├── templates/
│   └── index.html          # Frontend chat UI
│
├── static/
│   └── charts/             # Generated chart images
│
├── utils/
│   ├── db.py               # Database connection & SQLAlchemy setup
│   ├── llm.py              # LLM / OpenRouter configuration
│   ├── sql_generator.py    # Natural language → SQL generation
│   ├── sql_agent.py        # LangChain SQL agent logic
│   ├── charts.py           # Chart generation utilities
│   └── answer_formatter.py # Formats results into readable responses
│
├── data/
│   ├── donation_data.csv   # Sample dataset
│   └── csv_to_sql.py       # Script to load CSV data into MySQL
│
└── README.md               # Project documentation

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
