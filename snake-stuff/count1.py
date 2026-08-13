
ex_list = ["apple","banana" ,"apple"]
def count_words(word_list):
##With this logic it must return a dictionary 
##By using this logic , we will use the key and store the value
##Python has the in operator that we can use
 temp = {}
 for item in word_list: 
    if item in temp:
      temp[item] += 1
    else:
      temp[item] = 1
    
 return temp

##final_result = count_words(ex_list)
##print(final_result)


## Max count finder
exp_dict = {"apple" : 2 , "banana" : 5 , "orange" : 1} ## Example dictionary
##Assumption made that the there is no negative values and the smallest is 0 



def find_max(dict_temp):
  
  max_item = None
  max_value = 0
  for item in dict_temp:
    if max_value < dict_temp[item]:
      max_value = dict_temp[item]
      max_item = item
      
      
  return  max_item , max_value

max_item , max_value = find_max(exp_dict)
###print(f'The maximum item is {max_item} with the count of {max_value}')

student_names = ["Alice", "Bob", "Charlie"]
student_scores = [85, 42, 90]

def generate_report(names,scores):
  status = ""
  for item , (name , status_amount) in enumerate(zip(student_names,student_scores)):
    if status_amount >= 50:
      status = "PASS"
    else:
      status = "FAIL"
      
    print(f'Rank {item + 1} : {name} - {status}' )


generate_report(student_names,student_scores)