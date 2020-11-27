echo Computing max temperatures per year

for %%i in (C:\Users\yelad\Hadoop-MapReduce\ncdc\*) do python max_temperature_map.py < %%i | python max_temperature_reduce.py