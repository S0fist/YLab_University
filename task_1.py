def domain_name(url):
    url = url.split('//')[-1]
    url = url.split('/')[0]
    url = url.split('.')[-2]
    return url
