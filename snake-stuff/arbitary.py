'''
def build_query(table_name, *columns, **filters):
  col_str = " , ".join(columns) if columns else "*"
  query = f'SELECT {col_str} FROM {table_name}'
  
  if filters:
    filters = [f'{keys}={values}' for keys , values in filters.items()]
    query += " WHERE " + ' AND '.join(filters)
  return query
     
     
print(build_query("users", "name", "age", role="admin", status="active"))
print(build_query("orders", status="completed", total=100))
print(build_query("products", "id", "price"))

def format_names(*names):
  if names: 
    return "/".join(names)

  return "No Names Provided"

print(format_names("Alice", "Bob", "Charlie"))
print(format_names("David"))                   
print(format_names())         

              

def process_numbers(numbers):
  return [num ** 2 for num in numbers if num > 0 and num % 2 == 0 ]


print(process_numbers([1, 2, 3, 4, 5, 6]))     
print(process_numbers([-4, -2, 0, 2, 4]))         
print(process_numbers([1, 3, 5]))   

'''  

def clean_usernames(raw_names):
  return [names.strip().lower() for names in raw_names if len(names.strip()) >= 4 ]     

print(clean_usernames(["  Alice  ", "bob", "CHARLIE", "  ed  ", "Dan_99 "])) 
print(clean_usernames(["hi", "   ", "ok"]))