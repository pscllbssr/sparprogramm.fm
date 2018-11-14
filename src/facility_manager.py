def sendReport(log_file):

    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.mime.application import MIMEApplication
    import radio_config
    from os.path import basename
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(radio_config.EMAIL_USER, radio_config.EMAIL_PASSWORD)

    message = MIMEMultipart()
    message['From'] = radio_config.EMAIL_SENDER
    message['To'] = radio_config.EMAIL_RECIPIENT
    message['Subject'] = "Sparprogramm.fm Log"
    body = "Sparprogramm.fm Log"
    message.attach(MIMEText(body, 'plain'))

    with open(log_file, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(log_file)
        )
        # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(log_file)
    message.attach(part)

    server.sendmail(radio_config.EMAIL_SENDER, radio_config.EMAIL_RECIPIENT, message.as_string())