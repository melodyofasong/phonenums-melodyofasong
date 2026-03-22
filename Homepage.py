import streamlit as st
from utils.extracter import phonenums

st.set_page_config(page_title="Extract Phone Numbers from text", page_icon='📄')
st.title("Extract Phone Numbers from Text")
st.caption("phonenums-melodyofasong")

st.write("Your input options are below")

outercol1, outercol2 = st.columns([3, 1])

with outercol1:
	with st.expander("Upload file"):
		file = st.file_uploader("Upload file", type=['txt'])
		if file is not None:
			text = file.read().decode('utf-8')
		else:
			text = None

	with st.expander("Or copy paste raw text:"):
		col1, col2 = st.columns(2)

		with col1:
			placeholder_text = "Please contact our Delhi office at 98201 23456 or reach Priya on +91 84739 20011 for further assistance. You can also call our Mumbai helpline at 022-49871234 or WhatsApp Rajan at 7865043210 for quick responses."
			text = st.text_area(label="Copy Paste below:", placeholder=placeholder_text, height=250)

		with col2:
			st.caption("Sample extracted phone numbers from placeholder text")
			st.table(phonenums(placeholder_text), border='horizontal')

with outercol2:
	with st.popover("Extract"):
		if st.button("Seperate"):
			if not text or text.strip() == "":
				st.warning("Input is empty.")
			else:
				csv = phonenums(text).to_csv().encode("utf-8")
				st.success(f"Successfully extracted {len(phonenums(text))} phone numbers from the provided text")
				st.download_button(label="Download as CSV", data=csv, 
							file_name="phonenumbers.csv", icon=":material/download:")
		
		with st.expander("Preview your extracted phone numbers"):
			st.table(phonenums(text), border='horizontal')

