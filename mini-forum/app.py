from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Dictionary to store comments by topic, with a default "Main" topic
topics = {"main": []}

# HTML template with tabbed navigation for topics
html_template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Mini Forum</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
    <div class="tab-bar">
      <a class="title" href="{{ url_for('view_topic', topic='main') }}">mini<span>forum</span></a>
      {% for topic in topics %}
        <a href="{{ url_for('view_topic', topic=topic) }}" class="tab {% if current_topic == topic %}active{% endif %}">
          {{ topic }}
        </a>
      {% endfor %}
    </div>

    <form class="input-bar" method="POST" action="/">
      <span>topic:</span>
      <input class="topic" type="text" name="topic" value="main" required>
      <span>comment:</span>
      <input type="text" name="comment" required>
      <button type="submit">Post</button>
    </form>

    {% if current_topic %}
      {% for comment in topics[current_topic] %}
        <div class="comment">{{ comment }}</div>
      {% endfor %}
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the topic and comment from the form
        topic = request.form.get("topic")
        comment = request.form.get("comment")

        if topic and comment:
            # Initialize the topic list if it doesn't exist
            if topic not in topics:
                topics[topic] = []
            # Add the comment to the appropriate topic list
            topics[topic].append(comment)

        # Redirect to the "Main" topic after posting
        return redirect(url_for("view_topic", topic="main"))

    # Render the main page, defaulting to "Main" topic
    return redirect(url_for("view_topic", topic="main"))

@app.route("/topic/<topic>")
def view_topic(topic):
    # Ensure the topic exists, otherwise redirect to "Main"
    if topic not in topics:
        return redirect(url_for("view_topic", topic="main"))
    # Render the page for the specified topic with its comments
    return render_template_string(html_template, topics=topics, current_topic=topic)

if __name__ == "__main__":
    app.run(debug=True)
