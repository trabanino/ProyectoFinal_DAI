class Session:
    _session_data = {}

    @staticmethod
    def set(key, value):
        Session._session_data[key] = value

    @staticmethod
    def get(key):
        return Session._session_data.get(key, None)

    @staticmethod
    def clear():
        Session._session_data = {}
