#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, redirect
import random

app = Flask(__name__)

# 三份问卷链接
SURVEY_LINKS = [
    "https://ust.az1.qualtrics.com/jfe/form/SV_ezjxfQJClPscq7s",  # control group
    "https://ust.az1.qualtrics.com/jfe/form/SV_eEgZOi8lCEBdZLU",  # soft
    "https://ust.az1.qualtrics.com/jfe/form/SV_1SyxIrE1j9WhZdA"   # hard
]

@app.route("/")
def index():
    selected_link = random.choice(SURVEY_LINKS)
    return redirect(selected_link)

if __name__ == "__main__":
    app.run(debug=True, port=1234)


# In[ ]:





# In[ ]:




