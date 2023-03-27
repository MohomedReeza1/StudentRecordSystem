# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1867161
# Date: 08/12/2021

#Part 4 - Text File

#creating list
marks = [0,20,40,60,80,100,120]
store = []

#creating variables
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

n = 0


while True:
    def inputs(message,error_message = 'Integer required'):
        while True:
            try:
                input_value = int(input(message))
                if input_value not in marks:
                    print('Out of range')
                    continue
            except ValueError:
                print(error_message)
                continue
            break
        return input_value

    input_pass = inputs('\nEnter your total pass credits: ')
    input_defer = inputs('Enter your total defer credits: ')
    input_fail = inputs('Enter your total fail credits: ')
    



#Process
#Check the total
    if input_pass + input_defer + input_fail != 120:
        print('Total incorrect.')
        continue
    else:
        store.append(input_pass)
        store.append(input_defer)
        store.append(input_fail)
    
#function progress (1)      
    def progress(input_pass,input_defer,input_fail):
        result = 'Progress'
        store.append(result)
        print(result)
    
        global progress_count
        progress_count += 1
        return progress_count
        
#function trailer (2 to 3)
    def trailer(input_pass,input_defer,input_fail):
        result = 'Progress (module trailer)'
        store.append(result)
        print(result)
        
        global trailer_count
        trailer_count += 1
        return trailer_count

#function retriever (4 to 14), (16 to 19), (22 to 25)
    def retriever(input_pass,input_defer,input_fail):
        result = 'Do not progress – module retriever'
        store.append(result)
        print(result)
        
        global retriever_count
        retriever_count += 1
        return retriever_count
        
#function exclude (15), (20 to 21), (26 to 28)
    def exclude(input_pass,input_defer,input_fail):
        result = 'Exclude'
        store.append(result)
        print(result)
        
        global exclude_count
        exclude_count += 1
        return exclude_count
        
#function call progress (1)
    if input_pass == 120:
        progress(input_pass,input_defer,input_fail)
        
#function call trailer (2 to 3)        
    if (input_pass == 100) and (input_defer in marks[0:2]) and (input_fail in marks[0:2]):
        trailer(input_pass,input_defer,input_fail)
        
#function call retriever (4 to 14), (16 to 19), (22 to 25)
    if (input_pass in marks[0:5]) and (input_defer in marks[0:]) and (input_fail in marks[0:4]):
        retriever(input_pass,input_defer,input_fail)
        
#function call exclude (15), (20 to 21), (26 to 28)
    if (input_pass in marks[0:3]) and (input_defer in marks[0:3]) and (input_fail in marks[4:]):
        exclude(input_pass,input_defer,input_fail)
  

    print('\nWould you like to enter another set of data?')
    
    choice = input("Enter 'y' for yes or 'q' to quit and view results: ")

    if choice.lower() == 'q':
        break
    
    else:
        continue


#Histogram
   
print('\n------------------------------------------------------------')
print('Horizontal Histogram:\n')

print('Progress', progress_count,' :', '*' * progress_count)
print('Trailer', trailer_count,'  :', '*' * trailer_count)
print('Retriever', retriever_count,':', '*' * retriever_count)
print('Excluded', exclude_count,' :', '*' * exclude_count,'\n')

#total outcomes
total_outcomes = progress_count + trailer_count + retriever_count + exclude_count
print(total_outcomes,'outcomes in total.')
print('------------------------------------------------------------')



#Vertical Histogram

print('Vertical Histogram:\n')

#This code is implemented from the website,
#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops

outcome = ['Progress', 'Trailer', 'Retriever', 'Excluded']

print(' '.join(outcome))

for x in range(max(progress_count, trailer_count, retriever_count, exclude_count)):
    print("   {0}        {1}        {2}        {3}".format(
        '*' if x < progress_count else ' ',
        '*' if x < trailer_count else ' ',
        '*' if x < retriever_count else ' ',
        '*' if x < exclude_count else ' '
    ))

print('\n')
print(total_outcomes,'outcomes in total.')
print('------------------------------------------------------------')


#printing the stored data from the list
print('Printing the stored data from the list:\n')

index_range = total_outcomes * 4

while n < index_range:
    print(store[n+3],'-',str(store[n])+',',str(store[n+1])+',',store[n+2])
    n += 4
    
print('------------------------------------------------------------')


#Part 4 - Text File
print('Printing the stored data from the text file:\n')

try:
    file = open('file.txt', 'w')

    n = 0
    index_range = total_outcomes * 4
    while n < index_range:
        file.write(str(store[n+3]))
        file.write(' - ')
        file.write(str(store[n])+', ')
        file.write(str(store[n+1])+', ')
        file.write(str(store[n+2])+'\n')
        n += 4
        
    file.flush()
    file.close()

    file = open('file.txt', 'r')
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print('File not found. Please check if the file exists in the folder')
