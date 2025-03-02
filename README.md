# LAC3204
LAC3204 is a course offered by NUS, called Chinese for Business & Social Sciences. There are some idioms taught in class and they will be tested. The pdf of the collated list of idioms taught in each lesson will be uploaded after the lesson. However, it might be abit troublesome for one to create flashcards using the pdf，so I wrote this python script to make the process easier. The Python script `Extract idioms.py` is designed to extract the text, then create and insert the text into a text file in your folder.

I have already extracted all the sentences and definitions from the pdf and place them in this [Quizlet Folder](https://quizlet.com/user/do_well_for_Alevel/folders/lac3204?i=1x1jo7&x=1xqt) for your convenience. But you can use the Python file for your extraction if that is what you prefer. 

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
4. Check the contents in the text file because occasionally there are missing or additional empty lines between the sentence and definition

## Word of caution
1. The code works for my semester but it might not work for yours, if the lecturer change the style of the pdf

## Possible improvements
1. Create a webapp where the user will get the text file after uploading the idioms pdf (for people that don't know how to code)
2. Write code to extract the idioms in each sentence, a possible way is to use the china-idiom package. https://github.com/sfyc23/China-idiom 

