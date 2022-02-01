
CREATE DATABASE BookYourTicket;

USE BookYourTicket;


CREATE TABLE screen_11(
Row INT,
Col INT,
Name VARCHAR(50),
Gender VARCHAR(20),
PhoneNo VARCHAR(10),
Status VARCHAR(10),
PRIMARY KEY(Row,Col));

CREATE TABLE screen_12(
Row INT,
Col INT,
Name VARCHAR(50),
Gender VARCHAR(20),
PhoneNo VARCHAR(10),
Status VARCHAR(10),
PRIMARY KEY(Row,Col));

CREATE TABLE statistics(
Screen VARCHAR(20),
NoOfTickets INT,
Percenatge INT,
CurrentIncome INT,
TotolIncome INT);

INSERT INTO statistics (Screen ,TotalIncome)
VALUES ("screen1",640);
INSERT INTO statistics (Screen ,TotalIncome)
VALUES ("screen2",640);




