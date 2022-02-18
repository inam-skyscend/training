# 38. Create a class Student and add member variables with False values. The variables
# are as listed below. Marks will have a default value blank list.
# 1. Name
# 2. Reg No
# 3. Roll No
# 4. Standard
# 5. Admission Year
# 6. Marks
# 7. Result
# Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission
# year. In the constructor add validation for Name to be only Alphabetic, Reg No to be
# alphanumeric, Roll No, Standard nad Admission year to be numeric. All abobve
# values will be accepted as string only. If the passed parameters are not string raise
# and Error to the user.
# Add a method that will accept a dictionary for marks containing subject as key and
# marks as values. It will add the dictionary to the list of marks. Marks list will have
# multiple elements and each element will be a dictionary only. Here there should be a
# validation to acccept the marks which are less than or equal to 100 only. If the
# obtained marks are less than 40 the result willl be fail otherwise pass. In the
# dictionary the result can be added.

# Add another method that will generate the result. This method will check if there
# is any line in the marks having fail as result the result will be Fail and it will print the
# complete result as following.
# If any of the result is Fail the Percentage will not be shown and only -- will be
# printed instead.
# Define a function to calculate the grade. For Example if the result is fail for any
# subject it will be F grade. If the Percentage is 95+ it will be O+. If the percentage is
# 90+ and less than 95 then it will be O. If the percentage is 85+ and less than 90 it will
# be A+. If the Percentage is 80+ and less than 85 it will be A. If the Percentage is 75+
# and less than 80 it will be a B+. If the percentgae is 70+ and less than 75 it will be B.
# If the Percentage is 60+ and less than 70 it will be C. If the percentage is 50+ and
# less than 60 it will be D. If the percetage is 40+ and less than 50 it will be E. The
# Grade must be displayed on the result which is shown below.
# *******************************************************************
# Name : <Student Name>
# Roll No : <Roll No>                     Standard: <Standard>
# *******************************************************************
# Subject   Total Marks   Passing Marks    Obtained Marks   Result
# <Sub 1>     100           40            <obtained marks>  <result>
# <Sub 1>     100           40            <obtained marks>  <result>
# <Sub 1>     100           40            <obtained marks>  <result>
# *******************************************************************
# TOTAL     <total>      <total>              <total>
# Result: PASS / FAIL                    Percentage: <percentage>
# Grade : <Obtained Grade>




class Student:

    Name = False
    Reg_No = False
    Roll_No = False
    Standard = False
    Admission_Year = False
    Marks = []
    Results = False

    def __init__(self, name, reg_no, roll_no, standard, admission_year):
        try:
            if name.isalpha():
                self.Name = name
            if reg_no.isalnum():
                self.Reg_No = reg_no
            if roll_no.isdigit():
                self.Roll_No = roll_no
            if standard.isdigit():
                self.Standard = standard
            if admission_year.isdigit():
                self.Admission_Year = admission_year
        except:
            raise Exception ("Enter element in string")

    def addMarks(self, marks):
        if list(marks.values())[0] > 0 and list(marks.values())[0] <= 100:
            if list(marks.values())[0] < 40:
                marks['Result'] = 'Fail'
            else:
                marks['Result'] = 'Pass'

            self.Marks.append(marks)
        else:
            print("marks not in range")

    def results(self):
        for ele in self.Marks:
            if ele['Result'] == 'Fail':
                self.Results = 'Fail'

            if self.Results != 'Fail':
                self.Results = 'Pass'

        print('************************************************************************************************')
        print("Name: ", self.Name)
        print("Roll No: ", self.Roll_No,  "              Standard: ", self.Standard)
        print('************************************************************************************************')
        print("Subject", end="       ")
        print("Total Marks", end="  ")
        print("Passing Marks ", end="  ")
        print("Obtained Marks", end="    ")
        print("Result")

        total_passing = 0
        total_obtained = 0
        total_total = 0
        for el in self.Marks:
            print(list(el.keys())[0], end="  ")
            print(100, end="          ")
            print(40, end="               ")
            print(list(el.values())[0], end="            ")
            print(el['Result'])
            total_passing += 40
            total_total += 100
            total_obtained += list(el.values())[0]

        print('************************************************************************************************')

        print("Total", end="             ")
        print(total_total, end="         ")
        print(total_passing, end="              ")
        print(total_obtained, end="         ")


        print("\nResult:", self.Results, end="       ")
        percentage=(total_obtained * 100) / total_total
        if self.Results=="Pass":
            print("\t\t\t\t\t\t\tPercentage: ",percentage)
        else:
            print("\t\t\t\t\t\t\tPercentage:--")
        def grade(self):
            if self.Results=="Fail":
                print("Grade : F")
            elif percentage>95:
                print("Grade : O+")
            elif percentage>90 and percentage<=95:
                print("Grade : O")
            elif percentage>85 and percentage<=90:
                print("Grade : A+")
            elif percentage>80 and percentage<=85:
                print("Grade : A")
            elif percentage>75 and percentage<=80:
                print("Grade : B+")
            elif percentage>70 and percentage<=75:
                print("Grade : B")
            elif percentage>60 and percentage<=70:
                print("Grade : C")
            elif percentage>50 and percentage<=60:
                print("Grade : D")
            else:
                print("Grade : E")

        grade(self)
x = Student('Inam', "201809590008554spu", "55", '10', '2018')
x.addMarks({"maths\t\t\t": 65})
x.addMarks({"English\t\t\t": 20})
x.addMarks({"Gujarati\t\t": 38})

x.results()


