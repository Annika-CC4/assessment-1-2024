# Declare a dictionary to easily access keys for question and values for checking the corredt answer.

country_capital={'France':'Paris','Denmark':'Copenhagen', 'Hungary':'Budapest','Ireland': 'Dublin','Russia':'Moscow',
  'Romania':'Bucharest', 'Monaco':'Monaco','Luxembourg': 'Luxembourg City', 'Netherlands': 'Amsterdam', 'Greece':'Athens'} 


for key, value in country_capital.items(): # for-loop to iterate each key-value pair in the dictionary.
    capital = input(f"What is the capital of {key}?\n" ).capitalize()  # capital variable to ask user for the answer. {key} to iterate for each questions.
   

    if capital != value:  # if-else condition to check if the input matches the value in the dictionary.
        print(f"Incorrect, the correct answer is {value}.")  #{value} to show the correct capital on the screen.
    
    
    else:
        print("Your answer is correct!") 
