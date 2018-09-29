'''
To run this program: 
    python main.py https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD
'''
import sys
import downloader
import all_tasks

# Get the url from the cmd line.
if __name__ == '__main__':
    _, url = sys.argv

# Download the file.
file_name = downloader.download(url)

print(all_tasks.task_1(file_name))
print(all_tasks.task_2(file_name))
print(all_tasks.task_3(file_name))
print(all_tasks.task_4(file_name))
print(all_tasks.task_5(file_name))


