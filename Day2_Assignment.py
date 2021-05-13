#Name : Palak Singhania
#Topic : Day 2 Assignment

# Question 1 : Create 2 list with some brand names
list_of_clothing_brands = ["Louis Vuitton", "Fila", "Gucci", "House of Versace", "Nike"]

list_of_shoes_brands = ["Adidas", "Fila", "Puma", "Nike", "Woodland"]


# Question 2 : List of overlapping brand names in both lists

#Approach 1 : using simple for loop and if else statement
list_of_overlapping_brand=[]
for element in list_of_clothing_brands:
    if element in list_of_shoes_brands:
        list_of_overlapping_brand.append(element)
print("List of overlapping brands by simple approach: ", list_of_overlapping_brand)

#Approach 2 : efficient one
list_of_overlapping_brands = list(set(list_of_clothing_brands).intersection(list_of_shoes_brands))
print("List of overlapping brands by efficient approach: ", list_of_overlapping_brands)


# Question 3 : Print even numbers starting with 20 and ending with 40
print("All even numbers from to 40 are : ", end = " ")
for even_nums in range(20,41,2):
    print(even_nums, end = " ")