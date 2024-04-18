import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
env = os.environ.get('env')

import matplotlib.pyplot as plt
import numpy as np

from Database import DiskoverDB
from Utils import flow_logger, build_log_message, build_log_error


def most_sold():
     disks = []
     quantity = []
     result = DiskoverDB.sales.aggregate([{'$group': {'_id': '$product_id', 'quantity': {'$sum': '$quantity'}}}, {'$sort': {'quantity': 1}}, {'$limit': 10}])
     for order in result:
          disks.append(order['_id'])
          quantity.append(order['quantity'])

     fig, ax = plt.subplots(figsize=(6, 6))
     ax.barh(disks, quantity)
     plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
     ax.set_ylabel('Disks')
     ax.set_xlabel('quantity')
     ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
     ax.set_axisbelow(True)
     ax.minorticks_on()
     plt.xticks(np.arange(0, max(quantity)+1, 25))
     ax.bar_label(ax.containers[0], label_type='center', color='white')

     plt.tight_layout()
     plt.draw()
     plt.savefig('assets/most_sold.png')

def most_orders():
     disks = []
     orders = []
     result = DiskoverDB.sales.aggregate([{'$group': {'_id': '$product_id', 'orders': {'$count': {}}}}, {'$sort': {'orders': 1}}, {'$limit': 10}])
     for order in result:
          disks.append(order['_id'])
          orders.append(order['orders'])

     fig, ax = plt.subplots(figsize=(6, 6))
     ax.barh(disks, orders)
     plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
     ax.set_ylabel('Disks')
     ax.set_xlabel('# of Orders')
     ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
     ax.set_axisbelow(True)
     ax.minorticks_on()
     plt.xticks(np.arange(0, max(orders)+1, 5))
     ax.bar_label(ax.containers[0], label_type='center', color='white')

     plt.tight_layout()
     plt.draw()
     plt.savefig('assets/most_orders.png')

def revenue_generated():
     disks = []
     revenues = []
     result = DiskoverDB.sales.aggregate([{'$group': {'_id': '$product_id', 'revenue': {'$sum': '$revenue'}}}, {'$sort': {'revenue': 1}}, {'$limit': 10}])
     for disk in result:
          disks.append(disk['_id'])
          revenues.append(disk['revenue'])

     fig, ax = plt.subplots(figsize=(6, 6))
     ax.barh(disks, revenues)
     plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
     ax.set_ylabel('Disks')
     ax.set_xlabel('Revenues')
     ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
     ax.set_axisbelow(True)
     ax.bar_label(ax.containers[0], label_type='center', color='white')

     plt.tight_layout()
     plt.draw()
     plt.savefig('assets/revenues_generated.png')

def most_busy_dates():
     dates = []
     revenues = []
     result = DiskoverDB.sales.aggregate([{'$group': {'_id': {'$dateToString': {'format': "%Y-%m-%d", 'date': {'$toDate': '$date'}}}, 'revenue': {'$sum': '$revenue'}}}, {'$sort': {'revenue': 1}}, {'$limit': 10}])
     for disk in result:
          dates.append(disk['_id'])
          revenues.append(disk['revenue'])

     fig, ax = plt.subplots(figsize=(6, 6))
     ax.barh(dates, revenues)
     plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
     ax.set_ylabel('Disks')
     ax.set_xlabel('Revenues')
     ax.grid(which='major', color='#DDDDDD', linewidth=0.8)
     ax.set_axisbelow(True)
     ax.bar_label(ax.containers[0], label_type='center', color='white')

     plt.tight_layout()
     plt.draw()
     plt.savefig('assets/most_busy_dates.png')


def generate_plots(correlation_id):
     try:
          most_sold()
          flow_logger.info(build_log_message(correlation_id, 'Most sold plot generated'))
          most_orders()
          flow_logger.info(build_log_message(correlation_id, 'Most orders plot generated'))
          revenue_generated()
          flow_logger.info(build_log_message(correlation_id, 'Most revenue plot generated'))
          most_busy_dates()
          flow_logger.info(build_log_message(correlation_id, 'Most busy dates plot generated'))
     except Exception as e:
          flow_logger.error(build_log_error(correlation_id, e))