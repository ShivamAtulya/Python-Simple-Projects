wel=("WELCOME IN MY KBC")
welocme=wel.center(200)
print(welocme)
name=input("Tell your Good Name Sir!")
print("Welcome in my game ", name , "Sir!")
print("Rules: PLEASE DON'T USE PHONE AND GIVE ONLY OPTION OF CORRECT ANSWER")
print("Lets Start the game")
questions=[
    """What is the chemical symbol for water?
    A) O2
    B) H2O
    C) CO2
    D) NaCl""",
    """Which is the smallest prime number?
    A) 0
    B) 1
    C) 2
    D) 3""",
    """ What is the largest planet in our solar system?
    A) Earth
    B) Mars
    C) Jupiter
    D) Saturn""",
    """What is the square root of 64?
    A) 6
    B) 7
    C) 8
    D) 9""",
    """What is the most abundant gas in the Earth's atmosphere?
    A) Oxygen
    B) Nitrogen
    C) Carbon Dioxide
    D) Hydrogen""",
    """What is the boiling point of water at sea level?
    A) 50°C
    B) 75°C
    C) 100°C
    D) 120°C""",
    """Who is known as the "Father of Computers"?
    A) Alan Turing
    B) Charles Babbage
    C) Bill Gates
    D) Steve Jobs""",
    """What is the capital city of Japan?
    A) Seoul
    B) Beijing
    C) Tokyo
    D) Bangkok""",
    """What is the process of converting water vapor into liquid water called?
    A) Condensation
    B) Evaporation
    C) Precipitation
    D) Sublimation""",
    """Who is the author of the book "1984"?
    A) Aldous Huxley
    B) George Orwell
    C) Ray Bradbury
    D) J.R.R. Tolkien""",
    """Who painted the Mona Lisa?
    A) Vincent van Gogh
    B) Pablo Picasso
    C) Leonardo da Vinci
    D) Michelangelo"""]
choice=["B","C","C","C","B","C","B","C","A","B","C"]
prize=0
i=0
for i in range(len(questions)):
 print(f"Q{i+1}: {questions[i]}")
 answer=(input("Enter your answer:"))
 if answer==choice[i]:
    print("Correct")
    prize=prize+100
    print("Your Winning Prize is Rs",prize)
 else:
    print("Wrong")
    print("Your Winning Prize is Rs",prize)
    print("HAHAHA Aapke sath Prank hua h aapko paisa nai milega...You will 5 Star Chocolate")
    print("Thank you for playing :)")
    break