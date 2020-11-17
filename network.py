import time
import psutil

def main():
    old_valueDown = 0
    old_valueUp = 0    

    while True:
        new_valueDown = psutil.net_io_counters().bytes_recv
        new_valueUp = psutil.net_io_counters().bytes_sent

        if old_valueDown or old_valueUp:
            send_stat(new_valueUp-old_valueUp,new_valueDown - old_valueDown)
        old_valueDown = new_valueDown
        old_valueUp = new_valueUp

        time.sleep(1)

def convert_to_gbit(value):
    return round(value/125000,3)

def send_stat(valueUp, valueDown):
    print (f"Download:{convert_to_gbit(valueDown)}, Upload:{convert_to_gbit(valueUp)}")

main()