import smtplib


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login("animeshkotka520@gmail.com", "Mark&Ruby")
server.sendmail(
  "animeshkotka520@gmail.com",
  "animeshkotka500@gmail.com",
  "this message is from python")
server.quit()