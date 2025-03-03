
from time import time

ts = time()
te = time()

def tstart():
    ts = time()

def tend(ts=ts):
    te = time()
    print("Time: " + str(te - ts))
    ts = time()
    te = 0

def tprint(ts=ts,te=te):
    print("Time: " + str(te-ts))

tstart()
import random as rand
import matplotlib.pyplot as plt
from numpy import pi, arccos, sin, cos, e, sqrt, cbrt, inf
import numpy as np
from scipy.integrate import quad
from math import dist
import os
os.chdir("insert")
tend()

seed = 42
rand.seed(seed)


#hubbleconstant = 2.27e-18 * 3.1536e16
#norm47k = 0.0311534911945
#norm9b = 0.163992409278
#norm13b = 0.372359037352

h0 = 1/14.39
Om_r = 3*10**(-5)
Om_s = 0
Om_d = 0.69
Om_m = 1 - Om_r - Om_d

def scale_fac_integral(a):
    #return a / sqrt(Om_r + Om_m * a + Om_s * a ** 2 + Om_d * a ** 4)
    return a * (Om_r + Om_m * a + Om_d * a ** 4) ** -0.5

def time_from_scale_factor(a):
    integ_a = quad(scale_fac_integral, 0, a)[0]
    return integ_a / h0


def time_from_inv_scale_factor(a):
    return time_from_scale_factor(1/a)

def light_has_travelled(a):
    tsx = time()
    integ_l = quad(time_from_inv_scale_factor, 1/a, inf)[0]
    tex = time()
    #print("Time: "+ str(tex - tsx))
    return integ_l + time_from_scale_factor(a) / a

def light_will_travel(a):
    tsx = time()
    integ_l = quad(time_from_inv_scale_factor, 0, 1/a)[0]  
    tex = time()
    #print("Time: "+ str(tex - tsx))
    return integ_l - time_from_scale_factor(a) / a

Rad_OU = light_has_travelled(1)
Rad_AU = light_will_travel(1)
Rad_EOU = Rad_OU + Rad_AU

tstart()
A1 = [0.000001 * 1.005 ** i for i in range(5001)]
tend()
T1 = [time_from_scale_factor(i) for i in A1]
tend()
#L1 = [light_has_travelled(i) for i in A1]
print()

def scale_factor_from_time(t, printit=False):
    for i in range(len(T1)):
        tthis = T1[i]
        if T1[i] >= t: 
            break
    tlast = T1[i-1]
    if printit: print(t, tlast, tthis, i)
    tpos = (t - tlast) / (tthis - tlast)

    athis = A1[i]
    alast = A1[i-1]
    
    ainter = alast + (athis - alast) * tpos
    return ainter

def scale_factor_from_time2(t):
    last_a = 1
    this_a = last_a
    lower_b = 0
    upper_b = 10**5
    test_t = time_from_scale_factor(this_a)
    for i in range(20):
        last_a = this_a
        if test_t > t:
            upper_b = last_a
        elif test_t < t:
            lower_b = last_a
        else: 
            break
            
        this_a = (upper_b + lower_b)/2
        test_t = time_from_scale_factor(this_a)
    return this_a

def comoving_distance_covered(t1,t2):
    a1 = scale_factor_from_time(t1)
    a2 = scale_factor_from_time(t2)
    return light_has_travelled(a2) - light_has_travelled(a1)






#tstart()
#print(time_from_scale_factor(1))
#tend()
print(light_has_travelled(1))
#tend()
#print(scale_factor_from_time2(150))
#tend()
#print(scale_factor_from_time(150))
#tend()

loaded_arrays = np.load("sophonce_grabby_arrays.npz")

#a = -13.776870135
ts = time()

a = time_from_scale_factor(1)


t1 = [10**(i/100 - 1) for i in range(511)] #601
#t1 = loaded_arrays["array1"]

#file = open("sophonce_grabby_arrays.txt", "w+")
#np.savetxt("sophonce_grabby_arrays.txt", np.asarray(t1))
#print(loadedarr == t1)
te = time()
tprint(ts,te)

ts = time()

l1 = [6.684811689019187*10**(-20),8.061618789801031*10**(-20),9.72283181385984*10**(-20),1.1727421265776268*10**(-19),1.4146642659695055*10**(-19),1.7066599097149255*10**(-19),2.0591371832623048*10**(-19),2.4846754675661987*10**(-19),2.9984926782929523*10**(-19),3.6189670203595236*10**(-19),4.368371097934492*10**(-19),5.273612732616156*10**(-19),6.367208433515277*10**(-19),7.688633046940116*10**(-19),9.285625750878794*10**(-19),1.1215749590429476*10**(-18),1.3548982975062567*10**(-18),1.6370138007888338*10**(-18),1.978190847432306*10**(-18),2.3908385860604998*10**(-18),2.88997237299945*10**(-18),3.4939094535228064*10**(-18),4.224809292747192*10**(-18),5.10955639017277*10**(-18),6.180737701472222*10**(-18),7.477598124990973*10**(-18),9.048329605480852*10**(-18),1.095121343785946*10**(-17),1.3257047246363789*10**(-17),1.605186234566326*10**(-17),1.9440238729030578*10**(-17),2.3548116097235852*10**(-17),2.8530368963185284*10**(-17),3.4574846650307864*10**(-17),4.19100444360782*10**(-17),5.0814122049235656*10**(-17),6.162582966414296*10**(-17),7.475787153417853*10**(-17),9.07104718737965*10**(-17),1.100956954720962*10**(-16),1.3366114609455082*10**(-16),1.6231761177545633*10**(-16),1.9717668218768986*10**(-16),2.3959561838821117*10**(-16),2.9123240644070625*10**(-16),3.5411334261881423*10**(-16),4.307119609710619*10**(-16),5.240473290879019*10**(-16),6.378307280377433*10**(-16),7.765977333168811*10**(-16),9.45904097244843*10**(-16),1.1525588381133342*10**(-15),1.40491152752177*10**(-15),1.7132066172262117*10**(-15),2.0900208141994244*10**(-15),2.550802947590065*10**(-15),3.1144938830686645*10**(-15),3.8044411155707556*10**(-15),4.649373496255712*10**(-15),5.684648565062731*10**(-15),6.953840151082758*10**(-15),8.5106768405624*10**(-15),1.042143429805032*10**(-14),1.2767975324059547*10**(-14),1.565144605773071*10**(-14),1.9196943759205132*10**(-14),2.3559226641573156*10**(-14),2.8929808109990364*10**(-14),3.5546453334087533*10**(-14),4.3704044342739556*10**(-14),5.376849437470518*10**(-14),6.61949459778761*10**(-14),8.154943628732926*10**(-14),1.0053679411896163*10**(-13),1.2403585087673206*10**(-13),1.5314189805897682*10**(-13),1.8922458366768325*10**(-13),2.3399562634957345*10**(-13),2.8959737031259107*10**(-13),3.5871303131441687*10**(-13),4.447107329189049*10**(-13),5.518205402832082*10**(-13),6.853591170000043*10**(-13),8.520243665946287*10**(-13),1.0602581841270326*10**(-12),1.3207170174992047*10**(-12),1.6468709961970107*10**(-12),2.0557704856946324*10**(-12),2.569032710332626*10**(-12),3.2140846496262943*10**(-12),4.02581870292964*10**(-12),5.0486540233983625*10**(-12),6.339230534217926*10**(-12),7.969914039331318*10**(-12),1.0033297513011217*10**(-11),1.2648059992295012*10**(-11),1.5966615431553343*10**(-11),2.0184902237709097*10**(-11),2.55555886833286*10**(-11),3.24048292852813*10**(-11),4.115455861994745*10**(-11),5.2351716829778904*10**(-11),6.670668129207139*10**(-11),8.514410895125194*10**(-11),1.088701682843887*10**(-10),1.3946162129992468*10**(-10),1.7898431676007755*10**(-10),2.30150794111105*10**(-10),2.9653279709647623*10**(-10),3.828429368682394*10**(-10),4.953139937451538*10**(-10),6.422120900609571*10**(-10),8.345283010272159*10**(-10),1.0869153165267096*10**(-9),1.4189605463352373*10**(-9),1.8569154799839518*10**(-9),2.436070987460951*10**(-9),3.2039992274012146*10**(-9),4.225042635559471*10**(-9),5.586465991960105*10**(-9),7.407002031638172*10**(-9),9.848694389679707*10**(-9),1.3133410024706491*10**(-8),1.7566025110941693*10**(-8),2.3566878720790468*10**(-8),3.171754981176478*10**(-8),4.282560769421572*10**(-8),5.8016606642065456*10**(-8),7.886526000650934*10**(-8),1.0758247716700233*10**(-7),1.4728654073113622*10**(-7),2.0239264173144207*10**(-7),2.791786006036307*10**(-7),3.86609167441094*10**(-7),5.375437229687024*10**(-7),7.505130000971068*10**(-7),0.0000010523466020050637,0.0000014820658635125167,0.0000020967173054479785,0.0000029801293523773606,0.000004256121316250038,0.000006108601609921404,0.000008812176971713452,0.000012779236345294605,0.00001863272444296896,0.00002731927031407382,0.00004028637805919578,0.000059761210876060116,0.00008919320842063014,0.0001339595277033687,0.00020248042185031095,0.0003079142988646556,0.0004707839165068726,0.0007230884272093609,0.0011116672635513565,0.0017145988136556295,0.002641764329949506,0.004041862603180467,0.006240327465856346,0.009501825466889935,0.01429284975249987,0.02172199659569168,0.033437221561950524,0.04855475703185494,0.07087696966712961,0.10453241975987627,0.15631868383102318,0.2238027326589306,0.31024437601695803,0.4311857930254432,0.6040258702381218,0.8567915842720891,1.1910716316208627,1.5660600671305442,2.0491556482958053,2.6813053346172637,3.525204546236174,4.67911001073746,6.217389439855831,7.800755362509868,9.711595873621933,12.035306858683526,14.895707508700246,18.47642075281134,23.058664618820607,29.08324007217899,35.19748169645357,42.14096940398522,50.17321920904668,59.51292894632716,70.46538432040552,83.47470801601939,99.20797720871185,118.69457346969935,137.89707849329787,162.94973342107008,188.23906968870048,216.58693088195025,248.45886521728238,284.49549160068756,325.5969941870868,373.1117239487735,429.08534655469333,495.95995682639676,561.821936311982,633.9498104740176,712.8939299372685,799.3150786609101,894.0720383496815,998.3077765120105,1113.6233314165554,1242.3512439068197,1388.0017396780856,1555.9994622377849,1743.3463217662397,1930.78997534918,2132.580369133143,2349.6383091702814,2576.0084035969326,2835.425539793858,3116.201355877982,3397.4636102421496,3715.5667609136535,4064.40629835587,4451.99599984596,4890.844554971883,5369.84970459676,5846.942319117664,6353.918365795557,6892.166482820755,7463.286512307963,8069.216388461649,8712.424456276012,9396.23889663002,10125.345845189488,10906.606485880016,11750.370848549372,12672.609729293325,13698.396236088875,14845.314326948683,15959.327571226591,17132.086441352076,18365.59871734508,19662.092669606376,21024.152177768407,22454.940798403375,23961.354207339344,25602.12079946273,27332.898688783418,29172.619049790894,31100.777229188294,33142.224104368266,35295.73008436079,37565.12280774317,40159.98972279326,42730.101503466176,45417.4595612326,48225.20508903869,51157.133751255256,54216.88858222767,57409.8459345771,60742.18162071362,64222.06712045883,67861.81833423412,71678.94670317479,75699.53938362963,79964.19141143614,84536.12227543666,89514.89531189694,95059.00312621891,100896.35247005576,106618.95367435715,112579.21534585848,118782.81086569339,125235.67750970062,131944.2333312963,138915.91534725833,146159.66564700357,153762.50518418752,161891.06762765156,170403.27244042535,179313.6039248731,188639.24336720508,198307.63657674805,208315.15031188968,218757.41032132632,230177.32211018057,241895.66705645286,254400.35900541343,268362.13548609207,282013.0294493884,296183.3016890641,310883.8031838036,326125.9695455156,341922.42201399634,358287.9259021368,375240.9043179534,392805.8183210829,411686.2145657179,431548.81609124725,452289.53192763514,473947.98891766334,496565.63331304723,520178.3702357468,544833.3417268512,570490.4057695131,597555.9846882218,627696.0223340837,658011.9253659344,689454.9454186031,722046.1338084759,755806.1038052414,790755.4011616602,826915.1466574838,864308.0973768608,902960.3533798627,939548.4434404303,982383.6647581499,1027050.7634919056,1073621.846990059,1122176.4118292856,1172792.4063447204,1225557.27238745,1280554.179955835,1337874.6651310748,1397608.717687785,1459858.583234893,1524724.1545534243,1592306.982540911,1662851.2747361693,1735862.9250968497,1812684.5378339533,1906715.452889967,1990845.2900622238,2077764.6253672352,2167511.064994099,2260124.1797352727,2355648.8673412977,2454140.7026713802,2549104.177127521,2659022.403071827,2773477.9211185817,2892571.675236246,3016518.6230066647,3145503.148949461,3279723.2196549573,3428188.069199863,3575372.9215767244,3727031.5898816558,3883614.059789626,4036690.4574073735,4206496.65080786,4383534.297095876,4567578.394549032,4758879.20940334,4999889.706911028,5211590.018312016,5429974.825125738,5655101.165669238,5887021.80393426,6125789.320201102,6349677.665051498,6611222.678384949,6859209.838134587,7140876.555870144,7433061.964371991,7736423.540599214,8053144.618804744,8379265.554797127,8720295.552904954,9073692.418201976,9439412.574546885,9821539.717528688,10217071.930238353,10627625.776710296,11053559.04461072,11541472.196845813,12003087.554656774,12430163.212231591,12924028.652661871,13436521.651880069,13967916.833913926,14518861.651647381,15256238.895037737,15854565.733332546,16469092.702997152,17099778.991946455,17746578.141906638,18278446.19897046,18987348.429303873,19721841.776624307,20482842.01831934,21270824.073128544,22191070.874634977,23040869.68398308,23807643.698956348,24713903.198745217,25651789.339435697,26622421.98462383,27626777.455584433,28665181.33976058,29740728.11283802,30852404.862910703,32001952.010575883,33190447.292687748,34418981.40939051,35688687.267850325,36999186.23213972,38356100.55460749,39756125.96274372,41201751.214703575,42694385.634144075,44480605.49748917,46070898.78670122,47465673.14314851,49713574.22579001,50902948.964418165,52702094.741481654,54556489.78728841,56467331.54934295,58435754.33268826,60462931.584832005,62549991.63118653,64698011.8388002,66908081.94622955,69181228.72260723,71518456.25538309,73920712.3265653,76388861.30738726,78923748.55016895,81526121.06494802,84196666.72419494,87502120.61515501,90313322.91151232,92622733.52750766,95570823.60463864,98588950.50008419,101677084.79910213,104835065.7582494,108062550.62730944,111358988.65210274,114723641.0106969,118155537.53769927,121653442.98409706,125215874.78559253,128841076.80318637,132526931.4848828,136271014.64597374,141633953.296731,145236203.74947506,147822616.18133986,151767725.4997246,155752535.42209828,159772383.3665449,165077924.2162752,169144155.20448798,171980771.2400783,176076379.85625997,180171546.95738652,184257046.9647783,188323981.50939238,192358685.63380682,196351806.83549258,200287792.20422044,204153463.1720596,207933028.12028,211609214.62621278,215164781.54040873,219219435.92361584,221830240.4309998,224885634.55475724,227750614.06916198,230348815.51076028,232718393.28649253,234771174.68844813,236491729.9843715,237844844.330619,238792072.43489948,241460394.75665402,241402377.21811795,238759881.067091,237631954.62606195,236662922.05684683,233374212.0565805,232479258.4824403,226030948.93087232,221040173.21596023,215057725.29276288,208006578.14723748,199798684.27014136,190340598.6688314,179531634.68221217,167265147.3945109,153426797.96238133,137894999.66604125,120540854.04209337,101225212.08556624,80117534.81268564,56110437.174979486,29993213.828879543,1258808.1736945442,7.94166837979795*10**(-17),5.711509036491679*10**(-50),5.939105147916485*10**(-78),2.804589671606358*10**(-115),1.5128971920629176*10**(-118),1.2715508671986047*10**(-167),4.809889608271023*10**(-172),1.4052697784875058*10**(-234),1.93774902600499*10**(-240),1.3189178109649872*10**(-246),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#l1 = loaded_arrays["array2"]

def R_GC_interpolate(t):
    if t <= 0.1 or t >= 10**5 : 
        return 0
    for i in range(len(t1)):
        if t1[i] == t:
            print(l1[i])
            return l1[i]
        elif t1[i] > t:
            break
    lot = t1[i-1]
    hit = t1[i]
    lol = l1[i-1]
    hil = l1[i]
    post = (t - lot) / (hit - lot)
    interl = (hil - lol) * post + lol
    #print(interl)
    #print(lot, hit)
    #print(lol, hil)
    return interl

print("Starting time is: " + str(t1[0]))
R_GC_interpolate(a)

#file.write("\n")
#file.write(str(np.asarray(l1)))
te = time()
tprint(ts,te)
#print(light_has_travelled(scale_factor_from_time(a, True)))
#print(scale_factor_from_time(a, True))
#print(a)
#print(scale_factor_from_time(time_from_scale_factor(1), True))
#print(scale_factor_from_time(time_from_scale_factor(0.15), True))
#print("YOOO")

ts = time()

#d1 = np.asarray([light_has_travelled(scale_factor_from_time(i)) for i in t1])
d1 = loaded_arrays["array3"]

#file.write("\n")
#file.write(str(d1))
te = time()
tprint(ts,te)
ts = time()

#d2 = d1.reshape(len(d1), 1)
#d3 = d1 - d2
d3 = loaded_arrays["array4"]

print("HEY + " + str(np.size(d3, 1)))

te = time()
tprint(ts,te)

np.savez("sophonce_grabby_arrays.npz", array1=t1, array2=l1, array3=d1, array4=d3)


file = open("sophonce_grabby_arrays.txt", "r")
#print(file.read())
#print("Time: " + str(te-ts))

def comoving_distance_list(t1,t2,T1=t1):
    t1_index = np.where(T1 == t1)
    t2_index = np.where(T1 == t2)
    return comoving_distance_list_index(t1_index,t2_index)

def comoving_distance_list_index(t1,t2,T1=t1,d1=d1):
    l1 = d1[t1]
    l2 = d1[t2]
    #print(l1, l2)
    return d3[t1, t2]

print(A1[220])
print(T1[220])
print(comoving_distance_covered(0.000001,13.8))
print(comoving_distance_list(t1[0],t1[400]))


class GC():
    def __init__(self, index, pos, pindex, time, tindex=0):
        self.index = index
        self.pos = pos
        self.pindex = pindex
        self.time = time
        self.tindex = tindex
        self.hutime = time - a
        self.ourad = OU_rads_dates[self.index]

    def comovingradius(self, time):
        return comoving_distance_covered(self.time, time)
        #costime = time - a
        #cosbtime = self.ctime
        #print(costime)
        #print(cosbtime)
        #if self.time >= a + 9.8:
        #    print("HAHAH")
        #    radius = (e ** (- self.ctime * hubbleconstant) - e ** (- costime * hubbleconstant)) / (hubbleconstant * norm13b)
        #    return radius
        #elif time < a + 9.8:
        #    radius = - 3 * (self.ctime ** (1/3) - costime ** (1/3)) / norm9b
        #    return radius
        #else: #takes into account shift from powerlaw expansion to exponential expansion of universe at t = 9.8 billion 
        #    radius1 = - 3 * (self.ctime ** (1/3) - 9.8 ** (1/3)) / norm9b
        #    radius2 = (e ** (- 9.8 * hubbleconstant) - e ** (- costime * hubbleconstant)) / (hubbleconstant * norm13b)
        #    return radius1 + radius2

    def comovingradius_list(self,time):
        return comoving_distance_list(self.time, time)
    
    def comovingradius_list_index(self,tindex):
        return comoving_distance_list_index(self.tindex, tindex)

icnum = 1.1309316874 * 10**9


def PointInSphere(radius):
    u = rand.random()
    v = rand.random()
    theta = u * 2.0 * pi
    phi = arccos(2.0 * v - 1.0)
    r = cbrt(rand.random()) * radius
    sinTheta = sin(theta)
    cosTheta = cos(theta)
    sinPhi = sin(phi)
    cosPhi = cos(phi)
    x = r * sinPhi * cosTheta
    y = r * sinPhi * sinTheta
    z = r * cosPhi
    return (x, y, z)

def PointInSphereCrude(radius):
    prad = radius * 2
    while prad > radius:
        rx = rand.random() * radius * 2 - radius
        ry = rand.random() * radius * 2 - radius
        rz = rand.random() * radius * 2 - radius
        prad = dist((rx, ry, rz), (0, 0, 0))
    #print("Radius: " + str(prad))
    return (rx, ry, rz)

l_randgx = []
l_randgy = []
l_randbx = []
l_randby = []

def randpdf(pdf, x1, x2, y1, y2):
    x3 = x1
    y3 = pdf(x3) + 1
    xr = x2 - x1
    yr = y2 - y1
    while True:
        x3 = rand.random() * xr + x1
        y3 = rand.random() * yr + y1
        if y3 >= pdf(x3):
            l_randbx.append(x3)
            l_randby.append(y3)
        else:
            l_randgx.append(x3)
            l_randgy.append(y3)
            return x3

def rand_GC_time(starttime=0.1, endtime=a):
    return randpdf(R_GC_interpolate, starttime, endtime, 0, 3*10**4)

def DistanceBetweenPoints(p1, p2):
    #tweenx = p2[0] - p1[0]
    #tweeny = p2[1] - p1[1]
    #tweenz = p2[2] - p1[2]
    #return sqrt(tweenx**2 + tweeny**2 + tweenz**2)
    return dist(p1,p2)

def IsPointInSphere(radius, spoint, point):
    dx = abs(point[0] - spoint[0])
    dy = abs(point[1] - spoint[1])
    dz = abs(point[2] - spoint[2])
    if dx > radius or dy > radius or dz > radius:
        return False
    elif sqrt(dx**2 + dy**2 + dz**2) > radius:
        return False
    else:
        return True
    
def VolumeOfSphere(radius):
    return 3/4 * pi * radius**3

def VolumeFractionSpheres(radius1, radius2):
    return (radius1/radius2) ** 3

def VolumeFractionOUSV(radius):
    return VolumeFractionSpheres(radius, Rad_OU)

print(DistanceBetweenPoints((0,0,0), (0,1,-1)))

#----------------------------------------------------- BIRTHDATES, OU RADII ---------------------------------------------------------
rand.seed(str(42) + "GC times")

times_loading = True

universe_cutoff = 30


gc_pergyr_oneplanet = [0,4.2546658834708776*10**(-29),2.4609579039648997*10**(-25),1.5417004688632546*10**(-22),3.727345294412463*10**(-20),2.047668565777006*10**(-18),2.830979314777244*10**(-17),1.594570822238996*10**(-16),5.477540846856254*10**(-16),1.3784054733928482*10**(-15),2.8131868977426146*10**(-15),5.092981830686937*10**(-15),8.334507578454709*10**(-15),1.2486131284589973*10**(-14),1.810226487229367*10**(-14),2.4994759152422298*10**(-14),3.28924897170376*10**(-14),4.201405255408686*10**(-14),5.299617931879158*10**(-14),6.594927317539919*10**(-14),7.962903001059168*10**(-14),9.446637083951629*10**(-14),1.1052508033027574*10**(-13),1.280408624963071*10**(-13),1.4762325058037253*10**(-13),1.7009511916788013*10**(-13),1.9304615298377014*10**(-13),2.1682202016132117*10**(-13),2.416601108851307*10**(-13),2.675164936410615*10**(-13),2.9524924666625715*10**(-13)]
num_hab_planets = 2.5511553931*10**(22)
ic_to_gc_rate = 10**(-6.469070092)

gcnum_tnow_oneplanet = 4.4343714048*10**(-14)
gcnum_tnow_perOUSV = int( (gcnum_tnow_oneplanet * num_hab_planets * ic_to_gc_rate) // 1 )

gc_pergyr_perOUSV = [i * num_hab_planets * ic_to_gc_rate for i in gc_pergyr_oneplanet]

def num_GCs_by_gyr(gyr):
    return int( sum(gc_pergyr_perOUSV[:gyr+1]) // 1 )


def GC_num_from_cutoff(cutoff,a=a):
    if cutoff == a : 
        return gcnum_tnow_perOUSV
    else :
        return num_GCs_by_gyr(cutoff)

gcnum = GC_num_from_cutoff(universe_cutoff)

grabbies = []

ts = time()


if times_loading:
    time_arrays = np.load("sophonce_gc_times.npz")

    birthdates = time_arrays["arr_bd"]
    print("\nLOADING BIRTHDATES")
else:
    print("\nGENERATING BIRTHDATES")
    birthdates = []
    thisdate = 0

    if gcnum >= gcnum_tnow_perOUSV: # keeps the set before humanity the same for all cutoffs after now

        print("GENERATING PAST BIRTHDATES")
        rand.seed(str(seed) + "past bdates")
        for i in range(gcnum_tnow_perOUSV):
            thisdate = rand_GC_time()
            birthdates.append(thisdate)
            #print(thisdate)

        print("APPENDING HUMANITY")
        birthdates.append(a)

        print("GENERATING FUTURE BIRTHDATES")
        rand.seed(str(seed) + "future bdates")
        for i in range(gcnum-gcnum_tnow_perOUSV):
            thisdate = rand_GC_time(a, universe_cutoff)
            birthdates.append(thisdate)
            #print(a, universe_cutoff)

    else:

        print("GENERATING PAST BIRTHDATES")
        rand.seed(str(seed) + "past bdates")
        for i in range(gcnum):
            birthdates.append(rand_GC_time(0.1, universe_cutoff))
    birthdates.sort()

te = time()
tprint(ts,te)

ts = time()

if times_loading:
    birthdates_sf = time_arrays["arr_bdsf"]
    print("\nLOADING BIRTH SCALE FACTORS")
else:
    print("\nCALCULATING BIRTH SCALE FACTORS")
    birthdates_sf = [scale_factor_from_time(i) for i in birthdates]
    birthdates_inv_sf = [1/i for i in birthdates_sf]



te = time()
tprint(ts,te)

ts = time()

if times_loading:
    OU_rads_dates = time_arrays["arr_our"]
    print("\nLOADING OU-RADS")
else:
    print("\nCALCULATING OU-RADS")
    OU_rads_dates = [light_has_travelled(birthdates_sf[0])]
    
    for i in range(gcnum-1+1): #plus one cos humanity
        herets = time()
        if i% 100 == 0 : print(str(i) + " finished")
        j = i+1
        already_travelled = OU_rads_dates[i]
        if i > 0: 
            lo_a = hi_a
            lo_t = hi_t
            inv_lo_a = inv_hi_a
        else:
            lo_a = birthdates_sf[i]
            lo_t = birthdates[i]
            inv_lo_a = birthdates_inv_sf[i]
        hi_a = birthdates_sf[j]
        hi_t = birthdates[j]
        inv_hi_a = birthdates_inv_sf[j]
        #hereherets = time()
        next_integral = quad(time_from_inv_scale_factor, inv_hi_a, inv_lo_a)[0]
        #hereherete = time()
        adjustment = (inv_hi_a) * (hi_t - lo_t) - (inv_lo_a - inv_hi_a) * lo_t
        OU_rads_dates.append(already_travelled + next_integral + adjustment)
        herete = time()
        #print("Time fraction: " + str((hereherete-hereherets) - (herete-herets)))

    #OU_rads_dates.append(Rad_AU)

te = time()
tprint(ts,te)

#ts = time()



#OU_rads_dates = [light_has_travelled(scale_factor_from_time(i)) for i in birthdates]

#print(OU_rads_dates[1], light_has_travelled(birthdates_sf[1]))
#print(OU_rads_dates[-1], light_has_travelled(birthdates_sf[-1]))

#te = time()
#tprint(ts,te)

print()

if not times_loading:
    np.savez("sophonce_gc_times.npz", arr_bd=birthdates, arr_bdsf=birthdates_sf, arr_our=OU_rads_dates)

#print(birthdates)
#print(len(birthdates), len(birthdates_sf), len(OU_rads_dates))



#rand.seed(str(42) + "GC positions")

points_loading = True


ts = time()

points = []
pointnum = 20000 # 5000
lastpointindex = -1
if points_loading:
    print("\nLOADING POINTS")
    point_arrays = np.load("sophonce_gc_points.npz")
    points = point_arrays["array5"]
    #pointdists = point_arrays["array6"]
else:
    print("\nGENERATING POINTS")

    rand.seed(str(seed) + "points")
    for i in range(pointnum):
        points.append(PointInSphereCrude(Rad_OU))
    #pointdists = []
    #for i in range(len(points)):
    #    pointdists.append([])
    #    for j in range(len(points)):
    #        thisdist = DistanceBetweenPoints(points[i], points[j])
    #        #print(thisdist)
    #        pointdists[i].append(thisdist)
    #        #print([i, j])
    #    print(i)
    #print(points)
    #print(pointdists)

#adding humanity's origin
points[gcnum_tnow_perOUSV] = (0, 0, 0)

te = time()
tprint(ts,te)

if not points_loading:
    #np.savez("sophonce_gc_points.npz", array5=points, array6 = pointdists)
    np.savez("sophonce_gc_points.npz", array5=points)



gc_loading = True

ts = time()

successful_indices = []
if gc_loading:
    print("\nLOADING GCS")
    point_arrays = np.load("sophonce_gc_civs.npz")
    successful_indices = point_arrays["array"]
    for i in successful_indices:
        grabbies.append(GC(i, points[i], 0, birthdates[i], 0))
else:
    print("\nSTARTING GC ITERATIVE REJECTION")
    for i in range(gcnum+1):
        thist = birthdates[i]
        thisp = points[i]
        thisou = OU_rads_dates[i]
        this_rej = False

        for j in grabbies:
            thatt = j.time
            thatp = j.pos
            thatou = j.ourad
            #print(thisp, thatp)
            thatrad = thisou - thatou
            #print(thatrad)
            if IsPointInSphere(thatrad, thatp, thisp):
                #print("GC " + str(i) + " rejected due to being within GC " + str(j.index))
                this_rej = True
                break
        
        if not this_rej :
            #print("GC " + str(i) + " successfully begins expansion")
            #print(thist)
            successful_indices.append(i)
            grabbies.append(GC(i, thisp, 0, thist, 0))


te = time()
tprint(ts,te)

if not gc_loading:
    #np.savez("sophonce_gc_points.npz", array5=points, array6 = pointdists)
    np.savez("sophonce_gc_civs.npz", array=successful_indices)

#min_dist = Rad_OU
#for i in range(220): #220
#    thist = t1[i]
#    thisl = l1[i] * (t1[i+1] - thist)
#    #print(thist)
#    if thist > a: break
#    lmod = int(thisl // 1)
#    lrem = thisl - lmod
#    rand.seed(42 + lrem)
#    extra = rand.random() < lrem
#    #print(extra)
#    rejected = 0 
#    for j in range(lmod + extra):
#        lastpointindex += 1
#        gc_pos = points[lastpointindex]
#
#        this_rejected = False
#        for k in grabbies:
#            #ts = time()
#            distpoints = pointdists[lastpointindex, k.pindex]
#            #print(pointdists[lastpointindex, k.pindex])
#            #print(DistanceBetweenPoints(points[lastpointindex], points[k.pindex]))
#        
#            #print("DIfference: " + str(distpoints - pointdists[lastpointindex, k.pindex]))
#            if min_dist > distpoints:
#                min_dist = distpoints
#                print(min_dist)
#            that_comov_rad = k.comovingradius_list_index(i)
#            #print(distpoints, that_comov_rad)
#            if IsPointInSphere(that_comov_rad, k.pos, gc_pos):
#                rejected += 1
#                this_rejected = True
#                break
#            #te = time()
#            #print("Time: " + str(te-ts))
#        
#        if not this_rejected:
#            grabbies.append(GC(gc_pos, lastpointindex, thist, i))
#    
#    if rejected > 0: 
#        print(str(rejected) + " GCs rejected at " + str(thist))

rand.seed(str(seed) + "GCs iterated")

print("Number of GCs: " + str(len(grabbies)))
print("Number of attempted GCs: " + str(gcnum+1))
print("Largest comoving radius by now: " + str(grabbies[0].comovingradius(a)))
print("Earliest time of GC: " + str(grabbies[0].time))



#print(pointdists[:5,:5])
#print(points[:5])

real_birthdates = []
for i in grabbies:
    real_birthdates.append(i.time)
        


#print(t1)

#---------------------------------------------------- SEARCHING FOR HUMANITY -----------------------------------------------------

humanindex = -1

for i in range(len(grabbies)):
    g = grabbies[i]
    if 13.5 < g.time < 14:
        if g.time == a:
            humanindex = i
            print("\nHUMAN INDEX LOCATED: " + str(i))


humanity = grabbies[humanindex]
print(humanity.pos)
print(humanity.comovingradius(a))
print(humanity.comovingradius(1000))
print(VolumeFractionOUSV(humanity.comovingradius(1000)))

print("Observable Universe current radius: " + str(Rad_OU))
print("Affectable Universe current radius: " + str(Rad_AU))

print()

n_gc_contact = 0
n_gc_comehere = 0
n_gc_gothere = 0


#for i in range(len(grabbies)):
#    g = grabbies[i]
#    dist_e = DistanceBetweenPoints(g.pos, humanity.pos)
#    g_AU = Rad_EOU - g.ourad
#    if dist_e < g_AU + Rad_AU :
#        print("\nGC " + str(i))
#        print(round(g.time, 3), round(dist_e, 3), g.pos)
#        print("GC and humanity in contact")
#        if g.time < a:
#            print("We meet at this distance:", str((dist_e - (Rad_OU - g.ourad))/2))
#        else:
#            print("We meet at this distance:", str((dist_e - (g.ourad - Rad_OU))/2))
#        n_gc_contact += 1
#        if dist_e < g_AU :
#            print("GC can reach Earth")
#            n_gc_comehere += 1
#        if dist_e < Rad_AU :
#            print("Humanity can reach GC origin")
#            n_gc_gothere += 1
#
#print("Number of GCs we meet: " + str(n_gc_contact))
#print("Number of GCs that can come here: " + str(n_gc_comehere))
#print("Number of GCs whose origin we can go to: " + str(n_gc_gothere))

def PointIsInWhatGC(point, sf):
    candidate_index = -1
    maxdistextra = 0
    for i in range(len(grabbies)):
        g = grabbies[i]
        grad = Rad_EOU - g.ourad
        if grad >= 0:
            #print(i)
            if IsPointInSphere(grad, g.pos, point):
                gdist = dist(g.pos, point)
                gdistextra = grad - gdist
                if gdistextra > maxdistextra:
                    maxdistextra = gdistextra
                    candidate_index = i
    return candidate_index

print(PointIsInWhatGC((5, 0, 0), 1))

samplepoints = [(0,0,0)]

samplerad = 6 #16.5

for i in range(2000):
    point = PointInSphereCrude(samplerad)
    pointwhatgc = PointIsInWhatGC(point, 1)
    #while pointwhatgc > 30:
    #    point = PointInSphereCrude(samplerad)
    #    pointwhatgc = PointIsInWhatGC(point, 1)
    samplepoints.append(point)

sampleindices = [PointIsInWhatGC(i, 1) for i in samplepoints]
xs = [i[0] for i in samplepoints]
ys = [i[1] for i in samplepoints]
zs = [i[2] for i in samplepoints]
cs = [((i**10%255)/255, (i**11%255)/255, (i**12%255)/255) for i in sampleindices]
print(sampleindices)
print(list(set(sampleindices)))
for i in list(set(sampleindices)):
    g = grabbies[i]
    print(i, round(g.time, 3))
    p = g.pos
    print((round(p[0], 3),round(p[1], 3),round(p[2], 3)))

#---------------------------------------------------- GRAPH REAL GCS AGAINST GC BIRTHRATE -----------------------------------------------------
timelist_2 = [i * 1 + 5 for i in range(int(universe_cutoff - 4))]
interv_gc_births_theory = [gc_pergyr_perOUSV[i] for i in timelist_2]
interv_gc_births_attempt = [0]
interv_gc_births_real = [0]

for i in range(len(timelist_2)-1):
    lowr = timelist_2[i]
    hir = timelist_2[i+1]
    #print(lowr, hir)
    attcount = 0
    for j in birthdates:
        if lowr < j and j <= hir:
            attcount += 1
    #print(count)
    interv_gc_births_attempt.append(attcount * 1 * 1)

    realcount = 0
    for j in real_birthdates:
        if lowr < j and j <= hir:
            realcount += 1
    #print(count)
    interv_gc_births_real.append(realcount * 1 * 1)

#print(max(real_birthdates))
#print(ngc_list)

#print(num_GCs_by_gyr(30))
#print(timelist_2)

# GRAPH IT
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fig, ax = plt.subplots()
ax.plot(t1,l1[:511])
ax.scatter(l_randbx, l_randby)
ax.scatter(l_randgx, l_randgy)
ax.plot(timelist_2,interv_gc_births_theory, color="green")
ax.plot(timelist_2,interv_gc_births_attempt, color="blue")
ax.plot(timelist_2,[R_GC_interpolate(i) for i in timelist_2], color="red")
ax.plot(timelist_2,interv_gc_births_real, color="orange")
plt.xlim(0,30)
plt.ylim(0,10**4)
plt.show()

ax = plt.figure().add_subplot(projection="3d")
ax.set_aspect("equal")
ax.scatter(xs, ys, zs, c=cs)
ax.axes.set_xlim3d(left  =-samplerad, right=samplerad) 
ax.axes.set_ylim3d(bottom=-samplerad, top=  samplerad) 
ax.axes.set_zlim3d(bottom=-samplerad, top=  samplerad)
plt.show()