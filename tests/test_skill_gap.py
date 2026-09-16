from src.skills.skill_gap import skill_gap


def test_full_match_has_no_gap():
    result = skill_gap(['Python','SQL','Pandas','Power BI','Git'], 'Data Analyst')
    assert result['missing_skills'] == []
    assert result['priority'] == 'low'


def test_missing_skills_are_reported():
    result = skill_gap(['Python','SQL'], 'Data Analyst')
    assert 'Pandas' in result['missing_skills']
    assert 'Power BI' in result['missing_skills']
    assert result['priority'] == 'high'


def test_case_and_whitespace_do_not_create_false_gaps():
    result = skill_gap([' python ', 'SQL', 'PANDAS', 'Power BI', 'git'], 'Data Analyst')
    assert result['missing_skills'] == []
