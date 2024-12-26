from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

#Memory items for skills
skills = [
    {'id': 1, 'name': 'Proactive'},
    {'id': 2, 'name': 'Empatheric'},
    {'id': 3, 'name': 'Call mom'}
]
next_id = 4

@app.route("/")
def home_view():
    return render_template('home.html', title="Jeronimo's portfolio", name='Jeronimo', lastname="Betancur Duque")

@app.route("/skills")
def skills_view():
    return render_template('skills.html', title="Jeronimo's skills", skills=skills)

@app.route("/create", methods=['GET', 'POST'])
def create_view():
    global next_id
    if request.method == 'POST':
        skill_name = request.form['name']
        if skill_name:
            new_skill = {'id': next_id, 'name': skill_name}
            skills.append(new_skill)
            next_id += 1
            return redirect(url_for('skills_view'))

    return render_template('create.html')

@app.route("/delete/<int:skill_id>", methods=["GET"])
def delete(skill_id):
    global skills
    

if __name__ == '__main__':
    app.run(debug=True)