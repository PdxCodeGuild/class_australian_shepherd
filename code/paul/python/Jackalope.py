jackalope_age = 0
jackalope_count = 2
years = 0
def age(jackalope_age, jackalope_count, years):
    while jackalope_age > 10:
        jackalope_age += 1
        if jackalope_age >= 4 and jackalope_age <= 8:
            jackalope_count += 2
           
        print('count', jackalope_count)
        if jackalope_age == 10:
            jackalope_count -= 2
        print('jackalope age is: ', jackalope_age)
        if jackalope_count > 1000:
            return years
        years += 1
        print('count', jackalope_count)
        
            
    # else:
    #     return jackalope_count
print(years)
age(jackalope_age, jackalope_count, years)



# age = 0
# j = ['a', 'a']
# while age < 10:
#     age += 1
#     print(age)
#     if age >= 4 and age <= 8:
#         j.append('a')
#         print(j)
