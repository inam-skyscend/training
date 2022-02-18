class Student:
    Name=False
    Reg_No=False
    Roll_No=False
    Standard=False
    Admission_year=False
    Marks = []
    Result = False

    def __init__(self,name,regno,rollno,standard,admissionyear):
        if name.isalpha():
            self.Name=name

        if regno.isalnum():
            self.Reg_No=regno

        if rollno.isdigit():
            self.Roll_No=rollno

        if standard.isdigit():
            self.Standard=standard

        if admissionyear.isdigit():
            self.Admission_year=admissionyear


    def add_marks(self,marks):
        if list(marks.values())[0]>0 and list(marks.values())[0]<=100:
            if list(marks.values())[0]<40:
                marks["Result"] = "Fail"
            else:
                marks["Result"] = "Pass"
            self.Marks.append(marks)
        else:
            print("you marks out of range,marks range should be 0 to 100")

    def result(self):
        for ele in self.Marks:

            if ele["Result"]=="Fail":
                self.Result="Fail"

            if self.Result!="Fail":
                self.Result="Pass"

        print('************************************************************************************************')
        print("Name: ",self.Name)
        print("Roll No: ",self.Roll_No, "              Standard: ",self.Standard)
        print('************************************************************************************************')
        print("Subject", end="       ")
        print("Total Marks", end="  ")
        print("Passing Marks ", end="   ")
        print("Obtained Marks", end="      ")
        print("Result")

        Total_Total=0       #Total of Total marks
        Total_Passing=0
        Total_obtained=0

        for el in self.Marks:
            print(list(el.keys())[0],end="")
            print(100,end="         ")
            print(40,end="                 ")
            print(list(el.values())[0],end=" \t\t\t ")
            print(el["Result"])
            Total_Total+=100
            Total_Passing+=40
            Total_obtained+=list(el.values())[0]

        print('************************************************************************************************')

        print("Total",end="\t\t\t\t")
        print(Total_Total,end="\t\t\t")
        print(Total_Passing,end="\t\t\t\t  ")
        print(Total_obtained,end="     ")


        print("\nResult: ", self.Result, end="       ")
        print("\t\t\t\t\t\t\t\tPercentage: ", (Total_obtained * 100) / Total_Total)


s=Student("Inamhusain","A457","57","12","2017")
s.add_marks({"maths\t\t\t\t": 45})
s.add_marks({"Physics\t\t\t\t": 23})
s.add_marks({"Chemistry\t\t\t": 89})
s.result()








