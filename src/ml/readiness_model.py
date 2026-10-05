from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "cgpa",
    "attendance_percentage",
    "project_count",
    "certification_count",
    "internship_count",
    "activity_count",
]


def load_student_data(path=None):
    """Load the fictional student dataset."""

    if path is None:
        path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "raw"
            / "students.csv"
        )

    return pd.read_csv(path)


def prepare_features(df):
    """Prepare numeric features for ML analysis."""

    missing = [
        column
        for column in FEATURE_COLUMNS
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required ML features: {missing}"
        )

    return df[FEATURE_COLUMNS].astype(float)


def calculate_readiness_profiles(df):
    """
    Group students into three data-driven readiness profiles.

    This is unsupervised profiling, not predictive career forecasting.
    """

    features = prepare_features(df)

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=20
    )

    clusters = model.fit_predict(scaled_features)

    result = df.copy()
    result["ml_cluster"] = clusters

    cluster_means = (
        result.groupby("ml_cluster")[FEATURE_COLUMNS]
        .mean()
    )

    cluster_scores = cluster_means.mean(axis=1)

    ordered_clusters = cluster_scores.sort_values().index.tolist()

    profile_mapping = {
        ordered_clusters[0]: "Developing",
        ordered_clusters[1]: "Emerging",
        ordered_clusters[2]: "Ready",
    }

    result["ml_readiness_profile"] = result["ml_cluster"].map(
        profile_mapping
    )

    return result


def analyze_student(student_id, df=None):
    """Return the ML readiness profile for one student."""

    if df is None:
        df = load_student_data()

    result = calculate_readiness_profiles(df)

    student = result[
        result["student_id"].astype(str) == str(student_id)
    ]

    if student.empty:
        raise ValueError(
            f"Student not found: {student_id}"
        )

    row = student.iloc[0]

    return {
        "student_id": str(row["student_id"]),
        "ml_cluster": int(row["ml_cluster"]),
        "ml_readiness_profile": str(
            row["ml_readiness_profile"]
        ),
    }


if __name__ == "__main__":
    df = load_student_data()

    result = calculate_readiness_profiles(df)

    output_path = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "processed"
        / "ml_readiness_profiles.csv"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    result.to_csv(
        output_path,
        index=False
    )

    print(
        f"ML readiness profiles written to: {output_path}"
    )