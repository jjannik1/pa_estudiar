P = [[0,0],[0,0]]

def run(A: list, B: list) -> list:
    # TODO
    global P

    P[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    P[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    P[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    P[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]

   
    



    return P


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

    for i in P:
        print(i)
