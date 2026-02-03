@app.route('/signup',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({
                "message" : "User already exists.please login"
            }),400
        hashed_password = generate_password_hash(password)
        