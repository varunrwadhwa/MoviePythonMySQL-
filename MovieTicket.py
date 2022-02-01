import mysql.connector
from mysql.connector import Error
class bookTicket:
  print("Hi welcome to BookYourMovie.com ", "\n")

  @classmethod
  def insertScree_11(cls,r, c,name,gender,phoneNo,status):
      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='BookYourTicket',
                                               user='root',
                                               password='root')
          cursor = connection.cursor()
          mySql_insert_query = """INSERT INTO screen_11 (Row,Col,Name,Gender,PhoneNo,Status)
                                  VALUES (%s, %s, %s, %s, %s, %s) """

          recordTuple = (r, c,name,gender,phoneNo,status)
          cursor.execute(mySql_insert_query, recordTuple)
          connection.commit()
          print("Booked successfully ")

      except mysql.connector.Error as error:
          print("Failed to insert into MySQL table {}".format(error))

      finally:
          if (connection.is_connected()):
              cursor.close()
              connection.close()

  @classmethod
  def insertScree_12(cls,r, c,name,gender,phoneNo,status):
      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='BookYourTicket',
                                               user='root',
                                               password='root')
          cursor = connection.cursor()
          mySql_insert_query = """INSERT INTO screen_12 (Row,Col,Name,Gender,PhoneNo,Status)
                                  VALUES (%s, %s, %s, %s, %s, %s) """

          recordTuple = (r, c,name,gender,phoneNo,status)
          cursor.execute(mySql_insert_query, recordTuple)
          connection.commit()
          print("Booked successfully ")

      except mysql.connector.Error as error:
          print("Failed to insert into MySQL table {}".format(error))

      finally:
          if (connection.is_connected()):
              cursor.close()
              connection.close()
  @classmethod
  def updateScreen1(cls):
      import mysql.connector
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='BookYourTicket',
                                               user='root',
                                               password='root')
          cursor = connection.cursor()

          sql_update_query = """Update statistics set  NoOfTickets = (select count(status) from screen_11),CurrentIncome=NoOfTickets * 10,Percentage=CurrentIncome / 560 * 100 where Screen = 'Screen1'"""
          cursor.execute(sql_update_query)
          connection.commit()
      except mysql.connector.Error as error:
          print("Failed to update table record: {}".format(error))
      finally:
          if (connection.is_connected()):
              connection.close()
      bookTicket.display()
  @classmethod
  def updateScreen2(cls):
      import mysql.connector
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='BookYourTicket',
                                               user='root',
                                               password='root')
          cursor = connection.cursor()

          sql_update_query = """Update statistics set  NoOfTickets = (select count(status) from screen_12),CurrentIncome=NoOfTickets * 10,Percentage=CurrentIncome / 640 * 100 where Screen = 'Screen2'"""
          cursor.execute(sql_update_query)
          connection.commit()
      except mysql.connector.Error as error:
          print("Failed to update table record: {}".format(error))
      finally:
          if (connection.is_connected()):
              connection.close()
      bookTicket.display()
  @classmethod
  def screen1(cls,rows,cols):
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='BookYourTicket',
                                               user='root',
                                               password='root')

          sql_select_Query = "select Row,Col from screen_11"
          cursor = connection.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          print("Cinema:")
          for m in range(0, cols):
              if m == 0:
                  print(" ", end=" ")
              else:
                  print(m, end=" ")
          for i in range(0, rows):
              print()
              for j in range(0, cols):
                  if (i == 0 and j >= 0):
                      print(" ", end=' ')
                      break
                  if i > 0 and j == 0:
                      print(i, end=' ')
                  else:
                      if (i, j) in (records):

                          print('B', end=' ')
                      else:
                          print('S', end=" ")

      except Error as e:
          print("Error reading data from MySQL table", e)
      finally:
          if (connection.is_connected()):
              connection.close()
              cursor.close()
  @classmethod
  def screen2(cls,rows,cols):
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='BookYourTicket',
                                               user='root',
                                               password='root')

          sql_select_Query = "select Row,Col from screen_12"
          cursor = connection.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          print("Cinema:")
          for m in range(0, cols):
              if m == 0:
                  print(" ", end=" ")
              else:
                  print(m, end=" ")
          for i in range(0, rows):
              print()
              for j in range(0, cols):
                  if (i == 0 and j >= 0):
                      print(" ", end=' ')
                      break
                  if i > 0 and j == 0:
                      print(i, end=' ')
                  else:
                      if (i, j) in (records):

                          print('B', end=' ')
                      else:
                          print('S', end=" ")
      except Error as e:
          print("Error reading data from MySQL table", e)
      finally:
          if (connection.is_connected()):
              connection.close()
              cursor.close()

  @classmethod
  def yourChoice(cls):
      print("1.  screen1 (less than 60 seats)\n")
      print("2. screen2 (More than 60 seats)\n")
  @classmethod
  def screenDisp(cls):
      select = int(input("Please select the screen\n"))
      if select == 1:
          bookTicket.screen1(6, 8)
          print()
          print("Want to Booked Ticket:\n")
          print("1. Yes")
          print("2. No")
          ch = int(input("select 1 or 2:\n"))
          if ch == 1:
              bookTicket.display()
          if ch == 2:
              bookTicket.display()
      if select == 2:
              bookTicket.screen2(8, 8)
              print()
              print("Want to Booked Ticket:\n")
              print("1. Yes")
              print("2. No")
              ch = int(input("select 1 or 2:\n"))
              if ch == 1:
                 bookTicket.display()
              if ch == 2:
                  bookTicket.display()
  @classmethod
  def statisticsDetail1(cls):
          try:
              mySQLConnection = mysql.connector.connect(host='localhost',
                                                    database='BookYourTicket',
                                                    user='root',
                                                    password='root')

              cursor = mySQLConnection.cursor(buffered=True)
              sql_select_query = """select * from statistics """
              cursor.execute(sql_select_query)
              record = cursor.fetchall()
              for r in record:
                  print("Screen = ", r[0], )
                  print("NoOfTickets = ", r[1])
                  print("Percentage = ", r[2])
                  print("CurrentIncome = " ,r[3])
                  print("TotalIncome = ", r[4])
                  print()
          except mysql.connector.Error as error:
          # print("Failed to get record from MySQL table: {}".format(error))
              print("Something wrong")
          finally:
              if (mySQLConnection.is_connected()):
                  cursor.close()
                  mySQLConnection.close()
          bookTicket.display()
  @classmethod
  def getUserDetail1(cls,row,col):
      try:
          mySQLConnection = mysql.connector.connect(host='localhost',
                                                    database='BookYourTicket',
                                                    user='root',
                                                    password='root')

          cursor = mySQLConnection.cursor(buffered=True)
          sql_select_query = """select * from screen_11 where row = %s and col = %s"""
          cursor.execute(sql_select_query, (row,col))
          record = cursor.fetchall()
          for r in record:
              print("Name = ", r[2], )
              print("Gender = ", r[3])
              print("PhoneNo = ", r[4])
              print("Price = " ,"$10")
      except mysql.connector.Error as error:
          # print("Failed to get record from MySQL table: {}".format(error))
          print("Something wrong")
      finally:
          if (mySQLConnection.is_connected()):
              cursor.close()
              mySQLConnection.close()
  @classmethod
  def getUserDetail2(cls,row,col):
      try:
          mySQLConnection = mysql.connector.connect(host='localhost',
                                                    database='BookYourTicket',
                                                    user='root',
                                                    password='root')
          cursor = mySQLConnection.cursor(buffered=True)
          sql_select_query = """select * from screen_12 where row = %s and col = %s"""
          cursor.execute(sql_select_query, (row,col))
          record = cursor.fetchall()
          for r in record:
              if r[0] <= 4:
                      print("Name = ", r[2])
                      print("Gender = ", r[3])
                      print("PhoneNo = ", r[4])
                      print("Price = " ,"$10")
              else:
                      print("Name = ", r[2], )
                      print("Gender = ", r[3])
                      print("PhoneNo = ", r[4])
                      print("Price = ", "$8")
      except mysql.connector.Error as error:
          # print("Failed to get record from MySQL table: {}".format(error))
          print("Something wrong")

      finally:
          if (mySQLConnection.is_connected()):
              cursor.close()
              mySQLConnection.close()
  @classmethod
  def display(cls):
    print("Please Enter your choice:")
    print("**********************************************************************")
    print("0. Exit")
    print("1. Show the Seats.")
    print("2. Buy the ticket.")
    print("3. Statitics.")
    print("4. Show booked ticket's user Info.")
    choice = int(input("Enter your choice:\n"))
    if choice == 0:
      exit()
    if choice == 1:
      bookTicket.yourChoice()
      bookTicket.screenDisp()

    if choice == 2:
      print("Book my ticket in:\n")
      print("1. screen1")
      print("2. Screen2")
      screenChoice = int(input("Select 1 or 2:\n"))
      if screenChoice == 1:
        r = int(input("Select the row\n"))
        c = int(input("select the col\n"))
        name = input("enter your name\n")
        gender = input("enter the gender\n")
        phoneNo = input("Enter the mbl no\n")
        bookTicket.insertScree_11(r, c, name, gender, phoneNo, "Booked")
        bookTicket.updateScreen1()
      if screenChoice == 2:
        r = int(input("Select the row\n"))
        c = int(input("select the col\n"))
        name = input("enter your name\n")
        gender = input("enter the gender\n")
        phoneNo = input("Enter the mbl no\n")
        bookTicket.insertScree_12(r, c, name, gender, phoneNo, "Booked")
        bookTicket.updateScreen2()
    if choice == 4:
      print("1. Show data from screen1")
      print("2. Show data from screen2")
      datachoice = int(input("select1 or 2"))
      if datachoice == 1:
        user1Row = int(input("Enter User's Row:\n"))
        user1Col = int(input("Enter User's Col:\n"))
        bookTicket.getUserDetail1(user1Row, user1Col)
      if datachoice == 2:
        user2Row = int(input("Enter User's Row:\n"))
        user2Col = int(input("Enter User's Col:\n"))
        bookTicket.getUserDetail2(user2Row, user2Col)

    if choice == 3:
      bookTicket.statisticsDetail1()


disp = bookTicket()
disp.display()


