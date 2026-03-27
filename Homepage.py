import streamlit as st
from utils.extracter import phonenums

st.set_page_config(page_title="Extract Phone Numbers from text", page_icon='📄')

st.markdown("""
<style>
/* alignment */
.stTabs [data-baseweb="tab-list"] {
    justify-content: center;
}

/* remove the default underline gap */
.stTabs [data-baseweb="tab-list"] {
    gap: 20px;
}

/* style individual tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 12px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

st.title("Extract Phone Numbers from Text")
st.caption("Paste text or upload a file — get a clean CSV of every Indian phone number found.")
with st.sidebar:
	st.space()
	st.space()
	st.caption("phonenums-melodyofasong")

st.write("Input")

input_container = st.container(border=True)

with input_container:
	rawtext, upload, webscraping = st.tabs(["Paste Text", "Upload File", "Web-Scraping"])
	with rawtext:
		placeholder_text = "Please contact our Delhi office at 98201 23456 or reach Priya on +91 84739 20011 for further assistance. You can also call our Mumbai helpline at 022-49871234 or WhatsApp Rajan at 7865043210 for quick responses."
		text = st.text_area(label="Copy Paste below:", placeholder=placeholder_text, height=150)

	with upload:
		file = st.file_uploader("Upload File", type=['txt'])
		if file is not None:
			text = file.read().decode('utf-8')
		else:
			text = None

	col1, col2 = st.columns([2, 1])

	with col2:
		extract = st.button("Extract Numbers" , icon=":material/arrow_forward:",shortcut="Enter")

with st.container(border=True) as output_container:
    col3, col4 = st.columns([2.5, 1])
    with col3:
        st.subheader("Results")
    with st.status("Extracting phone numbers...", expanded=True) as status:
    	if extract:
        	if not text or text.strip() == "":
        		st.warning("Input is empty.")
        	else:
        		try:
        			df = phonenums(text)
        			csv = df.to_csv().encode("utf-8")
        			status.update(label=f"Extracted {len(df)} numbers", state="complete", expanded=False)
        		except Exception as e:
        			status.update(label=f"Something went wrong: {e}", state="error")

        		with col4:
        			download = st.download_button(label="Download as CSV", data=csv,
                                   file_name="phonenumbers.csv", icon=":material/download:")
        		if download:
        			st.toast("Your csv file has been saved.")
        		st.dataframe(df)

st.caption("phonenums-melodyofasong")
