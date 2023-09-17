#https://learn.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
#To determine whether a year is a leap year, follow these steps:

#If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#The year is a leap year (it has 366 days).
#The year is not a leap year (it has 365 days).

def is_leap(year):
    leap = False
    if((year > 1900) and (year <= 10 ** 5)):
        if(year %4 == 0):
            if(year %100 ==0 ):
                if(year %400 ==0 ):
                    return True
                else:
                    return False
            else:
                return True   
        else:
            return False
                
            

    # Write your logic here
    
    return leap

