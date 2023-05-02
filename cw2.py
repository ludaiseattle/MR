from flask import Flask, render_template, request
import smtplib

app = Flask("Novelist")

history = []
emails = []

history.append("It was an evening in 1870, and in front of you was the famous Red Square. \
        A bonfire was burning in the middle of Red Square, and people \
        from all around the world were sitting by the fire. \
        There were merchants, explorers, killers, and lumberjack, each with a story to tell...")

def send_email(subject, message, from_email, to_email):
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(from_email, 'MR@666MR@666') 
    msg = f'Subject: {subject}\n\n{message}'
    server.sendmail(from_email, to_email, msg.encode('utf-8'))
    server.quit()

def get_history():
    return history

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ''
    output_text = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        history.append(input_text)
        output_text = '<br>'.join(history) + '<br>'

        email = request.form['email']
        if email:
            emails.append(email)
        if len(emails):
            from_email = 'mixedreality888@outlook.com' 
            subject = 'Story Content'
            message = f'New Content: {input_text}'
            for to_email in emails:
                send_email(subject, message, from_email, to_email)

    return render_template('index.html', input_text=input_text, get_history=get_history)

if __name__ == '__main__':
    get_history()
    app.run(host='0.0.0.0', port=80)

