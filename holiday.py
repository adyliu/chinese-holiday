#/usr/bin/env python3
#-*- encoding:utf-8 -*-
#http://sousuo.gov.cn/s.htm?t=paper&advance=true&title=%E8%8A%82%E5%81%87%E6%97%A5%E5%AE%89%E6%8E%92

from datetime import date,timedelta
from itertools import chain
import sys

holiday_map={'元旦':(20160101,20170101,20170102),
    '春节':(20160207,20160208,20160209,20160210,20160211,20160212,20160213,20170127,20170128,20170129,20170130,20170131,20170201,20170202),
    '清明节':(20160404,20170402,20170403,20170404),
    '劳动节':(20160501,20160502,20170501,),
    '端午节':(20160609,20160610,20160611,20170528,20170529,20170530),
    '中秋国庆':(20160915,20160916,20160917,20161001,20161002,20161003,20161004,20161005,20161006,20161007,20171001,20171002,20171003,20171004,20171005,20171006,20171007,20171008)
    }
work=(20160206,20160214,20160612,20160918,20170122,20170204,20170401,20170527,20170930,20161008,20161009)

holidays=[*chain(*holiday_map.values())]

def _int(d): return d.year*10000+d.month*100+d.day


def build_year(years:list):
    min_day,max_day=date(years[0],1,1),date(years[-1],12,31)
    ret=[]
    today=min_day
    while today <= max_day:
        day_value=_int(today)
        if day_value in holidays or (day_value not in work and today.isoweekday() > 5):
            ret.append(day_value)
        today+=timedelta(days=1)
    return ret


if __name__ == '__main__':
    years = [int(x) for x in sys.argv[1:]]
    if years:
        ret =build_year(years)
        print('size =',len(ret))
        import json
        with open('holiday.json','w') as f:
            f.write(json.dumps(ret))
        with open('holiday.txt','w') as f:
            f.write('\n'.join(map(str,ret)))
        print(ret)