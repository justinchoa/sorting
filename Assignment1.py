
# name:Justin Choa Jia Jun  Admin no.:214239F


blank = []
holiday_value=[{'Package Name': 'Malaysia', 'Customer Name': 'john', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'vietnam', 'Customer Name': 'manny', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'Singapore', 'Customer Name': 'goh', 'Number of Pax': 30,'Package cost': 30 },
 {'Package Name': 'Iceland', 'Customer Name': 'rem', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'Greenland', 'Customer Name': 'shivani', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'Canada', 'Customer Name': 'kenny', 'Number of Pax': 30,'Package cost': 30 },

            ]

temp=[{'Package Name': 'Malaysia', 'Customer Name': 'john', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'vietnam', 'Customer Name': 'manny', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'Singapore', 'Customer Name': 'goh', 'Number of Pax': 30,'Package cost': 30 },
 {'Package Name': 'Iceland', 'Customer Name': 'rem', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'Greenland', 'Customer Name': 'shivani', 'Number of Pax': 30,'Package cost': 30 },
{'Package Name': 'Canada', 'Customer Name': 'kenny', 'Number of Pax': 30,'Package cost': 30 },  ]       #MeatShield


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # sorting by using simultaneous assignment in python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

while True:
    x= input("Are u a admin? (Y/N)? :")

    for list in holiday_value:
            if x == "Y":

                print(*holiday_value, sep = "\n" )
            break
    y= input(" want to sort? :")
    if y == 'Y':
        print('1. Display all records',
              '2. Sort record by Customer Name using Bubble sort',
              '3. Sort record by Package Name using Selection sort',
              '4. Sort record by Package Cost using Insertion sort',
              '5. Search record by Customer Name using Linear Search and update record',
              '6. Search record by Package Name using Binary Search and update record',
              '7. List records range from $X to $Y. e.g $100-200',
              'Exit Application', sep="\n")
    z=input("choice: ")
    if z == "1":

        results = []
        for item in holiday_value:
            results.append(item['Customer Name'])
            bubble_sort(results)
        print('After Bubble sorting Customer Name : {}'.format(results))

        break
