import string as st
import numpy as np 

comp = st.ascii_letters
number = st.digits
exp = st.punctuation
alga = comp + number + exp
password = np.random.choice(list(alga),10)
print(password)
