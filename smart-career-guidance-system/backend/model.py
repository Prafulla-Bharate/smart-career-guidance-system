import joblib
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load serialized objects
model = joblib.load("backend/model.pkl")
label_encoder = joblib.load("backend/label_encoder.pkl")
scaler = joblib.load("backend/scaler.pkl")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Expected columns
categorical_cols = ["Degree", "Branch", "Gender"]
text_groupings = {
    "technical_profile": ["Skills", "Certifications", "Internship_Experience"],
    "interest_profile": ["Favorite_Subjects", "Interests"],
    "soft_profile": ["Soft_Skills", "Personality_Type", "Preferred_Work_Style"]
}
numeric_cols = ["Age", "CGPA"]

def preprocess_input(student_df: pd.DataFrame):
    df = student_df.copy()

    # Fill missing expected columns
    for col in categorical_cols:
        if col not in df.columns:
            df[col] = "Unknown"
    for group in text_groupings.values():
        for col in group:
            if col not in df.columns:
                df[col] = ""
    for col in numeric_cols:
        if col not in df.columns:
            df[col] = np.nan

    # Handle missing values
    df[categorical_cols] = df[categorical_cols].fillna("Unknown")
    for group in text_groupings.values():
        df[group] = df.get(group, "").fillna("")
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median(numeric_only=True))

    # Encode text groupings
    for new_col, group_cols in text_groupings.items():
        df[new_col] = df[group_cols].agg(" ".join, axis=1)

    # Apply sentence embeddings
    tech_emb = embedder.encode(df["technical_profile"].tolist())
    int_emb = embedder.encode(df["interest_profile"].tolist())
    soft_emb = embedder.encode(df["soft_profile"].tolist())

    tech_df = pd.DataFrame(tech_emb, columns=[f"tech_emb_{i}" for i in range(tech_emb.shape[1])])
    int_df = pd.DataFrame(int_emb, columns=[f"int_emb_{i}" for i in range(int_emb.shape[1])])
    soft_df = pd.DataFrame(soft_emb, columns=[f"soft_emb_{i}" for i in range(soft_emb.shape[1])])

    # Encode categorical
    df["Degree"] = pd.factorize(df["Degree"])[0]
    df["Branch"] = pd.factorize(df["Branch"])[0]
    df["Gender"] = pd.factorize(df["Gender"])[0]

    # Scale numerical
    numeric_scaled = pd.DataFrame(scaler.transform(df[numeric_cols]), columns=numeric_cols)

    # Final feature set
    final_input = pd.concat([
        df[["Degree", "Branch", "Gender"]],
        numeric_scaled,
        tech_df,
        int_df,
        soft_df
    ], axis=1)

    return final_input


def predict_top_3_careers(student_df: pd.DataFrame):
    X = preprocess_input(student_df)
    probs = model.predict_proba(X)[0]
    top3_idx = np.argsort(probs)[-3:][::-1]
    top3_labels = label_encoder.inverse_transform(top3_idx)
    top3_probs = probs[top3_idx]
    return list(zip(top3_labels, top3_probs))
