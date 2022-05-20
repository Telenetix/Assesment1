import collections

with open("customerdata.txt", 'r',
          encoding='utf-8') as customers_file:
    data_list = customers_file.readlines()

data_list.pop(0)

def totalAmount():
    total_amount = 0
    for each in data_list:
        total_amount += int(each[-4:])
    return total_amount


def customers(orders):
    customers_names_list = []
    for each in data_list:
        customers_names_list.append(each[24:-5].replace(",", ""))
        orders_collection = collections.Counter(customers_names_list)

    customers_list = []
    if orders>=5:
        for user, order_status in orders_collection.items():
            if order_status >= orders:
                customers_list.append(user)
    else:
        for user, order_status in orders_collection.items():
            if order_status == orders:
                customers_list.append(user)

    return customers_list



with open('output.txt', 'w') as output_file:
    output_file.write("\n\t\tAssesment 1 By TELENETIX groups \n \t\t--------------------------------\n")
    output_file.write(
        "1. Total number of orders site received are " '{}/-\n'.format(len(data_list))) 
    output_file.write(
        "\n2. Total amount of the orders is " '{}/-\n'.format(totalAmount()))
    output_file.write("\n3. Distribution of customers who ordered exactly once, exactly twice, and so on up to 4 orders and group the rest as 5 orders and above.\n")
    output_file.write("\nList of customers who ordered exactly once \n")
    output_file.write(', '.join(customers(1)) + '\n')
    output_file.write("\nList of customers who ordered exactly twice \n")
    output_file.write(', '.join(customers(2)) + '\n')
    output_file.write("\nList of customers who ordered exactly thrise \n")
    output_file.write(', '.join(customers(3)) + '\n')
    output_file.write("\nList of customers who ordered exactly four times \n")
    output_file.write(', '.join(customers(4)) + '\n')
    output_file.write("\nList of customers who ordered more tham four times \n")
    output_file.write(', '.join(customers(5)) + '\n')
    output_file.write("\n\t\t\tOrders \t Count of Customers  \n")
    output_file.write("\t\t\t 1\t\t" '{} \n'.format(len(customers(1))))
    output_file.write("\t\t\t 2\t\t" '{} \n'.format(len(customers(2))))
    output_file.write("\t\t\t 3\t\t" '{} \n'.format(len(customers(3))))
    output_file.write("\t\t\t 4\t\t" '{} \n'.format(len(customers(4))))
    output_file.write("\t\t\t>4\t\t" '{} \n'.format(len(customers(5))))
    output_file.write("\t\t|Total customers|      " '{} '.format(len(customers(1))+len(customers(2))+len(customers(3))+len(customers(4))+len(customers(5))))