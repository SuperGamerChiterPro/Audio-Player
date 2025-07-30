from flask import *

from SQLagent import SQLAgent

app = Flask("Kahoot")
app.secret_key = "237980"


@app.route("/")
def index():
    agent = SQLAgent("SQL.db")
    result = agent.get_audio()
    agent.db.close()
    return render_template("index.html", audios=result)


@app.route("/aboutus")
def aboutus():
    agent = SQLAgent("SQL.db")
    result = agent.get_audio()
    agent.db.close()
    return render_template("index.html", audios=result)


@app.route("/music_info/<int:audio_id>")
def music_info(audio_id):
    agent = SQLAgent("SQL.db")
    result = agent.get_audio_by_id(audio_id)
    agent.db.close()
    return render_template("music_info.html", audio=result)





app.run()