from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

navigation = {
    'Pizza Toppings Form': '/',
    'Second Page': '/second',
    'Third Page': '/third'
}

@app.route('/', methods=['GET', 'POST'])
def checkbox_form():
    pizza_toppings = ["pepperoni", "sausage", "mushrooms", "onions", "green peppers"]
    input = "checkbox"
    tab_title = 'Template Logic'
    page_title = 'Checkbox Logic'
    
    if request.method == 'POST':
        choices = request.form.getlist('toppings')
    else:
        choices = []
    return render_template('checkbox_form.html', pizza_toppings=pizza_toppings,choices=choices, input=input, \
        tab_title=tab_title, page_title=page_title , navigation = navigation)

@app.route('/second', methods=['GET', 'POST'])
def second_page():
    tab_title= 'Template Logic'
    page_title='Second Page'

    if request.method == 'POST':
        choice = request.form['choice']
        if choice == 'yes':
            return redirect('/third')
        else:
            page_title = "Welcome Back!"

    return render_template('second.html', tab_title=tab_title, page_title=page_title , navigation = navigation)

@app.route('/third', methods=['GET', 'POST'])
def third_page():
    tab_title= 'Template Logic'
    page_title='Third Page'

    if request.method == 'POST':
        method_message = "Post request"
    else:
        method_message = "Get request"

    return render_template('third.html', tab_title=tab_title, page_title=page_title , navigation = navigation, \
        method_message= method_message)


if __name__ == '__main__':
    app.run()