create database Python_GUI

create table GUI_APP_LOGIN(
Id INT IDENTITY(1,1),
userId VARCHAR(150),
pass VARCHAR(150),
username VARCHAR(180),
age INT,
email VARCHAR(100),
phone VARCHAR(100)
)

INSERT INTO GUI_APP_LOGIN (userId,pass,username,age,email,phone) VALUES 
('abcd','abcd@123','John Doe',34,'John@gmail.com','43887426'),
('admin','admin@123','admin',38,'Admin@gmail.com','771246589'),
('Jani','Jani@123','Jani Doe',30,'Jani@gmail.com','124887136'),
('ritabrata','ritabrata@123','Ritabrata Goswami',27,'1995ritabrata@gmail.com','7980827297');

SELECT * FROM GUI_APP_LOGIN