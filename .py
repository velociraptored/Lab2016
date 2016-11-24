import math
m = .01651
mErr = .006
l = .646
lErr = .002
g = 9.8
gErr = .01
theta = [.52, .35, .17, .70, .87, 1.05]
thetaMax = [.5864, .3747, .2005, .6565, .806, .971]
thetaMaxErr = [.0007427, .0005028, .0003488, .0008688, .001462, .002365]
angVelo = [2.238, 1.44, .78, 2.49, 3.012, 3.550]
angVeloErr = [.001539, .00019499, .00136, .003276, .002339, .003456]

t = [1.7, 1.6, 1.6, 1.68, 1.7, 2.62]
tErr = [.031819, .03182, .028284, .007071, .028284, .003536]
sTheta = [2.2601, 2.2385, 2.2257, 2.2911, 2.3320, 2.384]
sErr = .0017453

# for k in range(6):
#    newErr = ((mErr*.5*(l**2)*(angVelo[k]**2))**2 + (lErr*l*m*angVelo[k]**2)**2 + (angVeloErr[k]*m*l**2*angVelo[k])**2)**(1/2)
#    print(newErr)
# print()
total = 0
ert = 0
for k in range(6):
    ke = .5 * m * l ** 2 * angVelo[k] ** 2
    u = m * g * l * (1 - math.cos(thetaMax[k]))
    err = ((((mErr * .5 * (l ** 2) * (angVelo[k] ** 2)) ** 2 + (lErr * l * m * angVelo[k] ** 2) ** 2 + (angVeloErr[k] * m * l ** 2 * angVelo[k]) ** 2) ** (1 / 2) * u) ** 2 + (((sErr * 2 * 2 ** (1 / 2) * (g / l) ** (1 / 2)) ** 2 + (lErr * (-(2) ** (1 / 2) * sTheta[k]) / ((g / l) ** (1 / 2) * l ** 2)) ** 2 + (gErr * ((2) ** (1 / 2) * sTheta[k]) / ((g / l) ** (1 / 2) * l)) ** 2) ** (1 / 2) * ke) ** 2) ** (1 / 2)
    print(ke / u)
    print(err)
    ert += err
    total += ke / u
print (total / 6)
print(ert / 6)
# print()
# for k in range(6):
    # newErr = ((mErr*g*l*(1-math.cos(thetaMax[k])))**2 + (gErr*m*l*(1-math.cos(thetaMax[k])))**2 + (lErr*m*g*(1-math.cos(thetaMax[k])))**2+ (thetaMaxErr[k]*m*g*l*math.sin(thetaMax[k]))**2)**(1/2)
    # print(newErr)


print()

# for k in range(6):
    # print(m*g*l*(1-math.cos(thetaMax[k])))
#    newErr= ( (sErr * 2 * 2**(1/2) * (g/l)**(1/2) )**2 + (lErr * (-(2)**(1/2) * sTheta[k])/ ((g/l)**(1/2) * l**2))**2 + (gErr * ((2)**(1/2) * sTheta[k])/ ((g/l)**(1/2) * l))**2  )**(1/2)
#    print(newErr)
# print()

# for k in range(6):
#    print(2*(2*l/g)**(1/2) * sTheta[k])

# for k in range(6):
#    print(sTheta[k])

