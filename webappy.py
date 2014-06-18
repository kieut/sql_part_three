from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")
    row = hackbright_app.get_student_by_github(student_github)
    grades = hackbright_app.show_all_grades(row[0], row[1])

    html = render_template("student_info.html", first_name = row[0],
                                                    last_name = row[1],
                                                    github = row[2],
                                                    grades = grades)

    return html
    #return hackbright_app.get_student_by_github(student_github)

if __name__ == "__main__":
    app.run(debug=True)