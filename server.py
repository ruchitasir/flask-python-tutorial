from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.flask_database


for_loop ={
    'name' : 'For-loop',
    'description' : 'The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal. \n In python there is “for in” loop which is similar to for each loop in other languages.',
    'syntax' : 'for iterator_var in sequence:\n statements(s)'
}

while_loop={
    'name' : 'While-loop',
    'description' : 'In python, while loop is used to execute a block of statements repeatedly until a given a condition is satisfied. And when the condition becomes false, the line immediately after the loop in program is executed.',
    'syntax' : 'while expression:\n statement(s)'
    
}

range_loop={
    'name' : 'For-Range-loop',
    'description' : 'We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).\n We can also define the start, stop and step size as range(start, stop, step_size).\n step_size defaults to 1 if not provided.',
    'syntax' : 'range(start, stop[, step]) or for i in range(2, 10, 2):\n  print(i)'
}

test_loop ={
    'name': 'test',
    'description': 'loop test'
}
floor_operator = {
  "name": "Floor Division",
  "description": "Division that rounds down to the nearest integer. Also known as integer division.",
  "symbol": "//",
  "example": "3 // 2 == 1",
  "uses": "A common situation we might see this operator is when we need to calcuate a \n  list index, which will need to be a whole number. For example, perhaps we are trying to  find the middle index of a list, but there are an even number of elements. In this case,  we could use floor division to select the leftmost element in the list by default."
}

add_operator = {
  "name": "Addition",
  "description": "Adds two numbers.",
  "symbol": "+",
  "example": "3 + 2 == 5",
  "uses": "In making a calculator, or even for string concatenation"
}
subtract_operator = {
  "name": "Subtraction",
  "description": "Subtract one number from another",
  "symbol": "-",
  "example": "3 - 2 == 1",
  "uses": "In making a calculator"
}


#loop_id =  db.loops.insert_one(for_loop).inserted_id
# db.loops.insert_many([ while_loop, range_loop])
# retrieved_loop = db.loops.find_one({"_id": loop_id})

# pprint.pprint(retrieved_loop)
# print('LOOP:', retrieved_loop['name'])

#query for several loops
print("Finding all loops :")
for loop in db.loops.find():
  pprint.pprint(loop)
print()

# db.operators.insert_many([ floor_operator, add_operator,subtract_operator])