#quiz game in python program
#create a dictionary that stores questions and answers
#have a variable that tracks the score of the player
#loop through the dictionary using the key value pairs
#display each question to the user and allow them to answers
#tell them if they are right or wrong
#show user the final result when quiz is completed

print("Welcome to the quiz!")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()
print ("Okay! Let's play :)")
print ("")

quiz = {
    "question1": {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    },
    "question2": {
        "question": "What is the capital of Philippines?",
        "answer": "Manila"
    },
    "question3": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question4": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question5": {
        "question": "What is the capital of Kenya?",
        "answer": "Nairobi"
    },
    "question6": {
        "question": "What is the capital of Norway?",
        "answer": "Oslo"
    },
    "question7": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question8": {
        "question": "What is the capital of Sweden?",
        "answer": "Stockholm"
    }, 
    "question9": {
        "question": "What is the capital of Colombia?",
        "answer": "Bogota"
    },
    "question10": {
        "question": "What is the capital of Finland?",
        "answer": "Helsinki"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input ('Answer? ')
    
    if answer.lower() == value['answer'].lower():
        print ('Correct!')
        score = score + 1
        print ('Your score is ' + str(score))
        print ("")
        print ("")
      
    else:
        print('Wrong!')
        print ('The answer is : ' + value['answer'])
        print ('Your score is ' + str(score))
        print("")
        print("")
        
print ("You got " + str(score) + " out of 10 questions correctly!")
print ("Your percentage is " +str(int(score/10*100)) + "%")


     
