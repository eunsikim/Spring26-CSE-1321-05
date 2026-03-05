# In physics you have learned this formula: Distance = Velocity * Time
# With this, we can also figure out the formula for Velocity and Time:
# Velocity = Distance / Time and Time = Distance / Velocity
# Create three functions that takes in 2 parameters and return the 
# result of each of the functions mentioned above.
def get_distance(v, t):
    return v * t

def get_velocity(d, t):
    return d / t

def get_time(d, v):
    return d / v

# Create a function that takes in three parameters which will represent
# Distance, Velocity, and Time. These parameters should be optional, with
# the default value of `None`.
# The function figures out what is the missing value and calls the corresponding
# function.
# For example: If you have Velocity and Time, then the function calls `get_distance()`
# Lastly, the function returns a string that includes the unknown part and its
# calculated value.
# For example: `"Distance: 40"`

def calculate_vdt(velocity=None, distance=None, time=None):
    res = ""

    if velocity == None:
        res += f"Velocity: {get_velocity(distance, time)}"
    elif distance == None:
        res += f"Distance: {get_distance(velocity, time)}"
    else:
        res += f"Time: {get_time(distance, velocity)}"

    return res

print(calculate_vdt(distance=5, time=6)) # Velocity
print(calculate_vdt(velocity=5, time=6)) # Distance
print(calculate_vdt(velocity=5, distance=6)) # Time