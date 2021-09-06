C = "consumption"
I = 'investment net of savings'
G = 'government spending + taxation'
M = 'imports'
X = 'exports'

ni = ("C + I + G + X - M") # ni = national income

mpc = 'mpc is "marginal prosperity to consume" or "the proportion/percentage of any extra unit of money earned which is spent\n'
mps = 'mps is "marginal prosperity to save" or "the proportion/percentage of any extra unit of money earned which is saved\n'
mpm = 'mpm is "marginal prosperity to import" or "the proportion/percentage of any extra unit of money earned which is spent on imports\n'
mpt = 'mpt is "marginal prosperity to be taxed" or "the proportion/percentage of any extra unit of money earned which is spent on exports\n'

cem = "Closed Economy Multiplier"
oem = "Open Economy Multiplier"
user = input("Which option= '1' for Closed Economy Multiplier (MPC only), '2' Open Economy Multiplier, '3' Full Multiplyer Formula: \n")

if user in ('1'):
    print(cem)

    print("")
    print(mpc)
    mpcnum = float(input('please input your mpc (after multiplying it by 10, e.g if mpc= .8 then you input 8)in numerical/decimal format: '))

    def formula(mpcnum):
        denominator= 10-mpcnum
        ans= 10/denominator
        return ans
    print('your multiplier is:')
    print(formula(mpcnum))


elif user in ('2'):
    print(oem)
    print("")
    user1 = input(" '1' for MPC route or '2' for  MPS route: ")
    if user1 in ('1'):
        print(mpc)
        mpcnum = float(input('please input your mpc (after multiplying it by 10, e.g if mpc= .8 then you input 8)in numerical/decimal format: '))

        print(mpm)
        mpmnum = float(input('\nplease input your mpm (after multiplying it by 10, e.g if mpm= .2 then you input 2) in numerical/decimal format: '))
        def formula(mpcnum):
            denominator = 10 - mpcnum + mpmnum
            ans = 10/denominator
            return ans
        print('\nyour multiplier is:')
        print(formula(mpcnum))

    elif user1 in ('2'):
        print(mps)
        mpsnum = float(input(
            'please input your mps (after multiplying it by 10, e.g if mps= .6 then you input 6)in numerical/decimal format: '))
        print(mpm)
        mpmnum = float(input(
            'please input your mpm (after multiplying it by 10, e.g if mpm= .2 then you input 2) in numerical/decimal format: '))

        def formula(mpsnum):
            denominator = mpsnum + mpmnum
            ans = 10 / denominator
            return ans

        print('\nyour multiplier is:')
        print(formula(mpsnum))
    else:
        print('not an option dumbass')


elif user in ('3'):
    print(mpm)
    print("")
    user1 = input(" '1' for MPC route or '2' for  MPS route: ")
    if user1 in ('1'):
        print(mpc)
        mpcnum = float(input('please input your mpc (after multiplying it by 10, e.g if mpc= .8 then you input 8)in numerical/decimal format: '))
        print(mpm)
        mpmnum = float(input('please input your mpm (after multiplying it by 10, e.g if mpm= .2 then you input 2) in numerical/decimal format: '))
        print(mpt)
        mptnum = float(input('please input your mpt (after multiplying it by 10, e.g if mpm= .3 then you input 3) in numerical/decimal format: '))

        def formula(mpcnum):
            denominator1 = 10 - mpcnum
            denominator = denominator1 + mptnum + mpmnum
            ans = 10/denominator
            return ans
        print('\nyour multiplier is:')
        print(formula(mpcnum))

    elif user1 in ('2'):
        print(mps)
        mpsnum = float(input('please input your mps (after multiplying it by 10, e.g if mps= .8 then you input 8)in numerical/decimal format: '))
        print(mpm)
        mpmnum = float(input('please input your mpm (after multiplying it by 10, e.g if mpm= .2 then you input 2) in numerical/decimal format: '))
        print(mpt)
        mptnum = float(input('please input your mpt (after multiplying it by 10, e.g if mpm= .3 then you input 3) in numerical/decimal format: '))

        def formula(mpsnum):
            denominator = mpsnum + mpmnum + mptnum
            ans = 10 / denominator
            return ans

        print('\nyour multiplier is:')
        print(formula(mpsnum))
    else:
        print('not an option dumbass')
else:
    print('Not one of the options dumbass')

