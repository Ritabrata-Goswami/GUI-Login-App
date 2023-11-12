# GUI-Login-App
By this GUI app we will do simple User Login and fetch the information about the user in dashboard.
This application used PyQt5. And For DB it used SQL Server.
The design of this application has build by QSS i.e. Qt Style Sheets.
QSS is very much similar to Cascading Style Sheets (CSS) for the web. The Syntax is also similar. 
For Example:-
```
QLineEdit {
  border-radius: 8px;
  border: 1px solid #e0e4e7;
  padding: 5px 15px;
}
```
or
```
#FirstHeading{
    font-size:25px;
    color:#00091a;
    margin-bottom: 5px;
    font-family: Monospace;
}
```
#FirstHeading is also use in web application in HTML to indicate 'Id' of an HTML element. But here it will indicate setObjectName("FirstHeading").
However, QSS supports only a limited number of rules in comparison with CSS.

The QSS file has to keep in same directoy as Py file and add this file by below syntax.
```
app.setStyleSheet(Path('login.qss').read_text())
```
In seperate file.
