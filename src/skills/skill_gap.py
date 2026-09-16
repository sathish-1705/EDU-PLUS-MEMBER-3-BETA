import json
from pathlib import Path

RECOMMENDATIONS = {
    'Python': 'Complete Python practice and build a small data or automation project.',
    'SQL': 'Practice SQL queries and database exercises using progressively harder datasets.',
    'Pandas': 'Work through Pandas exercises and build a small data-cleaning project.',
    'Power BI': 'Create a dashboard project using a public or fictional dataset.',
    'Git': 'Practice branching, commits, pull requests and conflict resolution.',
    'Java': 'Build a small Java application covering core OOP concepts.',
    'Spring': 'Build a small Spring REST service and document its endpoints.',
    'HTML': 'Build a responsive multi-page HTML interface.',
    'CSS': 'Practice responsive layouts and component styling.',
    'JavaScript': 'Build an interactive browser project using JavaScript.',
    'React': 'Create a small React application with reusable components.',
    'Node.js': 'Build a small Node.js API and connect it to a database.',
    'NumPy': 'Complete numerical computing exercises with NumPy.',
    'scikit-learn': 'Build a small supervised-learning experiment and document evaluation.',
    'C': 'Practice C programming with small systems-oriented exercises.',
    'C++': 'Build a small C++ project using classes and standard library features.',
    'Embedded C': 'Practice embedded C concepts with a simulated or supervised lab project.',
    'Arduino': 'Build a simple Arduino prototype with documented code and testing.'
}


def load_taxonomy(path=None):
    path = path or Path(__file__).resolve().parents[2] / 'data/skill_taxonomy.json'
    return json.loads(Path(path).read_text())


def skill_gap(student_skills, target_role, taxonomy=None):
    taxonomy = taxonomy or load_taxonomy()
    required = taxonomy[target_role]
    current = {s.strip().lower() for s in student_skills if s and s.strip()}
    missing = [s for s in required if s.lower() not in current]
    n = len(missing)
    priority = 'low' if n == 0 else 'medium' if n <= 2 else 'high'
    return {
        'target_role': target_role,
        'required_skills': required,
        'matched_skills': [s for s in required if s.lower() in current],
        'missing_skills': missing,
        'priority': priority,
        'recommendations': [RECOMMENDATIONS[s] for s in missing]
    }
