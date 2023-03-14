import os

def read_file(fp, filename, name):
    output = ["P1BYY1", "P2BYY2", "P1ONX2", "P2ONX1", "Y1ONX1", "Y2ONX2",
            "P1WITHP2", "X1WITHX2", "Y1WITHY2", "VARIANCEX1", "VARIANCEX2", "RESIDUALY1",
            "RESIDUALY2", "RESIDUALP1", "RESIDUALP2"]

    flag = -1

    fo = open(filename, 'r')
    while True:
        line = fo.readline()
        if line == None:
            break

        if "THE MODEL ESTIMATION TERMINATED NORMALLY" in line:
            flag = 0
            break
        elif "NO CONVERGENCE." in line:
            flag = 1
            break

    fo.close()

    fo = open(filename, 'r')
    if flag == 0:
        while True:
            line = fo.readline()
            if line == None:
                break

            if "CONFIDENCE INTERVALS OF MODEL RESULTS" in line:
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                idx = 0
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                line = fo.readline()
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')

                idx += 1
                line = fo.readline()
                ary = line.strip().split()
                fp.write(name + ' ' + output[idx] + ' ' + ary[1] + ' ' + ary[2] + ' ' + ary[3] + ' ' + ary[4] + ' ' + ary[5] + ' ' + ary[6] + ' ' + ary[7] + '\n')
                break
    elif flag == 1:
        for out in output:
            fp.write(name + ' ' + out + ' 0 0 0 0 0 0 0\n')
    elif flag == -1:
        print ('something wrong')


sample_size = [100, 200, 300]
condition = range(1, 32)
k = [-1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
numbering = range(1, 101)


fp = open('result', 'w')
fp.write("CONDITION\tPATH\tLower.5%\tLower2.5%\tLower5%\tUpper 5%\tUpper 2.5%\tUpper .5%\n")

for size in sample_size:
    idx = 0
    for file_k in k:
        for numb in numbering:
            filename = os.path.join(str(size), "Condition"+ str(condition[idx]) + "_" + str(file_k), "step2.external_monte_carlo_phantom_k_parameter_k_" + str(file_k) + "_s_" + str(size) + "_" + str(numb) + ".out")
            name = str(size) + "_" + str(file_k) + "_" + str(numb)
            read_file(fp, filename, name)
        idx += 1

fp.close()
