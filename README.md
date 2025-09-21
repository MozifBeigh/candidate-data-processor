# candidate-data-processor
Candidate Data Processor – AI-assisted pipeline for cleaning candidate data, deduplicating records, and generating SQL update scripts.


## 📌 Project Overview
The Candidate Data Processor is a Python-based pipeline that:
1. Reads candidate records from a CSV file.
2. Cleans and sanitizes names (removes unwanted tokens like MBA, PMP, ®, commas, etc.).
3. Deduplicates candidates based on email.
4. Generates SQL update scripts for Oracle HCM migration.


This project demonstrates how AI coding agents can accelerate development by handling boilerplate, refactoring, and debugging.


---


## 🚀 How to Run


1. Clone the repository:
```bash
git clone https://github.com/MozifBeigh/candidate-data-processor.git
cd candidate-data-processor
```


2. Add a CSV file named `input_candidates.csv` in the project root. Example:
```csv
CandidateNumber,FirstName,LastName,Email,City,State,Country
CAND001,Vin|Luyen , MBA/PMP/Lean Sigma,Luyen@example.com,Mumbai,Maharashtra,India
CAND002,Afsaneh|Mansouri, PMP®,mansouri@example.com,Tehran,Tehran,Iran
CAND003,John,Doe,john.doe@example.com,New York,NY,USA
```


3. Run the processor:
```bash
python main.py
```


4. The script will generate an `updates.sql` file with clean SQL update statements.


---


## 📂 Project Structure
```
candidate-data-processor/
│── main.py # Core pipeline logic
│── input_candidates.csv # Input file (sample provided)
│── updates.sql # Generated SQL updates
│── README.md # Documentation
```


---


## 🧠 Role of AI Code Agents
- **GitHub Copilot**: Used to scaffold CSV parsing methods and boilerplate functions.
- **Cursor AI**: Helped with refactoring and debugging encoding issues.
- **Claude Code**: Assisted in summarizing and reasoning about dependencies across files.


Together, these tools reduced development effort by **30–40%**, mainly by accelerating test generation, error handling, and refactoring.


---


## 📜 License
This project is open-source for demonstration purposes. You are free to fork and extend it.
