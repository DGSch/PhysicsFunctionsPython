train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  return ((f_temp - 32) * (5/9))
f100_in_celcius = f_to_c(100)
print(round(f100_in_celcius, 1))
def c_to_f(c_temp):
  return ((c_temp * (9/5)) + 32)
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
print("The GE train supplies", get_force(train_mass, train_acceleration), "Newtons of force.")

def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules.")

def get_work(mass, acceleration, distance):
  return (get_force(mass, acceleration) * distance)

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
