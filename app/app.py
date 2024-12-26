from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'Welcome to the Inventory Management System!'

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=5000)
