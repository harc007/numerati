import math

def get_pearson_correlation(x, y):
    if len(x) == len(y):
        if type(x) is tuple or type(x) is list:
            mean_x = sum(x)/len(x)
        else:
            return None
        if type(y) is tuple or type(y) is list:
            mean_x = sum(x)/len(x)
        else:
            return None
        num = 0
        den_x = 0
        den_y = 0
        for i range(len(x)):
            num += (x[i]-mean_x)*(y[i]-mean_y)
            den_x += math.pow((x[i]-mean_x), 2)
            den_y += math.pow((y[i]-mean_y), 2)
        return num/(math.pow(den_x, 0.5)*math.pow(den_y, 0.5)
    else:
        return None


def get_cosine_similarity(x, y):
    if len(x) == len(y):
        if type(x) is tuple or type(x) is list:
            mean_x = sum(x)/len(x)
        else:
            return None
        if type(y) is tuple or type(y) is list:
            mean_x = sum(x)/len(x)
        else:
            return None
        num = 0
        den_x = 0
        den_y = 0
        for i in range(len(x)):
            num += x[i]*y[i]
            den_x += math.pow(x[i], 2)
            den_y += math.pow(y[i], 2)
        return num/(math.pow(den_x, 0.5)*math.pow(den_y, 0.5)
    else:
        return None
