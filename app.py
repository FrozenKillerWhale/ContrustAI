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


# --- Agreement UI Function ---
# This function displays the terms & privacy agreement before the main app loads.
def show_agreement_ui():
    st.title("✨ ConTrust AI")
    st.header("Please Agree to Our Terms to Continue")

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

        st.markdown("""
        [Terms of Service](https://cloar.tech/terms_of_service) | [Privacy Policy](https://cloar.tech/privacy_policy)
        """)

    # --- Agreement checkbox and handling ---
    # 콜백 함수: 체크박스가 변경되면 세션 상태를 True로 설정
    def agree_checkbox_callback():
        st.session_state.agreed_to_terms = True
        # 콜백 내에서 즉시 rerun을 시도 (문제 발생 시 주석 처리하고 아래 메인 로직에서 제어)
        st.experimental_rerun()

    st.checkbox(
        "I have read and agree to the Terms of Service and Privacy Policy regarding data collection and usage.",
        key="agreement_checkbox_key",
        on_change=agree_checkbox_callback # 체크박스 변경 시 콜백 함수 호출
    )

    # Note: `st.success` 메시지는 콜백이 즉시 rerun을 호출할 때 화면에 잠깐만 보일 수 있습니다.
    # 동의 후 앱 재실행 로직은 주로 `if not st.session_state.agreed_to_terms` 외부에서 제어됩니다.


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

    # --- Donation Link Section ---
    # 이 섹션은 main_app() 함수 내부에 있어야 앱이 로드된 후에만 표시됩니다.
    st.markdown("---")
    st.subheader("💡 Support ConTrust AI!")
    st.write("Your support helps us improve the service and advance our AI models.")

    col1, col2, col3 = st.columns(3)
    with col1:
        # 당신의 실제 Buy Me a Coffee 페이지 주소를 넣습니다.
        st.link_button("Buy Me a Coffee! ☕", url="https://coff.ee/cloar") # 실제 링크 적용 완료!
    with col2:
        # 실제 이메일 주소를 넣습니다.
        st.link_button("Contact Us 📧", url="mailto:contact@cloar.tech") # 실제 이메일 주소 적용 완료!
    with col3:
        # 실제 설문조사 URL을 넣습니다. **이 부분은 당신이 직접 만든 설문조사 URL로 변경해야 합니다.**
        st.link_button("Take Survey 📝", url="YOUR_ACTUAL_SURVEY_URL_HERE")
    st.write("Thank you for your valuable contribution!")


# --- Main App Execution Flow Control ---
# This is the entry point of your Streamlit app.
# It checks if the user has agreed to the terms; if not, it shows the agreement UI.
if not st.session_state.agreed_to_terms:
    show_agreement_ui()
else:
    main_app()