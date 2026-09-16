from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = [
    'student_id','name','program','cgpa','attendance_percentage','skills','project_count',
    'certification_count','internship_count','technical_indicator_count',
    'communication_indicator','activity_count','career_goal'
]
NUMERIC_COLUMNS = [
    'cgpa','attendance_percentage','project_count','certification_count',
    'internship_count','technical_indicator_count','communication_indicator','activity_count'
]

def normalize_skills(value):
    if pd.isna(value):
        return ''
    skills = sorted({s.strip() for s in str(value).split(';') if s.strip()}, key=str.lower)
    return ';'.join(skills)

def validate_and_clean(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f'Missing required columns: {missing}')
    out = df[REQUIRED_COLUMNS].copy()
    if out['student_id'].duplicated().any():
        raise ValueError('Duplicate student_id values found')
    for col in NUMERIC_COLUMNS:
        out[col] = pd.to_numeric(out[col], errors='raise')
    if not out['cgpa'].between(0, 10).all():
        raise ValueError('CGPA must be between 0 and 10')
    if not out['attendance_percentage'].between(0, 100).all():
        raise ValueError('Attendance must be between 0 and 100')
    for col in NUMERIC_COLUMNS[2:]:
        if (out[col] < 0).any():
            raise ValueError(f'{col} cannot be negative')
    if out[REQUIRED_COLUMNS].isna().any().any():
        raise ValueError('Missing values found in required fields')
    out['skills'] = out['skills'].map(normalize_skills)
    out['skill_count'] = out['skills'].map(lambda x: 0 if not x else len(x.split(';')))
    return out

def preprocess_file(input_path, output_path):
    df = pd.read_csv(input_path)
    cleaned = validate_and_clean(df)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(output_path, index=False)
    return cleaned

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    preprocess_file(root/'data/raw/students.csv', root/'data/processed/students_features.csv')
    print('Preprocessing completed.')
