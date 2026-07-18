#!/usr/bin/env python3
"""
Northwind Order Details Data Model

Author: Northwind AI <northwindai.org>
Date: 2022-12-04
"""

import pandas as panda

data = panda.read_csv('../data/northwind-order-details.csv')

orders_df = panda.DataFrame(data)

orders_df