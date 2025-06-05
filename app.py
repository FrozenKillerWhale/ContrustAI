import streamlit as st

# --- Global CSS Injection ---
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
if 'agreed_to_terms' not in st.session_state:
    st.session_state.agreed_to_terms = False


# --- Agreement UI Function ---
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
    # 콜백 함수: 체크박스가 변경되면 세션 상태만 True로 설정합니다.
    # st.experimental_rerun()은 호출하지 않습니다.
    def agree_checkbox_callback():
        st.session_state.agreed_to_terms = True

    st.checkbox(
        "I have read and agree to the Terms of Service and Privacy Policy regarding data collection and usage.",
        key="agreement_checkbox_key",
        on_change=agree_checkbox_callback # 체크박스 변경 시 콜백 함수 호출
    )

    # 사용자가 동의 체크박스를 클릭했을 때 표시되는 메시지
    # 앱이 자동으로 재실행되지 않으므로, 이 메시지를 통해 사용자에게 안내합니다.
    if st.session_state.agreed_to_terms:
        st.success("Thank you for agreeing! The app will reload to show the main features. Please wait or refresh the page if it doesn't automatically transition.")


# --- Main Application Logic Function ---
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
    st.markdown("---")
    st.subheader("💡 Support ConTrust AI!")
    st.write("Your support helps us improve the service and advance our AI models.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("Buy Me a Coffee! ☕", url="https://coff.ee/cloar")
    with col2:
        st.link_button("Contact Us 📧", url="mailto:contact@cloar.tech")
    with col3:
        st.link_button("Take Survey 📝", url="https://forms.gle/bsPrVBZnwpWMizDU9")
    st.write("Thank you for your valuable contribution!")


# --- Main App Execution Flow Control ---
# 이 부분은 변경되지 않았습니다.
if not st.session_state.agreed_to_terms:
    show_agreement_ui()
else:
    main_app()