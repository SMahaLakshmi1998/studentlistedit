from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
Student_list = [{"Name": "Mahalakshmi", "Age": 24, "Roll_NO": 101, "Marks": [90, 75, 80, 98, 75]},

                {"Name": "Nijanthan", "Age": 23, "Roll_NO": 102, "Marks": [90, 75, 80, 98, 65]},

                {"Name": "Selva", "Age": 22, "Roll_NO": 103, "Marks": [90, 75, 80, 78, 99]},

                {"Name": "Preethi", "Age": 22, "Roll_NO": 104, "Marks": [94, 75, 80, 88, 35]},

                {"Name": "Ajay", "Age": 23, "Roll_NO": 105, "Marks": [70, 85, 80, 98, 35]},

                {"Name": "Anand", "Age": 26, "Roll_NO": 106, "Marks": [90, 75, 85, 98, 35]},

                {"Name": "Pavitran", "Age": 21, "Roll_NO": 107, "Marks": [80, 98, 35, 90, 75]},

                {"Name": "Kumar", "Age": 25, "Roll_NO": 108, "Marks": [90, 80, 98, 35, 75]},

                {"Name": "Saranya", "Age": 26, "Roll_NO": 109, "Marks": [75, 80, 90, 98, 35]},

                {"Name": "Jeffin", "Age": 22, "Roll_NO": 110, "Marks": [98, 35, 90, 75, 80]}]


@app.route('/hai',methods=["POST","GET"])
def home():
         if request.method=="POST":
             name=request.form.get("name")
             age=request.form.get("age")
             roll=request.form.get("roll")
             tamil=request.form.get("tamil")
             english=request.form.get("english")
             maths=request.form.get("maths")
             science=request.form.get("science")
             social=request.form.get("social")
             marks=[tamil,english,maths,science,social]
             dic={}
             dic.update({"Name":name})
             dic.update({"Age":age})
             dic.update({"Roll_NO":roll})
             dic.update({"Marks":marks})
             Student_list.append(dic)
              
         return render_template("sample.html",s=Student_list)

@app.route('/<a>')
def fun1(a):
      Student_list.pop(int(a)-1)
      
      return render_template("sample.html",s=Student_list)
@app.route('/edit/<int:item>',methods=["POST","GET"])
def edit(item):
      if request.method=="POST":
             name=request.form.get("name")
             age=request.form.get("age")
             roll=request.form.get("roll")
             tamil=request.form.get("tamil")
             english=request.form.get("english")
             maths=request.form.get("maths")
             science=request.form.get("science")
             social=request.form.get("social")
             marks=[tamil,english,maths,science,social]
             
             dic=Student_list[int(item)-1]
             dic.update({"Name":name})
             dic.update({"Age":age})
             dic.update({"Roll_NO":roll})
             dic.update({"Marks":marks})
             return redirect(url_for('home'))
      edit_Student_list=Student_list[int(item)-1]
      return render_template("home.html",s=edit_Student_list)

      
      
if __name__=="__main__":
    app.run(debug=True)