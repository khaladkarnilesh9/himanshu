import streamlit as st
from rxn4chemistry import RXN4ChemistryWrapper

# Load API key from Streamlit secrets
API_KEY = st.secrets["ibm_rxn_api_key"]

# Initialize IBM RXN wrapper with API key
rxn_wrapper = RXN4ChemistryWrapper(api_key=API_KEY)

st.title("Chemistry Protocol Extractor")

st.write("Paste your chemical reaction procedure text below:")

input_text = st.text_area("Reaction Procedure Text", height=300)

if st.button("Extract Protocol Steps"):
    if not input_text.strip():
        st.warning("Please enter some reaction procedure text first.")
    else:
        with st.spinner("Extracting synthesis protocol steps..."):
            try:
                result = rxn_wrapper.paragraph_to_actions(paragraph=input_text)
                actions = result.get("actions", [])
                if actions:
                    st.subheader("Extracted Protocol Steps:")
                    for i, action in enumerate(actions, 1):
                        st.write(f"{i}. {action}")
                else:
                    st.info("No protocol steps extracted. Please verify the input format.")
            except Exception as e:
                st.error(f"Error calling IBM RXN API: {e}")

