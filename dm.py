import os
import urllib2

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


def download(url, n):
    path = 'D:\work\YJH\ChinaMap'
    file_name = r'map%s.osm' % n
    dest_dir = os.path.join(path, file_name)
    has_dir = os.path.exists(dest_dir)
    if has_dir:
        return
    f = urllib2.urlopen(url)
    data = f.read()
    with open(dest_dir, "wb") as code:
        code.write(data)


if __name__ == '__main__':
    while True:
        error_count = 0
        longitude_l = 73.4
        latitude_t = 53.33
        n = 1
        while latitude_t >= 17.6:
            while longitude_l <= 134.73:
                try:
                    url = 'https://Overpass-api.de/api/map?bbox=%s,%s,%s,%s' % (
                        longitude_l, latitude_t - 0.5, longitude_l + 0.5, latitude_t)
                    print 'Being processed...'
                    print url + ' %s' %n
                    download(url, n)
                    n += 1
                    longitude_l += 0.5
                except:
                    f = open('ExceptionUrl_test.txt', 'a')
                    print 'Exception...'
                    error_count += 1
                    f.write(url + ' %s' %n + '\n')
                    longitude_l += 0.5
                    n += 1
            latitude_t -= 0.5
            longitude_l = 73.4
        print 'success'
        if error_count == 0:
            break
    print 'Finally successful!!!'