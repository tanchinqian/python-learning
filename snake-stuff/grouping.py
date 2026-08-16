words = ["apple", "bat", "car", "banana", "dog", "kiwi"]

# Expected output:
# {
#     5: ["apple"],
#     3: ["bat", "car", "dog"],
#     6: ["banana"],
#     4: ["kiwi"]
# }

def group_by_length(words):
  temp_dict = {}
  for word in words:
     length = len(word)
     if length not in temp_dict:
       temp_dict[length] = []
     temp_dict[length].append(word)
  print(temp_dict)
group_by_length(words)