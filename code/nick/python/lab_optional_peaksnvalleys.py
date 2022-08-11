# Lab Optional Peaks and Valleys

# Define the following functions:
# peaks(data) - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# valleys(data) - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# peaks_and_valleys(data) - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# peak
def peaks(index):
    order = 1
    for p in (index [1:(index_length-1)]): 
        if p > (index[order-1]) and p > (index[order+1]):
            peak_indicies.append(order)
        order += 1
    print(peak_indicies)
    

#valley
def valleys(index):
    order = 1 
    for v in (index [1:(index_length-1)]): 
        if v < (index[order-1]) and v < (index[order+1]):
            valley_indicies.append(order)
        order += 1
    print(valley_indicies)

#peaks_and_valleys
def peaks_and_valleys(index):
    order = 1
    for data in (index [1:(index_length-1)]):  
        if data < (index[order-1]) and data < (index[order+1]):
            peaks_and_valleys_indicies.append(order)
        elif data > (index[order-1]) and data > (index[order+1]):
            peaks_and_valleys_indicies.append(order)
        order += 1
    print(peaks_and_valleys_indicies)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_indicies = []
valley_indicies = []
peaks_and_valleys_indicies = []
index_length = len(data)
peaks(data)
valleys(data)
peaks_and_valleys(data)

# Version 2
# Using the data list above, draw the image of X's above.
order = 0
for i in range(max(data)):
    visual_list = []
    for num in data:
        if num >= (max(data) - order):
            visual_list.append(' X')
        else:
            visual_list.append('  ')
    order += 1
    visual_line = ''.join(visual_list)
    print(visual_line)
order += 1

# Version 3
# Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. 
# Below the water is represented by ~'s. Given data, calculate the amount of water that would be collected, and if you can, draw the following diagram.

#add water
order = 0
amount_of_water = 0
for valley in valley_indicies:
    multiplier = valley_indicies[order] - peak_indicies[order]
    amount_of_water += (multiplier * (multiplier+1))/2
    order += 1
print(f'There are {amount_of_water} units of water.')

#add water visual
order = 0
for i in range(max(data)):
    visual_list = []
    for num in data:
        if num >= (max(data) - order):
            visual_list.append(' X')
        elif ' X' in visual_list:
            visual_list.append(' ~')
        else:
            visual_list.append('  ')
    order += 1
    visual_line = ''.join(visual_list)
    print(visual_line)
order += 1