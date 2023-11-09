
def weight_2d(D, L, W, H, G=9.81):
    """
    Calculate the weight of a 2d object
    D = Density in kg/m³
    L = Lenght in meters
    W = Width in meters
    H = Height in meters
    G = Gravity
    """
    result = D * L * W * H * G

    print(f"{round(result, 2)} N")

    return round(result)


def mass_total(*args, G=9.81):
    """"
    G = gravity (m/s)
    args = Weigths (N)
    """
    result = []

    total_w = sum(args)

    print(f"{total_w} N, {round(total_w / G, 2)} Kg")
    result.append(total_w)
    result.append(round(total_w / G))

    return result


def center_gravity(*args, Mt):
    """"
    args = Cx1, N1, Cx2, N2, ETC
    Mt = total weight (N)
    """
    result = 0
    for i in range(0, len(args) - 1, 2):
        result += args[i] * args[i + 1]

    cg = result / Mt

    print(f"{round(cg, 2)} m")

    return round(cg, 2)


def moment_of_inertia(W, w, L, G=9.81):
    """
    Io = (W / 12)(w² + L²)

    W = weight (N)
    w = width (meters)
    L = length (meters)
    """

    result = ((W / G) / 12) * (w ** 2 + L ** 2)

    print(f"{round(result, 2)} - s² - m")

    return round(result, 2)


def distance_from_body_center(Xcg1, Xcg, Ycg1, Ycg):
    result = ((Xcg1 - Xcg) ** 2) + ((Ycg1 - Ycg) ** 2)

    print(f"{round(result, 2)} m²")

    return round(result, 2)


def parallel_axis_theorem(Io, m, d, G=9.81):
    """
    Icg  = Io + md2

    Io = Inercia calculada em moment_of_inertia()
    m = Massa em N
    d = distancia calculada em distance_from_body_center()
    G = gravidade

    """ 

    result = Io + m / G  * d

    print(f"{round(result, 2)} N − s² − m")

    return round(result, 2)


if __name__ == "__main__":

    ## For the example, assuming a 2d car with a fuel tank and a driver
    # Car                         | Driver (seated)               | Fuel
    # Length = 4.70 m             | Length = 0.90 m               | Length = 0.50 m
    # Width = 1.80 m              | Width = 0.50 m                | Width = 0.90 m
    # Height = 1.25 m             | Height = 1.10 m               | Height = 0.30 m
    # Weight = 17,500 N           | Weight = 850 N                | Density of fuel = 750 kg/m3
    # Centroid = (30.5, 30.5) m   | Centroid = (31.50, 31.00) m   | Centroid = (28.00, 30.50) m

    # Peso do tanque de combustivel
    w_fuel_tank = weight_2d(750, 0.5, 0.9, 0.3)

    # massa total do carro
    m_total = mass_total(17500, 850, w_fuel_tank)

    # centro de gravidade eixo x
    x_cg = center_gravity(30.5, 17500, 31.5, 850, 28.0, 993, Mt=m_total[0])

    # centro de gravidade eixo y
    y_cg = center_gravity(30.5, 17500, 31.0, 850, 30.5, 993, Mt=m_total[0])

    # inercia do carro
    i_o_car = moment_of_inertia(17500, 1.8, 4.7)

    # inercia do motora
    i_o_motora = moment_of_inertia(850, 0.5, 0.9)

    # inercia do tanque combustivel
    i_o_comb = moment_of_inertia(w_fuel_tank, 0.9, 0.5)

    # Encontra a distancia do centro de cada objeto do centro de gravidade do corpo
    dist_car = distance_from_body_center(30.5, x_cg, 30.5, y_cg)
    dist_driver = distance_from_body_center(31.5, x_cg, 31.0, y_cg)
    dist_fuel = distance_from_body_center(28.0, x_cg, 30.5, y_cg)

    # parallel axis theorem
    icg_car = parallel_axis_theorem(i_o_car, 17500, dist_car)
    icg_driver = parallel_axis_theorem(i_o_motora, 850, dist_driver)
    icg_fuel = parallel_axis_theorem(i_o_comb, w_fuel_tank, dist_fuel)

    icg_total = icg_car + icg_driver + icg_fuel
    #print(f"Total inertia for the car: {icg_total} N – s2 – m")
    print("\n " * 2)
    print("-" * 80)
    print(f"| {'Property':<50} | {'Computed value':<20}    |")
    print("-" * 80)
    print(f"| {'Total mass (weight)':<50} | {m_total[1]} Kg {m_total[0]} N         |")
    print(f"| {'Combined center of mass location':<50} | (x,y) = {x_cg}m, {y_cg}m  |")
    print(f"| {'Mass moment of inertia':<50} | {icg_total} N – s² – m       |")
    print("-" * 80)

