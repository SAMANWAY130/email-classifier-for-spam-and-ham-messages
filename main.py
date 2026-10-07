import streamlit as st
import pickle
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from string import punctuation
from nltk.tokenize import word_tokenize
stp = stopwords.words("english")

model = pickle.load(open("model (1).pkl","rb"))
vec = pickle.load(open("vector.pkl","rb"))

st.title("EMAIL SPAM OR NOT")  
tab1,tab2 = st.columns(2)
with tab2 :
    st.image("data:image/png;base64,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",width = 100)
with tab1:
    st.subheader("this is a email classifier write msg here")   

    input = st.text_input("write......")    

    def trans(txt):
      txt = txt.lower()
      txt = word_tokenize(txt)
      a = []
      b = []
      c = []
      for i in txt :
        if i.isalnum():
          a.append(i)
      for i in  a :
        if (i not in stp) and (i not in punctuation):
          b.append(i)
      ps = PorterStemmer()
      for i in b :
        c.append(ps.stem(i))

      return " ".join(c)

    if st.button("predict"):
        input_data = trans(input)
        vector_data = vec.transform([input_data])
        result = model.predict(vector_data)
        if result == 0 :
           st.success("ham message")
        else :
           st.warning("spam message")   

  