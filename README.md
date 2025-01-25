# LAC3204
LAC3204 is a course offered by NUS, called Chinese for Business & Social Sciences. There are some idioms taught in class and apparently they will be tested. The pdf of the collated list of idioms taught in each lesson will be uploaded after the lesson. However, it might be abit troublesome for one to create flashcards using the pdf，so I wrote this python script to make the process easier. The Python script extract the text, then create and insert the text into a text file in your folder.

## Extracted content
The text file content will look like this:

Sentence containing Idiom

Definition of Idiom

Empty Line

Sentence containing Idiom

Definition of Idiom

.

.

.

## How to run the code
I assume that you have something that you can use to edit the Python file.
1. Change the filepath stated in the python file to the filepath of the file that you want to extract from
2. State the filepath where you want to save the text file to 
3. Run the Python file

## Word of caution
1. The code works for my semester but it might not work for yours, if the lecturer change the style of the pdf

## Possible improvements
1. Create a webapp where the user will get the text file after uploading the idioms pdf (for people that don't know how to code)
2. Write code to extract the idioms in each sentence, a possible way is to use the china-idiom package. https://github.com/sfyc23/China-idiom 

