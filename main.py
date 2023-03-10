from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

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
        tab_title=tab_title, page_title=page_title )

@app.route('/second', methods=['GET', 'POST'])
def second_page():
    tab_title= 'Template Logic'
    page_title='Second Page'

    return render_template('second.html', tab_title=tab_title, page_title=page_title)

if __name__ == '__main__':
    app.run()