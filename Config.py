class Config:
    def __init__(self):
        self.broker_ip = "172.16.138.15"
        self.port = 1883
        self.topic = "v1/devices/me/telemetry"
        self.access_token = "e8tbhn3bafvormt85vp1"

    def getBrokerIp(self):
        return self.broker_ip

    def getAccessToken(self):
        return self.access_token

    def getPort(self):
        return self.port

    def getTopic(self):
        return self.topic