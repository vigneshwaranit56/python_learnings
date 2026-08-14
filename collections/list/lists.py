nums = [10,230,30,40,50]

# append() method adds an element at the end of the list

nums.append(60)

print(f"List after appending 60: {nums}")

nums.pop(1) # pop by index 1
nums.pop() # pop last element

print(f"List after popping elements: {nums}")


nums.remove(30) # remove by value

print(f"list of  elements after removing 30: {nums}")


nums.insert(1,20) # insert 20 at index 1
print(f"list after inserting 20 at index 1: {nums}")

nums.insert(3,100)
print(f"list before sorting: {nums}")

nums.sort() # in place sorting  with orignal list get changed

nums.sort(reverse = True) # in place sorting reverse order

sorted_nums = sorted(nums,reverse = True)
 # sorted() method returns a new list and original 
 # list remains unchanged

print(f"list of sorting elements in reverse order: {sorted_nums}")


print(f"list after sorting: {nums}")

nums.reverse()

print(f"List after reversing:{nums}")

