class Apple:
    def intro(self):
        return 'Apple is an american manufacturer of personal computers,\nsmartphones, tablet computers, computer peripherals, and computer software'

    def ceo(self):
        return 'Tim Cook is the CEO'


    def founders(self):
        return 'Steve Jobs, Steve Wozniak and Ronald Wayne are the founders'


if __name__ == '__main__':
    company = Apple()
    print(company.intro())
    print(company.ceo())
    print(company.founders())
