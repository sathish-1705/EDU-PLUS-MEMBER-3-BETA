import pandas as pd
from src.analysis.performance_analysis import analyze


def test_baseline_levels_are_deterministic():
    df = pd.DataFrame([
        {'cgpa':8.0,'attendance_percentage':80,'project_count':1,'internship_count':0,'certification_count':1,'activity_count':1},
        {'cgpa':6.5,'attendance_percentage':60,'project_count':0,'internship_count':0,'certification_count':0,'activity_count':0}
    ])
    result = analyze(df)
    assert list(result['evidence_level']) == ['strong', 'limited']
    assert list(result['evidence_count']) == [3, 0]
