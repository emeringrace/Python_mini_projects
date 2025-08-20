def roots(x):
    if type(x) != str:
        raise ValueError('Invalid input type. Expecting a String.')
    if 'x2' not in x:
        raise ValueError('Not a Quadratic equation.')
    if ',' in x:
        raise ValueError('Invalid Equation.')
    y = ''
    for i in x:
        if i.isnumeric() or i in ['x','-','+','.']:
            y += i
    a = y[:y.index('x')]
    b = 0
    if a == '':
        a = 1
    else:
        a = float(a)
    y = y[y.index('x')+2:]
    if 'x' in y:
        b = y[:y.index('x')]
        if b == '+':
            b = 1
        elif b == '-':
            b = -1
        else:
            b = float(b)
        y = y[y.index('x')+1:]
    if y == '':
        c = 0
    else:
        c = float(y)
        
    d = b**2 - 4*a*c
    if d<0:
        raise ValueError('Roots are Complex.')
    elif d == 0:
        return [-1*b/(2*a)]
    else:
        return [round((-1*b + d**0.5)/(2*a),3),round((-1*b - d**0.5)/(2*a),3)]
