# Week 1 Data Analysis Notebook Record

This markdown companion records the reproducible exploration steps. Run the Python scripts from the repository root after installing `requirements.txt`.

```python
import pandas as pd

df = pd.read_csv('data/raw/students.csv')
df.info()
df.isna().sum()
df.duplicated().sum()
df.describe(numeric_only=True)
```

Key checks:
- 20 fictional student records are present.
- Required academic, experience and skill fields are represented.
- Numeric ranges are validated by `src/preprocessing/preprocess.py`.
- Skills are normalized before analysis.
- Baseline readiness is evidence-based and deterministic, not a predictive model.

Run:

```bash
python src/preprocessing/preprocess.py
python src/analysis/performance_analysis.py
pytest -q
```
