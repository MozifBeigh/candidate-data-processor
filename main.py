import csv
from typing import List


class Candidate:
def __init__(self, candidate_number: str, first_name: str, last_name: str, email: str, city: str, state: str, country: str):
self.candidate_number = candidate_number
self.first_name = Candidate.clean_name(first_name)
self.last_name = Candidate.clean_name(last_name)
self.email = email.strip().lower()
self.city = city
self.state = state
self.country = country


@staticmethod
def clean_name(name: str) -> str:
unwanted = ["MBA", "PMP", "®", ",", "|"]
for token in unwanted:
name = name.replace(token, "")
return name.strip()


def to_sql_update(self) -> str:
return f"""
UPDATE oalhcm.oalhcm_orc_cre_cand_profile
SET first_name='{self.first_name}', last_name='{self.last_name}', city='{self.city}',
orcl_candidate_state_name='{self.state}', orcl_candidate_country_name='{self.country}'
WHERE candidate_number='{self.candidate_number}';
""".strip()


class CandidateDataProcessor:
def __init__(self, input_csv: str, output_sql: str):
self.input_csv = input_csv
self.output_sql = output_sql
self.candidates: List[Candidate] = []


def load_candidates(self):
with open(self.input_csv, mode="r", encoding="utf-8") as f:
reader = csv.DictReader(f)
for row in reader:
candidate = Candidate(
candidate_number=row.get("CandidateNumber", "").strip(),
first_name=row.get("FirstName", "").strip(),
last_name=row.get("LastName", "").strip(),
email=row.get("Email", "").strip(),
city=row.get("City", "").strip(),
state=row.get("State", "").strip(),
country=row.get("Country", "").strip()
)
self.candidates.append(candidate)


def remove_duplicates(self):
seen = set()
unique = []
for c in self.candidates:
if c.email not in seen:
seen.add(c.email)
unique.append(c)
self.candidates = unique


def export_sql(self):
with open(self.output_sql, mode="w", encoding="utf-8") as f:
for c in self.candidates:
f.write(c.to_sql_update() + "\n")


if __name__ == "__main__":
processor = CandidateDataProcessor("input_candidates.csv", "updates.sql")
processor.load_candidates()
processor.remove_duplicates()
processor.export_sql()
print(f"Processed {len(processor.candidates)} unique candidates. SQL written to updates.sql")
