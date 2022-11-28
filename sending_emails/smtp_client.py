import logging
import smtplib


class SmtpClient:
    def __init__(self, user, password, host, port):
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._connect()

    def _connect(self):
        try:
            self._server = smtplib.SMTP(self._host, self._port)
            self._server.starttls()
            self._server.login(self._user, self._password)
        except Exception:
            raise Exception('Не удалось подключиться к SMTP серверу.')

    def send(self, to, msg):
        self._server.sendmail(self._user, to, msg)
