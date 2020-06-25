import speedtest as st
from datetime import date

x = 0.0
y = 0.0
z = 0.0

def get_new_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()
    ping = round(speed_test.results.ping,0)
    download = round(speed_test.download() / (10**6), 2)
    upload = round(speed_test.upload() / (10**6), 2)
    global x
    x = ping
    global y
    y = download
    global z
    z = upload
    return (True)

def save_speeds(ping, download, upload):
    today = date.today()
    line_out = '''
    --------------------------------------------------------------------------------\n
    Speed test ({0})\n
    Ping: {1} \n
    Download: {2} mbps \n
    Upload: {3} mbps\n
    --------------------------------------------------------------------------------
    '''.format(str(today),(ping),(download),(upload))
    with open("outputs/speeds.txt", "a+") as file:
        file.write(line_out)
    return (True)

def main():
    if get_new_speeds():
        if save_speeds(x,y,z):
            print("complete")
            return 0
    print("failed")
    return -1

main()
