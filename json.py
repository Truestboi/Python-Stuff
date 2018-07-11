survey_answers = {
    "DOB": "1966",
    "hometown": "Sussex",
    "age": "52",
    "name": "Murdoc"}

list_of_answers = [] #empty list to store dicitonaries

survey_q = [
  "What is your date of birth? ",
  "What is your hometown? ",
  "How old are you? ",
  "What is your name? "
]

survey_key = [
  'DOB',
  'hometown',
  'age',
  'name'
]

cont = input("Are you done recording information? (Y/N?) ")

#while 'n' in cont: #we wanna keep taking surveys:
    answers = {} #empty dictionary
    for x in range(len(survey_q)) :
      answer = input(survey_q[x])
      answers[survey_key[x]] = answer
    list_of_answers.append(answers)
    cont = input("Are you done recording information? (Y/N?) ")
    cont = cont.lower()

 #answer = "1966"
 #answers['DOB'] = '1966'
#print(list_of_answers)
