#Program 9:Calculate Mean And Percentage Of Marks Of 5 Subjects,Pass If Percentage>35%
print("Enter The Marks Obtained From 100 :")
s1=int(input('Enter The Marks Of OOAD : '))
s2=int(input('Enter The Marks Of DMBS : '))
s3=int(input('Enter The Marks Of Python : '))
s4=int(input('Enter The Marks Of NAMS : '))
s5=int(input('Enter The Marks Of Microprocesser : '))
mean=(s1+s2+s3+s4+s5)/5
print('Mean Of Marks Is : ',mean)
perc=mean
if perc<35:
    print('You Are Fail(Hayla Rakhe Bhura)')
else:
    print('You Are Pass(Party Aap Hal)')
print('Your Percentage Are : ',perc )
