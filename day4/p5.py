def ram():
    from  collections import Counter
    list=[]
    n=int(input("ENTER Total Number Of Votes: "))
    for i in range(n):
               ele =input("Enter Candidate Name: ")
               list.append(ele) 
    print(list)
    vote_count=Counter(list)
    max_votes=max(vote_count.values())
    lst=[i for i in vote_count.keys() if vote_count[i]==max_votes]
    print(sorted(lst)[0]) 
ram()
