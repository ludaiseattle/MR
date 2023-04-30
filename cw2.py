from flask import Flask, render_template, request

app = Flask("Novelist")

history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ''
    output_text = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        history.append(input_text+"\n")
        output_text = ''.join(history)
    return render_template('index.html', input_text=input_text, output_text=output_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

