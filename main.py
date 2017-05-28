from flask import Flask, render_template, url_for
import query_handler
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", title="Links to query pages")


@app.route('/mentors', methods=['GET'])
def mentors():

    mentors_query = query_handler.mentors_and_schools()
    print(mentors_query)
    return render_template("mentors_school.html", mentors=mentors_query, title="Mentors")


@app.route('/all-school', methods=['GET'])
def all_school():
    pass


@app.route('/mentors-by-country', methods=['GET'])
def mentors_by_country():
    pass


@app.route('/contacts', methods=['GET'])
def contacts():
    pass


@app.route('/applicants', methods=['GET'])
def applicants():
    pass


@app.route('/applicants-and-mentors', methods=['GET'])
def applicants_and_mentors():
    pass


if __name__ == '__main__':
    app.run(debug=True)

