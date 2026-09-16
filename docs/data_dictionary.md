# EDU PLUS Member 3 — Data Dictionary

Prototype dataset is fictional and contains no real student data.

| Field | Type | Meaning |
|---|---|---|
| student_id | string | Stable fictional student identifier |
| name | string | Fictional display name |
| program | string | Academic program |
| cgpa | float | CGPA on a 0–10 scale |
| attendance_percentage | float | Attendance percentage, 0–100 |
| skills | semicolon-separated string | Current self/recorded skills |
| project_count | integer | Completed project count |
| certification_count | integer | Relevant certification count |
| internship_count | integer | Internship count |
| technical_indicator_count | integer | Prototype count of technical indicators |
| communication_indicator | integer | Prototype communication indicator |
| activity_count | integer | Relevant academic/extracurricular activity count |
| career_goal | string | Target role used by the prototype taxonomy |
| skill_count | integer | Derived number of normalized skills |

`technical_indicator_count` and `communication_indicator` are prototype fields. Member 3 must align their names and semantics with Member 2's final Supabase schema before integration. Do not create a competing backend schema.
