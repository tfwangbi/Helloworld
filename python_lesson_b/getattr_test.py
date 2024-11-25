class User:
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        # return 'Hello'
        pass


if __name__ == '__main__':
    user = User(info={'name': 'ZhangSan', 'company': 'ISSC'})
    print(user.name, user.company)
