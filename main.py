import math


def input_y_co_ordinate():
    y = float(input("Faka isilungelelanisi sika Y"))
    return y


def input_x_co_ordinates():
    x = float(input("Faka isilungelanisi sika X"))
    return x


def input_point_name():
    name = input("Faka igama lalendawo")
    return name


def input_radius():
    radius = float(input("Faka iradiyasi"))
    return radius


def cal_peri(rad):
    peri = 2*3.14*rad
    return peri


def cal_sur_area(ra):
    s_area = 3.14*ra**2
    return s_area


def det_in_out(x, y, radi):
    x_center = 0
    y_center = 0
    distance = math.sqrt((x-x_center)**2+(y-y_center)**2)
    if distance > radi:
        whe_in_out = "ngaphandle kwesekile"
    else:
        whe_in_out = "ngaphakathi kwesekile"
    return whe_in_out


def output(y_c, x_c, nme, pe, sa, whet):
    print("Iperimitha yalesekile ngu  ", pe)
    print("Isafesi eriya yalesekile ngu  ", sa)
    print("Lendawo ingu",nme,"(",x_c,",",y_c,")", "ifakwe ngumntu i", whet)


if __name__ == '__main__':
    y_co = input_y_co_ordinate()
    x_co = input_x_co_ordinates()
    name = input_point_name()
    rads = input_radius()
    per = cal_peri(rads)
    s_ar = cal_sur_area(rads)
    whether = det_in_out(x_co, y_co, rads)
    output(y_co, x_co, name, per, s_ar, whether)




