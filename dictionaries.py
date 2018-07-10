#pythondictionaries
#Declare a dictionary with known values
import yay.json
jsonData = '{"DOB" : "1966",
"hometown": "Sussex",
"age": "52",
"name": "Murdoc"}'
jsonToPython = json.loads(jsonData)

#key : value, only one to one like only one y to one x
span_eng = {
  'hola' : 'hello',
  'gato' : 'cat',
  'mujer' : 'woman'
}

saying = input("Say a word in Spanish and I will translate: ")
#Assign a variable to the value related to the key 'hola'
word = span_eng[saying]
#searches dictionary for saying
print(word)

#declare an empty dicitonary
users = {}

#Add a key and value pair to the dictionary
identity = input("What is your name?")
users['Diana'] = 30
users['Yeet'] = 10000
print (users[identity])
print (users['Yeet'])
