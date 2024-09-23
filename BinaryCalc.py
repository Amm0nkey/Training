# bin1 = input('Enter a binary number: ')
# bin2 = input('Enter a second binary number: ')
def bin_bin(num1, num2):
    if len(num2) > len(num1):
      greater_num = num2
      lesser_num = num1
    else:
      greater_num = num1
      lesser_num = num2
    lesser_num = lesser_num.zfill(len(greater_num))
    counter = -1
    string1 = []

    for char in greater_num and lesser_num:
        num_to_compare = greater_num[counter]
        num_to_compare2 = lesser_num[counter]
        index_of_str1 = num_to_compare + num_to_compare2
        string1.append(index_of_str1)
        counter -= 1
    return string1    
def bin_add(num1, num2):
    bin_add_list = ''
    bincompare = bin_bin(num1, num2)
    carry = 0
    for pair in bincompare:
        if carry == 0:
            if pair == '11':
                bin_add_list += '0'
                carry = 1
            elif pair == '00':
                bin_add_list += '0'
                carry = 0
            else:
                bin_add_list += '1'
                carry = 0
        else:  
            if pair == '11':
                bin_add_list += '1'
                carry = 1
            elif pair == '00':
                bin_add_list += '1'
                carry = 0
            else:
                bin_add_list += '0'
                carry = 1
    if carry > 0:
        bin_add_list += '1'
    # print(bin_add_list[::-1])
    return bin_add_list[::-1]



# A	B	 A x B
# 0	0	  0
# 0	1	  0
# 1	0	  0
# 1	1	  1

str1 = '111' #29 # 145
str2 = '101' #5
counter = -1
counter2 = 0
final = []

for char in str1[::-1]:
  sum_var = ''
  string_of_8 = ''
  for char in str2[::-1]:
    num_to_compare = str1[counter]
    pair = char + num_to_compare
    if pair == '11':
      string_of_8 += '1'
    else:
      string_of_8 += '0'
  

  new_string = string_of_8 + '0' * counter2
  sum_var = bin_add(new_string, sum_var)
  final.append(new_string)
  counter -= 1
  counter2 += 1
# print(final)

sum_final = bin_add(final[0], final[1])

counter3 = 2
counter_max = final[-1]
while counter3 != final.index(counter_max) + 1:
  sum_final = bin_add(sum_final, final[counter3])
  counter3 += 1

print(sum_final)

# 01101010111