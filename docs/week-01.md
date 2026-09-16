# Week 1 — Dataset & Feature Foundation

## Completed
- Created a clean fictional student dataset with 20 records.
- Defined academic, experience, technical, communication and activity fields.
- Added reproducible preprocessing validation.
- Normalized skill strings and derived `skill_count`.
- Defined the career-readiness output as an explainable evidence level rather than a rushed predictive model.

## Baseline target definition
Evidence is based on three documented groups:
1. Academic evidence: CGPA >= 7.5 and attendance >= 75%.
2. Experience evidence: at least one project or internship.
3. Development evidence: at least one certification or relevant activity.

Three groups satisfied = strong; two = developing; zero or one = limited.

## Backend requirements
Member 2 should expose the fields listed in `docs/data_dictionary.md`. Prototype-only fields must be reconciled with the final Supabase schema.

## Testing
Dataset structure, numeric ranges, missing values, duplicate IDs and skill normalization are covered by tests.
