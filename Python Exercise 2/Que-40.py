# 40. Format a string with inputs passed using the index and keyword techniques.


# using index
name="hello everyone,my name is {0},currently i am intern at {1}"
res=name.format("inam","Skyscend Business solution pvt.ltd.")
print(res)




# using keyword technique
mail="""
To : {to}
Subject : {subject}

Hello {name},

Thank you for your interest in {company}.
congratulation,you are selected as {Role} in {company}.

"""

compose=mail.format(to="inamhusain2001@gmail.com",subject='training',name="inamhusain",company="Skyscend Business Solution Pvt.Ltd.",Role="intern")
print(compose)