import numpy as np

def m_generate(x, y, count=1):
    a = np.random.randint(0, 10, (x, y, count))
    m = '\n'.join([''.join(['{:4}'.format(*item) for item in row]) for row in a])
    return m

def cicrle_len(rad):
    try:
        return 2*np.pi*rad
    except TypeError:
        try:
            return 2*np.pi*float(rad)
        except ValueError:
            print("Аргумент должен быть числом!")
            exit()