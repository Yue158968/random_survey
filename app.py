from flask import Flask, redirect, request
import random
from datetime import datetime
import os

app = Flask(__name__)

# 三份问卷链接及标签
SURVEY_LINKS = [
    ("https://ust.az1.qualtrics.com/jfe/form/SV_ezjxfQJClPscq7s", "control group"),
    ("https://ust.az1.qualtrics.com/jfe/form/SV_eEgZOi8lCEBdZLU", "soft"),
    ("https://ust.az1.qualtrics.com/jfe/form/SV_1SyxIrE1j9WhZdA", "hard")
]

@app.route("/")
def index():
    selected_link, label = random.choice(SURVEY_LINKS)

    # 记录访问日志
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
          f"Visitor IP: {request.remote_addr} -> Assigned to: {label}")

    return redirect(selected_link)

if __name__ == "__main__":
    # Render会自动设置PORT环境变量，我们需要读取它
    port = int(os.environ.get("PORT", 1234))
    app.run(host="0.0.0.0", port=port)




