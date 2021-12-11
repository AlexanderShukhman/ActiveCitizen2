from flask import Flask, render_template, redirect, request, abort, jsonify
#from flask_restful import Api
from forms.addcallform import AddCallForm
import joblib
import os


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = '2asdhasgj2543534ashdg'
app.config['JSON_AS_ASCII'] = False
predictor = joblib.load('model/my_log_reg')

@app.errorhandler(404)
def not_found(error):
    if request.path.startswith('/api/'):
        return jsonify({'error': 'url not found'}), 404
    else:
        return render_template('404.html', title='Страница не найдена'), 404


@app.route('/')
@app.route('/add_call', methods=['GET', 'POST'])
def add_call():
    form = AddCallForm()
    if form.validate_on_submit():
        message = form.message.data
        return redirect('/results')
    return render_template('add_call.html', title='Новое обращение',
                           form=form)


def main():
    #api.add_resource(call_resource.CallListResource, '/api/calls')
    #api.add_resource(call_resource.CallResource, '/api/calls/<int:id>')
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)

if __name__ == '__main__':
    main()
