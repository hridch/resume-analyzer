import streamlit as st
from AIModel import AIModel
import json

PROMPT = "Critically analyze the resume based on the given job description: "


def displayAnalysis(response):
    st.header("Analysis Result")
    result = json.loads(response.text)
    
    st.subheader("Overview")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Overall Match Score", f"{result["job_match_score"]["overall_score"]}%")
    with col2:
        st.write("💡 " + result["job_match_score"]["scoring_rationale"])

    st.subheader("Skills Match")
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ Matched skills")
        st.write(", ".join(result["matching_skills"]["matched"]))
    with col2:
        st.error("❌ Missing skills")
        st.write(", ".join(result["matching_skills"]["missing"]))


    st.subheader("Education Match")
    st.write("🎓 Requirement:", result["education_match"]["requirement"])
    st.write("📄 Candidate:", result["education_match"]["candidate"])

    if result["education_match"]["match"]:
        st.success("✅ Education Requirement Met")
    else:
        st.warning("⚠️ Education might not fully align")

    st.subheader("Keyword Match")
    st.progress(result["keyword_match"]["coverage_percent"] / 100)
    st.write(f"Coverage: {result["keyword_match"]["coverage_percent"]}%")
    with st.expander("Job Keywords"):
        st.write(result["keyword_match"]["job_keywords"])
    with st.expander("Resume Keywords Found"):
        st.write(result["keyword_match"]["resume_keywords_found"])


    st.subheader("Strengths")
    for strength in result["strengths"]:
        st.success(strength)

    st.subheader("Gaps")
    for gap in result["gaps"]:
        st.error(gap)

    st.subheader("Suggested Improvements")
    for improvement in result["suggested_improvements"]:
        st.info("👉 " + improvement)


def main():
    st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
    st.title("📄 Resume Analyzer")

    uploaded_resume = st.file_uploader(
        label="Upload your resume",
        type=["pdf"],
        accept_multiple_files=False,
        key=None,
        help=None,
        on_change=None,
        args=None,
        kwargs=None,
        disabled=False,
        label_visibility="visible",
        width="stretch",
    )

    job_description = st.text_area(
        label="Enter the job description here",
        value="",
        height=256,
        max_chars=None,
        key=None,
        help=None,
        on_change=None,
        args=None,
        kwargs=None,
        placeholder=None,
        disabled=False,
        label_visibility="visible",
        width="stretch",
    )

    is_button_clicked = st.button(
        label="Submit",
        key=None,
        help=None,
        on_click=None,
        args=None,
        kwargs=None,
        type="secondary",
        icon=None,
        disabled=False,
        use_container_width=None,
        width="content",
    )

    if uploaded_resume and job_description and is_button_clicked:
        with st.spinner("Please wait while we analyze your resume...", show_time=True):
            try:
                model = AIModel(uploaded_resume)
                response = model.generateResponse(prompt=PROMPT + job_description)
                displayAnalysis(response)

            except Exception as e:
                st.error(f"⚠️ Failed to analyze resume: {e}")

    else:
        st.info("👆 Please upload a resume document to begin.")


if __name__ == "__main__":
    main()
