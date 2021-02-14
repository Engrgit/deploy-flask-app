from flask import Flask, render_template, request, jsonify

app= Flask('__name__')

@app.route('/Nurudeen') #To render the homepage
def test():
    return ("Nurudeen Gbadegesin")

@app.route('/test1/test2/Nurudeen', methods=['POST'])
def test1():
    return 'My name is Nurudeen'

if __name__ == '__main__':
    app.run(debug=True)
