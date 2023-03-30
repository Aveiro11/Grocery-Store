from sql_connection import get_sql_connection
from datetime import datetime


def insert_order(connection, order):
    cursor = connection.cursor()
# orders
    order_query = ('INSERT INTO orders(name,total,date) VALUES(%s,%s,%s)')
    order_data = (order['name'], order['total'],datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_detail_query = (
        'INSERT INTO order_details(order_id, product_id, quantity, total_cost) VALUES(%s,%s,%s,%s)')

    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_cost'])
        ])

    cursor.executemany(order_detail_query, order_details_data)
    connection.commit()
    return order_id

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (order_id,name,date,total) in cursor:
        response.append({
            'order_id': order_id,
            'name': name,
            'date': date,
            'total': total,
        })

    cursor.close()

    # append order details in each order
    # for record in response:
    #     record['order_details'] = get_all_orders(connection, record['order_id'])

    return response

if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(insert_order(connection, {
    #     'name': 'wahid',
    #     'total': '500',
    #     'order_details': [
    #             {
    #                 'product_id': 2,
    #                 'quantity': 2,
    #                 'total_cost': 20
    #             },
    #         {
    #                 'product_id': 3,
    #                 'quantity': 1,
    #                 'total_cost': 40
    #                 }
    #     ]
    # }))
