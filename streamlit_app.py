import streamlit as st

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(99,102,241,.18), transparent 32%),
        radial-gradient(circle at 90% 80%, rgba(6,182,212,.12), transparent 32%),
        #07111f;
    color: #f8fafc;
}

.block-container {
    max-width: 1150px;
    padding-top: 10px;
}

/* NAVBAR */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 0 28px;
    border-bottom: 1px solid rgba(255,255,255,.07);
    margin-bottom: 55px;
}

.logo {
    display: flex;
    align-items: center;
    gap: 10px;
    color: white;
    font-size: 20px;
    font-weight: 700;
}

.logo-icon {
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    background: linear-gradient(135deg,#6366f1,#06b6d4);
}

.online {
    display: flex;
    align-items: center;
    gap: 7px;
    padding: 8px 14px;
    border: 1px solid rgba(34,197,94,.35);
    border-radius: 25px;
    color: #4ade80;
    background: rgba(34,197,94,.08);
    font-size: 13px;
}

/* HERO */

.badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 25px;
    border: 1px solid rgba(139,92,246,.4);
    background: rgba(139,92,246,.1);
    color: #c4b5fd;
    font-size: 13px;
}

.hero-title {
    font-size: 54px;
    line-height: 1.08;
    font-weight: 800;
    letter-spacing: -2px;
    color: white;
    margin: 28px 0 20px;
}

.gradient {
    background: linear-gradient(90deg,#a78bfa,#60a5fa,#22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-text {
    color: #94a3b8;
    font-size: 16px;
    line-height: 1.8;
    max-width: 650px;
}

/* DASHBOARD CARD */

.dashboard {
    padding: 28px;
    border-radius: 20px;
    background: rgba(15,27,46,.82);
    border: 1px solid rgba(148,163,184,.14);
    box-shadow: 0 25px 60px rgba(0,0,0,.25);
}

.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.dashboard-label {
    color: #94a3b8;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}

.live {
    color: #4ade80;
    font-size: 12px;
}

.preview {
    margin-top: 25px;
    padding: 22px;
    border-radius: 14px;
    background: rgba(255,255,255,.035);
}

.preview-label {
    color: #64748b;
    font-size: 12px;
}

.score {
    color: white;
    font-size: 44px;
    font-weight: 800;
    margin-top: 5px;
}

.preview-text {
    color: #64748b;
    font-size: 12px;
}

.bar {
    width: 100%;
    height: 7px;
    margin-top: 18px;
    border-radius: 10px;
    background: #1e293b;
    overflow: hidden;
}

.bar-fill {
    width: 64.25%;
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg,#8b5cf6,#22d3ee);
}

.stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 15px;
}

.stat {
    padding: 14px;
    border-radius: 10px;
    background: rgba(255,255,255,.035);
}

.stat-label {
    color: #64748b;
    font-size: 10px;
    display: block;
    margin-bottom: 5px;
}

.stat-value {
    color: #e2e8f0;
    font-size: 13px;
    font-weight: 600;
}

/* FEATURES */

.section-heading {
    margin-top: 70px;
    margin-bottom: 25px;
}

.section-heading small {
    color: #818cf8;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 11px;
    font-weight: 700;
}

.section-heading h2 {
    color: white;
    font-size: 29px;
    margin-top: 7px;
}

.feature {
    padding: 25px;
    min-height: 175px;
    border-radius: 16px;
    background: rgba(15,27,46,.65);
    border: 1px solid rgba(255,255,255,.07);
}

.feature-icon {
    font-size: 25px;
    margin-bottom: 15px;
}

.feature h3 {
    color: white;
    font-size: 16px;
}

.feature p {
    color: #64748b;
    font-size: 13px;
    line-height: 1.6;
}

/* BUTTON */

div.stButton > button {
    border-radius: 10px;
    border: 1px solid rgba(129,140,248,.35);
    background: linear-gradient(135deg,#6366f1,#4f46e5);
    color: white;
    font-weight: 600;
    padding: 11px 20px;
}

div.stButton > button:hover {
    color: white;
    border-color: #818cf8;
}

/* PREDICTION PAGE */

.prediction-heading {
    text-align: center;
    margin: 35px 0;
}

.prediction-heading h1 {
    color: white;
    font-size: 38px;
    margin: 15px 0 8px;
}

.prediction-heading p {
    color: #64748b;
    font-size: 14px;
}

.form-card {
    padding: 32px;
    border-radius: 20px;
    background: rgba(15,27,46,.78);
    border: 1px solid rgba(255,255,255,.08);
}

.form-title {
    color: white;
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 25px;
}

/* INPUTS */

.stSelectbox label,
.stNumberInput label {
    color: #cbd5e1 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] > div {
    background: #0b1728 !important;
    border-color: #26364d !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

div[data-testid="stNumberInput"] input {
    background: #0b1728 !important;
    border-color: #26364d !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

/* RESULT */

.result {
    margin-top: 30px;
    padding: 30px;
    text-align: center;
    border-radius: 18px;
    background: rgba(34,197,94,.06);
    border: 1px solid rgba(34,197,94,.2);
}

.result-label {
    color: #64748b;
    font-size: 12px;
}

.result-score {
    font-size: 55px;
    font-weight: 800;
    background: linear-gradient(90deg,#4ade80,#22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.result-text {
    color: #64748b;
    font-size: 12px;
}

.result-bar {
    max-width: 450px;
    height: 8px;
    margin: 20px auto 0;
    background: #1e293b;
    border-radius: 10px;
    overflow: hidden;
}

.result-fill {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg,#6366f1,#22d3ee);
}

/* FOOTER */

.footer {
    text-align: center;
    color: #475569;
    font-size: 12px;
    padding: 30px 0 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# =========================================================
# HOME / LANDING PAGE
# =========================================================

if st.session_state.page == "home":

    # NAVBAR
    st.html("""
    <div class="navbar">
        <div class="logo">
            <div class="logo-icon">🧠</div>
            Student Performance AI
        </div>

        <div class="online">
            ● Model Online
        </div>
    </div>
    """)

    left, right = st.columns([1.25, 0.9], gap="large")

    # LEFT SIDE
    with left:

        st.html("""
        <div class="badge">
            ✦ MACHINE LEARNING PREDICTION SYSTEM
        </div>

        <div class="hero-title">
            Predict Student<br>
            <span class="gradient">
                Performance
            </span>
        </div>

        <div class="hero-text">
            An intelligent machine learning application that predicts
            Mathematics scores using demographic, academic and
            test-preparation information.
        </div>
        """)

        st.write("")

        if st.button(
            "🚀  Start Prediction →",
            key="start_prediction"
        ):
            st.session_state.page = "prediction"
            st.rerun()

    # RIGHT SIDE
    with right:

        st.html("""
        <div class="dashboard">

            <div class="dashboard-header">

                <div class="dashboard-label">
                    MODEL DASHBOARD
                </div>

                <div class="live">
                    ● LIVE
                </div>

            </div>

            <div class="preview">

                <div class="preview-label">
                    Example Mathematics Score
                </div>

                <div class="score">
                    64.25
                </div>

                <div class="preview-text">
                    Example prediction
                </div>

                <div class="bar">
                    <div class="bar-fill"></div>
                </div>

            </div>

            <div class="stats">

                <div class="stat">
                    <span class="stat-label">MODEL</span>
                    <span class="stat-value">Linear Regression</span>
                </div>

                <div class="stat">
                    <span class="stat-label">PIPELINE</span>
                    <span class="stat-value">Preprocessed</span>
                </div>

                <div class="stat">
                    <span class="stat-label">INPUTS</span>
                    <span class="stat-value">7 Features</span>
                </div>

                <div class="stat">
                    <span class="stat-label">OUTPUT</span>
                    <span class="stat-value">Math Score</span>
                </div>

            </div>

        </div>
        """)

    # HOW IT WORKS
    st.html("""
    <div class="section-heading">
        <small>How it works</small>
        <h2>From student data to prediction</h2>
    </div>
    """)

    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        st.html("""
        <div class="feature">
            <div class="feature-icon">📋</div>
            <h3>Student Data</h3>
            <p>
                Enter demographic, academic and
                test-preparation information.
            </p>
        </div>
        """)

    with c2:
        st.html("""
        <div class="feature">
            <div class="feature-icon">⚙️</div>
            <h3>ML Pipeline</h3>
            <p>
                The information passes through the
                trained preprocessing and ML pipeline.
            </p>
        </div>
        """)

    with c3:
        st.html("""
        <div class="feature">
            <div class="feature-icon">🎯</div>
            <h3>Prediction</h3>
            <p>
                The trained model generates the predicted
                Mathematics score.
            </p>
        </div>
        """)

    st.html("""
    <div class="footer">
        Student Performance AI • Machine Learning Project
    </div>
    """)


# =========================================================
# PREDICTION PAGE
# =========================================================

else:

    # NAVBAR
    st.html("""
    <div class="navbar">

        <div class="logo">
            <div class="logo-icon">🧠</div>
            Student Performance AI
        </div>

        <div class="online">
            ● Model Online
        </div>

    </div>
    """)

    # BACK BUTTON
    if st.button(
        "← Back to Dashboard",
        key="back_button"
    ):
        st.session_state.page = "home"
        st.rerun()

    # HEADING
    st.html("""
    <div class="prediction-heading">

        <div class="badge">
            ✦ ML PREDICTION ENGINE
        </div>

        <h1>
            Student Performance Prediction
        </h1>

        <p>
            Enter student information to predict the Mathematics score.
        </p>

    </div>
    """)

    # FORM CARD
    st.html("""
    <div class="form-card">
        <div class="form-title">
            Student Information
        </div>
    </div>
    """)

    # FORM
    with st.form("prediction_form"):

        col1, col2 = st.columns(2, gap="large")

        with col1:

            gender = st.selectbox(
                "Gender",
                ["male", "female"],
                index=None,
                placeholder="Select gender"
            )

            race_ethnicity = st.selectbox(
                "Race / Ethnicity",
                [
                    "group A",
                    "group B",
                    "group C",
                    "group D",
                    "group E"
                ],
                index=None,
                placeholder="Select group"
            )

            parental_level_of_education = st.selectbox(
                "Parental Level of Education",
                [
                    "associate's degree",
                    "bachelor's degree",
                    "high school",
                    "master's degree",
                    "some college",
                    "some high school"
                ],
                index=None,
                placeholder="Select education level"
            )

            lunch = st.selectbox(
                "Lunch",
                [
                    "standard",
                    "free/reduced"
                ],
                index=None,
                placeholder="Select lunch type"
            )

        with col2:

            test_preparation_course = st.selectbox(
                "Test Preparation Course",
                [
                    "none",
                    "completed"
                ],
                index=None,
                placeholder="Select preparation status"
            )

            reading_score = st.number_input(
                "Reading Score",
                min_value=0.0,
                max_value=100.0,
                value=None,
                step=1.0,
                placeholder="Enter reading score"
            )

            writing_score = st.number_input(
                "Writing Score",
                min_value=0.0,
                max_value=100.0,
                value=None,
                step=1.0,
                placeholder="Enter writing score"
            )

        st.write("")

        submitted = st.form_submit_button(
            "Generate Mathematics Prediction →",
            use_container_width=True
        )


    # =====================================================
    # PREDICTION LOGIC
    # =====================================================

    if submitted:

        if (
            gender is None
            or race_ethnicity is None
            or parental_level_of_education is None
            or lunch is None
            or test_preparation_course is None
            or reading_score is None
            or writing_score is None
        ):

            st.warning(
                "Please fill in all 7 fields before generating the prediction."
            )

        else:

            try:

                # SAME LOGIC AS YOUR ORIGINAL app.py

                data = CustomData(
                    gender=gender,
                    race_ethnicity=race_ethnicity,
                    parental_level_of_education=
                        parental_level_of_education,
                    lunch=lunch,
                    test_preparation_course=
                        test_preparation_course,
                    reading_score=float(reading_score),
                    writing_score=float(writing_score)
                )

                pred_df = data.get_data_as_data_frame()

                predict_pipeline = PredictPipeline()

                results = predict_pipeline.predict(pred_df)

                prediction = float(results[0])

                progress = max(
                    0,
                    min(100, prediction)
                )

                st.html(f"""
                <div class="result">

                    <div class="result-label">
                        PREDICTED MATHEMATICS SCORE
                    </div>

                    <div class="result-score">
                        {prediction:.2f}
                    </div>

                    <div class="result-text">
                        Predicted score out of 100
                    </div>

                    <div class="result-bar">

                        <div
                            class="result-fill"
                            style="width:{progress}%;">
                        </div>

                    </div>

                </div>
                """)

            except Exception as e:

                st.error(
                    "Prediction could not be generated."
                )

                st.exception(e)

    st.html("""
    <div class="footer">
        Student Performance AI • Machine Learning Project
    </div>
    """)