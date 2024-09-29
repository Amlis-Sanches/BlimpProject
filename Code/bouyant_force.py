
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


if __name__ == "__main__":
    main()
