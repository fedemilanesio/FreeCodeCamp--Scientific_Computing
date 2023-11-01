class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.income= 0
        self.expense = 0
        self.stato=False

    def __repr__(self):
        count = -1
        format_ledger = self.name.center(30, '*')
        for i in range(len(self.ledger)):
            count += 1
            descr = self.ledger[count]['description']
            amount = '{0:.2f}'.format(self.ledger[count]['amount'])
            if len(amount) > 7:
                amount = amount[:7]
            if len(self.ledger[count]['description']) > 23:
                cut_descr = self.ledger[count]['description'][0:23]
                format_ledger += f'''\n{cut_descr}{amount.rjust(30 - len(cut_descr))}'''
            else:
                format_ledger += f'''\n{descr}{amount.rjust(30 - len(descr))}'''

        self.total = f"{self.get_balance():.2f}"
        format_ledger += f'''\n{'Total:'} {self.total}'''
        return format_ledger

    def deposit(self,amount,*args):
        deposit={}
        self.amount=float(amount)
        self.description = args[0] if args else ''

        deposit['description'] = self.description
        deposit['amount'] = self.amount
        self.income+=float(deposit['amount'])
        self.ledger.append(deposit)

    def withdraw(self, amount, *args):
        withdraw = {}
        self.amount= float(amount)
        if args:
            self.description = args[0]
        else:
            self.description = ''
        withdraw['description'] = self.description
        withdraw['amount']=self.amount*(-1)
        self.check_funds(abs(float(withdraw['amount'])))
        if self.stato==False:
            return False
        elif self.stato==True:
            self.expense += float(withdraw['amount'])
            self.ledger.append(withdraw)
            return True

    def transfer(self,amount,instance):
        descr_in = f'''{'Transfer to '}{instance.name}'''
        if self.stato==False:
            return False
        elif self.stato==True:
            self.withdraw(float(amount), descr_in)
            descr_out = f'''{'Transfer from '}{self.name}'''
            instance.deposit(float(amount), descr_out)
            return True

    def check_funds(self,amount):
        if abs(amount)>self.get_balance():
            return self.stato
        else:
           self.stato=True
           return self.stato

    def get_balance(self):
        self.total=self.income+self.expense
        return self.total

food = Category('Food')
clothing=Category('Clothing')
party=Category('Party')
entertainment=Category('Entertainment')
auto = Category('Auto')


food.deposit(300, 'deposit')
clothing.deposit(150,'deposit')
food.withdraw(65,'eggs,salmon,avocado,mortadella')
party.deposit(70,'deposit')
party.withdraw(25,'clubbing')
#party.withdraw(16,'alcol')
food.transfer(15,party)

def create_spend_chart(list):
    chart=f'''Percentage spent by each category\n'''
    categs=[]
    percentages=[]
    count=0
    total=0
    for i in list:
        categs.append(i.name)
        count+=1
        total+=int(abs(i.expense))

    for j in list:
        perc=int((abs(j.expense)/total*100)//10)*10
        percentages.append(perc)

    for num in range(100,-10,-10):
        chart+=f'''{(str(num)+'|').rjust(4)}'''
        for perc in percentages:
            if perc>=num:
                chart+=' o '
            else:chart+='   '
        chart+=' \n'

    chart+='    '+('-'*(len(categs)+2)*2)+'\n'
    max=0
    for name in categs:
        if len(name)>max: max=len(name)

    new_names=[ names.ljust(max) for names in categs]
    for name in zip(*new_names):
        chart+='     '+('  '.join(name)) + '  \n'

    return chart.rstrip('\n')

print(create_spend_chart([party,food]))

'''
ciao=['ciao','hello']
for i in zip(*ciao):
    print(' '.join(i))
    #print()
'''