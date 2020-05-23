

def countSteps(steps):
    if steps < 0:
        return 0
    elif steps==0:
        return 1
    return countSteps(steps-1) +countSteps(steps-2) + countSteps(steps-3)

def countStepsMemo(steps, memo):
    memo = {}
    if steps < 0:
        return 0
    elif steps ==0 :
        return 1
    elif steps == 1:
        return 1

    if steps in memo:
        return memo[steps]
    else:
        memo[steps] = countStepsMemo(steps-1, memo) + countStepsMemo(steps-2, memo) + countStepsMemo(steps-3, memo)
    return memo[steps]

def count(steps):
    memo = {}
    return countStepsMemo(steps, memo)

print("There are {} ways to climb the steps ".format(count(3)))