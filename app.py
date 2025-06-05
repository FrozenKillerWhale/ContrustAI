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
        Thankophobia you for using **ConTrust AI**!

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
    # 콜백 함수: 체크박스가 변경되면 세션 상태만 True로 설정하고,
    # 재실행은 메인 App Execution Flow Control에서 담당하도록 변경
    def agree_checkbox_callback():
        st.session_state.agreed_to_terms = True

    st.checkbox(
        "I have read and agree to the Terms of Service and Privacy Policy regarding data collection and usage.",
        key="agreement_checkbox_key",
        on_change=agree_checkbox_callback # 체크박스 변경 시 콜백 함수 호출
    )

    # Note: `st.success` 메시지는 콜백이 즉시 rerun을 호출하지 않으므로,
    # 여기서는 동의 후 바로 메인 앱으로 넘어가지 않는다면 메시지를 표시할 수 있습니다.
    if st.session_state.agreed_to_terms: # 콜백이 상태를 True로 변경했을 때 (다음 런에서)
        st.success("Thank you for agreeing! Loading the main application...")


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
    # 당신의 실제 설문조사 URL로 변경합니다.
    st.link_button("Take Survey 📝", url="https://forms.gle/bsPrVBZnwpWMizDU9") # ✨ 여기를 업데이트했습니다!
st.write("Thank you for your valuable contribution!")


# --- Main App Execution Flow Control ---
# This is the entry point of your Streamlit app.
# It checks if the user has agreed to the terms; if not, it shows the agreement UI.
# 동의 상태가 True로 바뀌면, 다음 Streamlit 런에서 main_app()이 호출됩니다.
if not st.session_state.agreed_to_terms:
    show_agreement_ui()
else:
    main_app()