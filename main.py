from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
           form {
               background-color: #eee;
               padding: 20px;
               margin: 0 auto;
               width: 540px;
               font: 16px sans-serif;
               border-radius: 10px;
           }
           textarea {
               color: red;
               margin: 10px 0;
               width: 540px;
               height: 120px;
           }
        </style>
    </head>
    <body>
"""
rotateby_form = """
    <form action ="/encrypt" method ="post">
        <label>
            <input type ="text" name = "rot" value= "0" />
         
        </label>
           <input type ="textarea" name = "text" /> 
            <input type="submit" value="Submit"/>
    </form>   
    """   
footer = """  
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt(rot, text):
    local_rot = int(rot)
    local_text = text 
    value_text = rotate_string(local_text, local_rot)
    return "<h1>" + value_text + "</h1>"


@app.route("/")
def index():
    content = form + rotateby_form + footer
    return content 


app.run()    