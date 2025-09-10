### **CHAT WITH MULTIPLE PDFs**
- UI built via streamlit
- Its a chatbot that allows to chat with multiple PDFs at once
- We upload PDFs then ask question which the chatbot 
- It will only answer questions related to the document uploaded

**LOGIC EXPLAINATION**
- Pdfs from user upload.
- Pdfs divided into pieces and chunks of texts.
- the chunks/pieces of texts converted to embeddings.
- embeddings are vector or simply number representation of texts.
- These embeddings/vector representations is stored into vector stores (Faiss).
- The questions of the user are going to be converted to similar embeddings.
- we will find the similar semantic context or meaning between the question/prompt embeddings and the document text chunk embeddings
- it will give ranked results of the chunks of texts based on similarity which we will send to the Language Model


**CODE EXPLAINATION**
- The st.spinner makes the user experience better as it shows processing when docs are first uploaded it will take time for all the conversion processes.
- the `get_conversation_chain` takes the history of the conversation and returns the next element 
- Streamlit tries to reinitialize variables as we click on a button so to persist the session we have used the `st.session_state.conversation` it also means the conversation variable is not going to be reinitialized
- also initializing conversation like this means we can use this variable outside of the sidebar too (`with.sidebar`).