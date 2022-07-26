# finds the next row based on input row
def next_row(row):
    next_row=[1]
    for x in range(len(row)-1):
        next_row.append((row[x]+row[x+1])%2)
    next_row.append(1)
    return(next_row)

last_row = [1] # initial row

n = 15 # number of rows after initial

# prints the whole triangle with n+1 rows 
#print(last_row)
#for x in range(n):
#    last_row = next_row(last_row)
#print(last_row)

# initial values
num_odds = [1] #intializes empty
tot_odds = 1
tot_ele = 1
tot_per_row =[1]
row_percent = [1] 

for y in range(n):
    last_row = next_row(last_row)
    num_odds.append(sum(last_row))
    tot_odds = tot_odds + sum(last_row)
    tot_ele = tot_ele + len(last_row)
    tot_per_row.append(tot_odds/tot_ele)
    row_percent.append(sum(last_row)/len(last_row))

#print(num_odds) #prints counts of odds in each row
#print(row_percent) # prints row percents of odds per row
#print("total", tot_per_row) # prints cummulative percent in triangle
#print(tot_odds/tot_ele) #just gives whole triangle percent with n+1 rows 