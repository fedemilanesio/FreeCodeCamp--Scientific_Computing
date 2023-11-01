def arithmetic_arranger(problems, show):
    arranged_problems = ''
    ##CONDITIONS OF THE PROBLEMS
    if len(problems) > 5:
        return 'Error: Too many problems.'
    final_score = ''
    first = ''
    operator = ''
    second = ''
    numbers = ''
    for prob in problems:

        # print(prob.split())
        first += prob.split()[0] + ' '
        second += prob.split()[2] + ' '
        operator += prob.split()[1] + ' '
        numbers += prob.split()[0] + ' '
        numbers += prob.split()[2] + ' '

    for i in numbers.split():
        if len(i) > 4:
            return'Error: Numbers cannot be more than four digits.'

        try:
            type(int(i)) == type(0)
        except ValueError:
            return 'Error: Numbers must only contain digits.'


    for i in operator.split():
        if i not in '+-':
            return"Error: Operator must be '+' or '-'."


        ##ACTUAL SOLVER
        line1=first.split()
        line2=second.split()
        operator1=operator.split()

        l1=''
        l2=''
        l3=''
        result=''
        sum = []

        for index,i in enumerate(line1):
            width=max(len(line1[index]),len(line2[index]))
            maxi=width+2
            if operator1[index] == '+':
                sum = int(line1[index]) + int(line2[index])
            elif operator1[index] == '-':
                sum = int(line1[index]) - int(line2[index])
            if index==0:
                l1+=f'''{line1[index].rjust(maxi)}'''
            elif index>0:
                l1 += f'''{'    '}{line1[index].rjust(maxi)}'''
            if index==0:
                l2+=f'''{operator1[index]} {line2[index].rjust(width)}'''
            elif index>0:
                l2 += f'''{'    '}{operator1[index]} {line2[index].rjust(width)}'''
            if index==0:
                l3+=f'''{'-'*maxi}'''
            elif index>0:
                l3+=f'''{'    '}{'-'*maxi}'''

            if operator1[index] == '+':
                sum = int(line1[index]) + int(line2[index])
            elif operator1[index] == '-':
                sum = int(line1[index]) - int(line2[index])
            if index==0:
                result+=f'''{str(sum).rjust(maxi)}'''
            elif index>0:
                result+=f'''{'    '}{str(sum).rjust(maxi)}'''


        if show==False:
            final_score=f'''{l1}\n{l2}\n{l3}'''
        elif show==True:
            final_score=f'''{l1}\n{l2}\n{l3}\n{result}'''

        return final_score



ar_arranger = arithmetic_arranger(['o + 9','1 - 2','10 + 44','11 - 10','88 + 2'], True)
print(ar_arranger)
