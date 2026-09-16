import pandas as pd
import pytest
from src.preprocessing.preprocess import validate_and_clean


def sample():
    return pd.DataFrame([{
        'student_id':'T1','name':'Test','program':'CSE','cgpa':8.0,
        'attendance_percentage':80,'skills':'Python; SQL; Python','project_count':1,
        'certification_count':1,'internship_count':0,'technical_indicator_count':2,
        'communication_indicator':3,'activity_count':1,'career_goal':'Data Analyst'
    }])


def test_clean_normalizes_skills():
    out = validate_and_clean(sample())
    assert out.loc[0,'skills'] == 'Python;SQL'
    assert out.loc[0,'skill_count'] == 2


def test_duplicate_ids_rejected():
    df = pd.concat([sample(), sample()], ignore_index=True)
    with pytest.raises(ValueError, match='Duplicate'):
        validate_and_clean(df)


def test_invalid_cgpa_rejected():
    df = sample(); df.loc[0,'cgpa'] = 11
    with pytest.raises(ValueError, match='CGPA'):
        validate_and_clean(df)
