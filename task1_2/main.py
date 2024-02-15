import mysql.connector
import smtplib


host = "localhost"
user = "olegfadeev"
password = "pass"
database = "SKELAR"


gmail_sender = "test@gmail.com"
gmail_password = "pass"
gmail_receiver = "test6@gmail.com"

connection = mysql.connector.connect(
    host=host, user=user, password=password, database=database
)

query1 = "SELECT * FROM x27_social_dialogs WHERE id_user_to = 12345;"

cursor = connection.cursor()
cursor.execute(query1)
results1 = cursor.fetchall()

query2 = """
SELECT *
FROM x27_social_dialogs 
WHERE id_user_to = 12345
AND date_created >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
AND has_new_msg = 1;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

message = "**Data from MySQL**\n\n**All user dialogs with ID = 12345:**\n\n"
for row in results1:
    message += f"{row}\n"

message += "\n**User dialogs with ID = 12345 for the last week with new messages:**\n\n"
for row in results2:
    message += f"{row}\n"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(gmail_sender, gmail_password)
server.sendmail(gmail_sender, gmail_receiver, message)
server.quit()

cursor.close()
connection.close()


#add to the crontab file
#crontab -e
#0 12 * * 1 python /Users/olegfadeev/Desktop/SKELLAR/task1_2.py/main.py

