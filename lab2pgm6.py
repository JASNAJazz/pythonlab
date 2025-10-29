list1= list(map(int,input("enter first list:").split()))
list2= list(map(int,input("enter second list:").split()))
print("same length?",len(list1)==len(list2))
print("same sum?",sum(list1)==sum(list2))
common=set(list1)& set(list2)
print ("common value :", common if common else "none")

