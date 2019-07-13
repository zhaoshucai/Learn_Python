from datetime import datetime, timedelta

now = datetime.now()
five_time = now - timedelta(days=5)

time_file_name = 'save_five_time_' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.txt'
time_file = open(time_file_name,'w')
time_file.write(str(five_time))
time_file.close()