from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'Welcome to the Inventory Management System!'

if _name_ == "_main_":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
