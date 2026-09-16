from pathlib import Path
import pandas as pd


def baseline_evidence(row):
    academic = row['cgpa'] >= 7.5 and row['attendance_percentage'] >= 75
    experience = row['project_count'] >= 1 or row['internship_count'] >= 1
    development = row['certification_count'] >= 1 or row['activity_count'] >= 1
    count = sum([academic, experience, development])
    level = 'strong' if count == 3 else 'developing' if count == 2 else 'limited'
    return pd.Series({'evidence_count': count, 'evidence_level': level,
                      'academic_evidence': academic, 'experience_evidence': experience,
                      'development_evidence': development})


def analyze(df):
    out = df.copy()
    evidence = out.apply(baseline_evidence, axis=1)
    return pd.concat([out, evidence], axis=1)


def summarize(df):
    return {
        'student_count': int(len(df)),
        'mean_cgpa': round(float(df['cgpa'].mean()), 2),
        'mean_attendance': round(float(df['attendance_percentage'].mean()), 2),
        'evidence_levels': df['evidence_level'].value_counts().to_dict(),
    }

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    df = pd.read_csv(root/'data/processed/students_features.csv')
    result = analyze(df)
    result.to_csv(root/'data/processed/student_analysis.csv', index=False)
    import json
    (root/'data/processed/performance_summary.json').write_text(json.dumps(summarize(result), indent=2))
    print(summarize(result))
