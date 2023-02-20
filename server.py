from flask import Flask,render_template, request

app = Flask(__name__)


@app.route('/calculator',methods = ['GET','POST'])
def calculator():
    if request.method == 'GET': #בקשה דיפולט שולחת לעמוד הרגיל
        return render_template('calculator.html') 
    if request.method == 'POST':#אם מקבלים בקשת פוסט
        num1 = int(request.form["first_num"])
        num2 = int(request.form["second_num"])
        return render_template('show_result.html', first_num=num1, second_num=num2) #יכול לבחור אם להעביר ערכים ככה או ישירות בקובץ הדף לגשת לערכים של פלאסק פורם
        
    

app.run(debug=True)