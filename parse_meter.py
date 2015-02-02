#!/usr/bin/python

import sys
import csv
import time


def main():
    FILES = ['15m', 'daily', 'monthly']
    ZABBIX_HOST = 'Bespin'

    for file in FILES:
        with open('IntervalMeterUsage_{file}.csv'.format(file=file), 'rb') as fh:
            meter_csv_obj = csv.reader(fh)
            meter_csv_obj.next()
            with open('IntervalMeterUsage_{file}.txt'.format(file=file), 'w') as txt_out:
                if file == '15m':
                    for esiid, date, timestart, timeend, kwh, estact, congen in meter_csv_obj:
                        timestamp = time.mktime(time.strptime(' '.join((date, timestart)), '%Y-%m-%d %H:%M'))
                        txt_out.write('Bespin house.kwh.{file} {timestamp} {kwh}\n'.format(file=file, timestamp=timestamp, kwh=kwh))
                elif file == 'daily':
                    for esiid, date, reading_start, reading_end, kwh in meter_csv_obj:
                        timestamp = time.mktime(time.strptime(date, '%m/%d/%Y'))
                        if not kwh:
                            kwh = 0
                        txt_out.write('Bespin house.kwh.{file} {timestamp} {kwh}\n'.format(file=file, timestamp=timestamp, kwh=kwh))
                elif file == 'monthly':
                    for esiid, date_start, date, kwh, kwh_m, kwh_b, kva_m, kva_b in meter_csv_obj:
                        timestamp = time.mktime(time.strptime(date, '%m/%d/%Y'))
                        txt_out.write('Bespin house.kwh.{file} {timestamp} {kwh}\n'.format(file=file, timestamp=timestamp, kwh=kwh))
                else:
                    sys.exit()


if __name__ == '__main__':
    sys.exit(main())
