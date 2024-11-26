pip install findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext(appName = " ")
sc

from pyspark.sql import SparkSession
from pysprak.sql.functions import *

spark = SparkSession.builder.getOrCreate()
