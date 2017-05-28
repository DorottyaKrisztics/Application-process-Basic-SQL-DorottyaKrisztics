from flask import Flask, render_template, url_for
import query_handler
app = Flask(__name__)


@app.route('/mentors', methods=['GET'])
def mentors():

    mentors_query = query_handler.mentors_and_schools()
    print(mentors_query)
    return render_template("mentors_school.html", mentors=mentors_query, title="Mentors")


if __name__ == '__main__':
    app.run(debug=True)

