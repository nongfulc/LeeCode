from datetime import datetime

DATE_FORMAT = ''
if __name__ == '__main__':
    while True:
        print(''' Please choose:  "1" for date to timestamp; "2" for timestamp to date; "q/Q" for quit.''')
        choice = input('Your choice: ')
        if '1' == choice:
            choice = input('Please enter the date(like 2020/12/12):')
            date = datetime.strptime(choice, '%Y/%m/%d')
            print(int(date.timestamp()))
        elif '2' == choice:
            choice = input('Please enter the timestamp:')
            date = datetime.fromtimestamp(float(choice))
            print(date.strftime('%Z %Y/%m/%d %H:%M:%S'))
        elif 'q' == choice or 'Q' == choice:
            break
        else:
            print('Please be serious')
