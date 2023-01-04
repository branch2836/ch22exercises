from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def checkbox_form():
    pizza_toppings = ["pepperoni", "sausage", "mushrooms", "onions", "green peppers"]
    input = "radio"
    if request.method == "POST":
        input = request.form['input-type']
    return render_template('checkbox_form.html', pizza_toppings=pizza_toppings,input=input )

if __name__ == '__main__':
    app.run()