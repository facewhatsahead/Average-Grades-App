userName = input('What is your name?')
syllabus = input("What was your score for this?")
midTerms = input("What did you get for the midterms?")
finalExam = input("What did you get on the final exam?")
totalPoints = syllabus + midTerms + finalExam
gradeAverage = totalPoints/3
print("Hello " +userName +"  Your average score was: "+gradeAverage)