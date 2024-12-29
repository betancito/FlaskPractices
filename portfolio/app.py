from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

#Memory items for skills
skills = [
    {'id': 1, 'name': 'Proactive'},
    {'id': 2, 'name': 'Empatheric'},
    {'id': 3, 'name': 'Numbers oriented'}
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
    skill_to_delete = next((skill for skill in skills if skill['id']==skill_id))
    if skill_to_delete:
        skills.remove(skill_to_delete)
        return redirect(url_for('skills_view'))
    else:
        return redirect(url_for('skills_view'))
    
@app.route("/edit/<int:skill_id>", methods=["GET", "POST"])
def edit(skill_id):
    global skills
    skill_to_edit=next((skill for skill in skills if skill['id']==skill_id), None)
    if not skill_to_edit:
        return redirect(url_for('skills_view'))
    
    if request.method == 'POST':
        new_name = request.form['name']
        if new_name:
            skill_to_edit['name'] = new_name
            return redirect(url_for('skills_view'))
        
    
    return render_template('edit.html', skill=skill_to_edit)
        

if __name__ == '__main__':
    app.run(debug=True)