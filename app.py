import streamlit as st

# --- Global CSS Injection ---
# This CSS applies custom styles to buttons and textareas across the app.
# Place this at the very top, right after imports, for app-wide styling.
st.markdown(
    """
    <style>
    /* General button styling for a consistent look */
    .stButton>button {
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        font-size: 18px; /* Larger font */
        padding: 10px 24px; /* More padding */
        border-radius: 8px; /* Rounded corners */
        border: none; /* No default border */
        cursor: pointer; /* Pointer on hover */
        transition: background-color 0.3s ease; /* Smooth transition */
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }

    /* Text area styling for better readability */
    textarea {
        font-family: 'Arial', sans-serif; /* A common sans-serif font */
        font-size: 16px; /* Comfortable reading size */
        line-height: 1.6; /* Good line spacing */
    }

    /* Styling for Streamlit's info/warning boxes */
    .stAlert {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Session State Initialization (Check for user consent) ---
# This ensures 'agreed_to_terms' is always in session_state, initialized to False
# It controls whether the app shows the consent UI or the main features.
if 'agreed_to_terms' not in st.session_state:
    st.session_state.agreed_to_terms = False


# --- Main Application Logic Function ---
# This function contains the core features of your ConTrust AI service.
def main_app():
    st.title("✨ ConTrust AI: Content Authenticity & Originality Analysis")
    st.write("Enter your content below to check its authenticity and originality.")

    user_input_text = st.text_area("Paste your text here for analysis:", height=250, help="Max 5000 words for optimal performance.")

    if st.button("Analyze Content"):
        if user_input_text:
            with st.spinner("Analyzing your content..."):
                # --- PHASE 0 MVP LOGIC PLACEHOLDER ---
                # This is where your AI analysis logic will go.
                # For now, it's just a placeholder.
                # In Phase 1, you'll integrate Claude here.
                # Example placeholder results:
                import time
                time.sleep(2) # Simulate analysis time

                ai_score = 0.75 # Example: 75% AI generated probability
                originality_score = 0.60 # Example: 60% originality score

                st.subheader("Analysis Results:")

                # AI Detection Result Display
                if ai_score > 0.5:
                    st.error(f"**AI Generated Probability:** {ai_score*100:.1f}% 🤖")
                    st.write("This content shows characteristics commonly found in AI-generated text. Consider reviewing for human touch.")
                else:
                    st.success(f"**AI Generated Probability:** {ai_score*100:.1f}% 🧑‍💻")
                    st.write("This content appears to be human-generated or heavily edited by a human.")

                # Originality Check Result Display
                st.info(f"**Content Originality Score:** {originality_score*100:.1f}% ✨")
                if originality_score < 0.7:
                    st.warning("This content might contain similar phrases or ideas found in existing sources. Review for potential duplication.")
                else:
                    st.success("Your content appears highly original!")

                st.markdown("---")
                st.write("💡 *Note: These are initial analysis results. For a more detailed breakdown, consider our advanced features.*")

                # --- END OF PHASE 0 MVP LOGIC PLACEHOLDER ---

        else:
            st.warning("Please paste some text into the box to start the analysis.")

    # --- Donation Link Section (Will be updated after publishing URL is available) ---
    st.markdown("---")
    st.subheader("💡 Support ConTrust AI!")
    st.write("Your support helps us improve the service and advance our AI models.")
    # ✨ 수정된 부분: st.link_button을 사용하여 버튼을 가로로 배치
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("Buy Me a Coffee! ☕", url="https://www.buymeacoffee.com/yourusername") # 실제 링크로 변경
    with col2:
        st.link_button("Contact Us 📧", url="mailto:your.email@example.com") # 실제 이메일 주소로 변경
    with col3:
        st.link_button("Take Survey 📝", url="your_survey_url") # 실제 설문조사 URL로 변경
    st.write("Thank you for your valuable contribution!")


# --- Agreement UI Function ---
# This function displays the terms & privacy agreement before the main app loads.
def show_agreement_ui():
    # ✨ 추가된 부분: 동의 화면 상단에도 앱 이름 표시
    st.title("✨ ConTrust AI")
    st.header("Please Agree to Our Terms to Continue")

    # 텍스트 내용 전체를 st.expander 안에 넣어 접기
    with st.expander("Read Important Information Regarding Data Collection & Usage"):
        st.markdown("""
        Thank you for using **ConTrust AI**!

        To provide you with the best service and continuously improve our AI models, we utilize the text you input for analysis. Your input content helps us:
        * **Enhance the accuracy of our AI detection and originality checks.**
        * **Advance the development of our `Galad AI` sociopsychological profiling models.**

        **✅ Important Information:**
        * **Only the text content you input for analysis is collected.** We do not collect any other personal information from you.
        * All collected text data is **fully anonymized**, meaning it cannot be linked back to you or any specific individual.
        * Anonymized data is used **solely for service improvement and AI model training purposes.**
        * For more details, please refer to our full policies below.
        """)

        # --- IMPORTANT: Replace these links with your actual URLs ---
        # You will need to create these pages (e.g., on your Cloar.tech domain or a separate Streamlit page)
        st.markdown("""
        [Terms of Service](https://cloar.tech/terms_of_service) | [Privacy Policy](https://cloar.tech/privacy_policy)
        """)
        # --- END OF LINK PLACEHOLDERS ---

    # Consent checkbox
    # ⚠️ 핵심 수정 부분: 체크박스 변경 여부를 확인하고 콜백 함수를 사용 (안정성 증대)
    # 콜백 함수 정의
    def set_agreed_state():
        st.session_state.agreed_to_terms = True

    agree_checkbox = st.checkbox(
        "I have read and agree to the Terms of Service and Privacy Policy regarding data collection and usage.",
        key="agreement_checkbox_key", # 고유한 키 추가 (필수)
        on_change=set_agreed_state # 체크박스 상태 변경 시 함수 호출
    )

    # 체크박스가 선택되었지만 아직 세션 상태가 True가 아닌 경우 (초기 로드 시)
    if agree_checkbox and not st.session_state.agreed_to_terms:
        # 이전에 발생한 오류의 원인 중 하나가 이중 호출일 수 있으므로,
        # 여기서는 바로 rerun 하지 않고, on_change 콜백에 의존합니다.
        # 만약 콜백이 작동하지 않는 Streamlit 구 버전이라면,
        # 아래 st.success 다음에 st.experimental_rerun()을 다시 활성화해야 할 수도 있습니다.
        st.success("Thank you for agreeing! Please refresh the page or wait for the app to reload.")
        # 만약 위의 수정으로도 오류가 지속되면, 아래 줄의 주석을 해제하세요.
        # st.experimental_rerun() # 동의 후 앱을 새로고침하여 메인 앱 표시


# --- Main App Execution Flow Control ---
# This is the entry point of your Streamlit app.
# It checks if the user has agreed to the terms; if not, it shows the agreement UI.
if not st.session_state.agreed_to_terms:
    show_agreement_ui()
else:
    main_app()