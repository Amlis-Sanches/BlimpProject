
def main():
    ...


def buoyant_force(pd: float = None, V: float = None, g: float = 9.8, Fb: float = None) -> float:
    '''
    Using the buoyant force equation, we calculate a variable within this function without hardcoding
    every possible equation. If one input is missing, the function will determine how to calculate it.
    Buoyant Force Equation: Fb = ρ × V × g

    :param Fb: Buoyant force in Newtons (N)
    :param pd: Density of the surrounding fluid in kilograms per cubic meter (kg/m³)
    :param V: Volume of displaced fluid in cubic meters (m³)
    :param g: Acceleration due to gravity in meters per second squared (m/s²)
    :return: The value of the missing variable
    '''

    # Create a dictionary of variables
    variables = {'Fb': Fb, 'pd': pd, 'V': V, 'g': g}

    # Identify which variable is missing
    missing_vars = [var for var, value in variables.items() if value is None]

    # Check that exactly one variable is missing
    if len(missing_vars) != 1:
        raise ValueError("Exactly one variable must be None (the unknown to solve for).")

    # Check that provided values are positive numbers
    if any(value is not None and value <= 0 for value in variables.values()):
        raise ValueError("All provided values must be positive numbers.")

    missing_var = missing_vars[0]

    # Use match-case to calculate the missing variable
    match missing_var:
        case 'Fb':
            result = variables['pd'] * variables['V'] * variables['g']
            return result
        case 'pd':
            result = variables['Fb'] / (variables['V'] * variables['g'])
            return result
        case 'V':
            result = variables['Fb'] / (variables['pd'] * variables['g'])
            return result
        case 'g':
            result = variables['Fb'] / (variables['pd'] * variables['V'])
            return result
        case _:
            raise ValueError(f"Unknown variable '{missing_var}' to solve for.")



def igl1(P:int|float = None, V:int|float = None,n:int|float = None, R:int|float = 8.3145, T:int|float = None) -> int|float:
    '''
    This is a function to determine the varables of the ideal gas law for a gass.
    :param P: This is the pressure of the gas (Pa)
    :type P: int
    :param V: Volume of the object (m³)
    :type V: int
    :param n: This is the number of moles of the gas (mol)
    :type n: int
    :param R: Universal gas constant (J/(mol·K))
    :type R: int
    :param T: This is the temperature of the gas (K)
    :type T: int
    '''
    #check which variable is the one we are solving for.
    variable:dict = {'P':P,'V':V,'n':n,'R':R,'T':T}
    missing_vars:list = [var for var, value in variable.items()if value is None]
    #count the items in the list that are none. if more than 1 return error
    if len(missing_vars) != 1:
        raise ValueError("More than one variable is None")
    
    #check that the values are positive
    if any(value is not None and value <= 0 for value in [P,V,n,R,T]):
        raise ValueError("All provided values must be positive numbers.")
    
    #set the missing variable
    missing_var:str = missing_vars[0]

    match missing_var:
        case 'P':
            result = (n*R*T)/(V)
            return result
        case 'V':
            result = (n*R*T)/(P)
            return result
        case 'n':
            result = (P*V)/(R*T)
            return result
        case 'R':
            result = (P*V)/(n*T)
            return result
        case 'T':
            result = (P*V)/(n*R)
            return result


def igl2(pd:int|float = None,P:int|float = None, M:int|float = None, R:int|float = 8.3145, T:int|float = None) -> int|float:
    """
    This is a function to determine the varables of the ideal gas law for a gass.
    :param pd: This is the dencity of the gas ()
    :type pd: int
    :param M: Molar mass of the fluid (kg/mol)
    :type M: int
    :param R: Universal gas constant (J/(mol·K))
    :type R: int
    :param T: This is the temperature of the gas (K)
    :type T: int
    """
    #check which variable is the one we are solving for.
    variable:dict = {'pd':pd, 'P':P,'M':M,'R':R,'T':T}
    missing_vars:list = [var for var, value in variable.items()if value is None]
    #count the items in the list that are none. if more than 1 return error
    if len(missing_vars) != 1:
        raise ValueError("More than one variable is None")
    
    #check that the values are positive
    if any(value is not None and value <= 0 for value in [pd,P,M,R,T]):
        raise ValueError("All provided values must be positive numbers.")
    
    #set the missing variable
    missing_var:str = missing_vars[0]

    match missing_var:
        case 'pd':
            result = (P*M)/(R*T)
            return result
        case 'P':
            result = (pd*R*T)/(M)
            return result
        case 'M':
            result = (pd*R*T)/(P)
            return result
        case 'R':
            result = (P*M)/(T*pd)
            return result
        case 'T':
            result = (P*M)/(pd*R)
            return result


def acceleration_core(
    F: float = None, m: float = None,
    v: float = None, u: float = None, a: float = None,
    t: float = None, s: float = None
) -> float:
    """
    Calculates the missing variable among force, mass, acceleration, initial velocity,
    final velocity, time, and displacement using Newton's Second Law and kinematic equations.

    Provide all variables except the one you want to solve for.

    :param F: Force (N)
    :param m: Mass (kg)
    :param v: Final velocity (m/s)
    :param u: Initial velocity (m/s)
    :param a: Acceleration (m/s²)
    :param t: Time (s)
    :param s: Displacement (m)
    :return: The value of the missing variable
    :raises ValueError: If the number of unknowns is not exactly one or if invalid values are provided.

    :example:
    >>> a = calculate_acceleration(F=10, m=2)
    >>> print(a)  # Output: 5.0
    """
    variables = {'F': F, 'm': m, 'v': v, 'u': u, 'a': a, 't': t, 's': s}
    missing_vars = [var for var, value in variables.items() if value is None]

    if len(missing_vars) != 1:
        raise ValueError("Exactly one variable must be None (the unknown to solve for).")

    # Check for negative values where not physically meaningful
    for var, value in variables.items():
        if value is not None and var in ['m', 't'] and value <= 0:
            raise ValueError(f"The value of '{var}' must be a positive number.")

    missing_var = missing_vars[0]

    # Solve for the missing variable
    if missing_var == 'F':
        if m is not None and a is not None:
            F = m * a
            return F
        else:
            raise ValueError("Insufficient data to solve for 'F' using F = m * a.")

    elif missing_var == 'm':
        if F is not None and a is not None and a != 0:
            m = F / a
            return m
        else:
            raise ValueError("Insufficient data to solve for 'm' or acceleration 'a' is zero.")

    elif missing_var == 'a':
        if F is not None and m is not None and m != 0:
            a = F / m
            return a
        elif v is not None and u is not None and t is not None and t != 0:
            a = (v - u) / t
            return a
        elif s is not None and u is not None and t is not None and t != 0:
            a = (2 * (s - u * t)) / (t ** 2)
            return a
        elif v is not None and u is not None and s is not None:
            a = (v ** 2 - u ** 2) / (2 * s)
            return a
        else:
            raise ValueError("Insufficient data to solve for 'a'.")

    elif missing_var == 'v':
        if u is not None and a is not None and t is not None:
            v = u + a * t
            return v
        elif u is not None and a is not None and s is not None:
            v = (u ** 2 + 2 * a * s) ** 0.5
            return v
        else:
            raise ValueError("Insufficient data to solve for 'v'.")

    elif missing_var == 'u':
        if v is not None and a is not None and t is not None:
            u = v - a * t
            return u
        elif v is not None and a is not None and s is not None:
            u = (v ** 2 - 2 * a * s) ** 0.5
            return u
        else:
            raise ValueError("Insufficient data to solve for 'u'.")

    elif missing_var == 't':
        if v is not None and u is not None and a is not None and a != 0:
            t = (v - u) / a
            return t
        elif s is not None and u is not None and a is not None:
            discriminant = u ** 2 + 2 * a * s
            if discriminant < 0:
                raise ValueError("No real solution for 't'.")
            v = discriminant ** 0.5
            t = (v - u) / a
            return t
        else:
            raise ValueError("Insufficient data to solve for 't'.")

    elif missing_var == 's':
        if u is not None and v is not None and t is not None:
            s = ((u + v) / 2) * t
            return s
        elif u is not None and a is not None and t is not None:
            s = u * t + 0.5 * a * t ** 2
            return s
        elif v is not None and a is not None and t is not None:
            s = v * t - 0.5 * a * t ** 2
            return s
        else:
            raise ValueError("Insufficient data to solve for 's'.")

    else:
        raise ValueError(f"Unknown variable '{missing_var}' to solve for.")


def calculate_momentum(
    p: float = None, m: float = None, v: float = None,
    J: float = None, F: float = None, t: float = None,
    v_i: float = None, v_f: float = None
) -> float:
    """
    Calculates the missing variable among momentum, mass, velocity, impulse, force, time interval,
    initial velocity, and final velocity using momentum and impulse equations.

    Provide all variables except the one you want to solve for.

    :param p: Momentum (kg·m/s)
    :param m: Mass (kg)
    :param v: Velocity (m/s)
    :param J: Impulse (N·s)
    :param F: Force (N)
    :param t: Time interval (s)
    :param v_i: Initial velocity (m/s)
    :param v_f: Final velocity (m/s)
    :return: The value of the missing variable
    :raises ValueError: If the number of unknowns is not exactly one or if invalid values are provided.

    :example:
    >>> p = calculate_momentum(m=2, v=5)
    >>> print(p)  # Output: 10.0
    """
    variables = {'p': p, 'm': m, 'v': v, 'J': J, 'F': F, 't': t, 'v_i': v_i, 'v_f': v_f}
    missing_vars = [var for var, value in variables.items() if value is None]

    if len(missing_vars) != 1:
        raise ValueError("Exactly one variable must be None (the unknown to solve for).")

    # Check for negative values where not physically meaningful
    for var, value in variables.items():
        if value is not None:
            if var in ['m', 't'] and value <= 0:
                raise ValueError(f"The value of '{var}' must be a positive number.")

    missing_var = missing_vars[0]

    # Solve for the missing variable
    if missing_var == 'p':
        if m is not None and v is not None:
            p = m * v
            return p
        else:
            raise ValueError("Insufficient data to solve for 'p' using p = m * v.")

    elif missing_var == 'm':
        if p is not None and v is not None and v != 0:
            m = p / v
            return m
        elif J is not None and v_f is not None and v_i is not None:
            m = J / (v_f - v_i)
            return m
        else:
            raise ValueError("Insufficient data to solve for 'm'.")

    elif missing_var == 'v':
        if p is not None and m is not None and m != 0:
            v = p / m
            return v
        else:
            raise ValueError("Insufficient data to solve for 'v' using v = p / m.")

    elif missing_var == 'J':
        if F is not None and t is not None:
            J = F * t
            return J
        elif m is not None and v_f is not None and v_i is not None:
            J = m * (v_f - v_i)
            return J
        else:
            raise ValueError("Insufficient data to solve for 'J'.")

    elif missing_var == 'F':
        if J is not None and t is not None and t != 0:
            F = J / t
            return F
        elif m is not None and v_f is not None and v_i is not None and t is not None and t != 0:
            F = m * (v_f - v_i) / t
            return F
        else:
            raise ValueError("Insufficient data to solve for 'F'.")

    elif missing_var == 't':
        if J is not None and F is not None and F != 0:
            t = J / F
            return t
        elif m is not None and v_f is not None and v_i is not None and F is not None and F != 0:
            t = m * (v_f - v_i) / F
            return t
        else:
            raise ValueError("Insufficient data to solve for 't'.")

    elif missing_var == 'v_i':
        if v_f is not None and J is not None and m is not None:
            v_i = v_f - (J / m)
            return v_i
        elif v_f is not None and a is not None and t is not None:
            v_i = v_f - a * t
            return v_i
        elif p is not None and m is not None:
            v_i = p / m
            return v_i
        else:
            raise ValueError("Insufficient data to solve for 'v_i'.")

    elif missing_var == 'v_f':
        if v_i is not None and J is not None and m is not None:
            v_f = v_i + (J / m)
            return v_f
        elif v_i is not None and F is not None and m is not None and t is not None:
            v_f = v_i + (F * t) / m
            return v_f
        elif v_i is not None and a is not None and t is not None:
            v_f = v_i + a * t
            return v_f
        else:
            raise ValueError("Insufficient data to solve for 'v_f'.")

    else:
        raise ValueError(f"Unknown variable '{missing_var}' to solve for.")


if __name__ == "__main__":
    main()
