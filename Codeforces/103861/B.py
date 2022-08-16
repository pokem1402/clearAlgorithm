def get_answer(S):

    #     S = bytes(S, 'ascii')
    answer = 0
    n = len(S)

    for start in range(n - 6 + 1):
        for la in range(1, int((n - 3 - start)/3) + 1):  # 3 * la <= n - 3 - start

            A = S[start:start+la]
            A1_start = start+la

            if A == S[A1_start:A1_start+la]:  # A[0] == A[1]

                for L in range(2, n - start - 3*la - 1 + 1):
                    A2_start = A1_start+la+L
                    if A != S[A2_start:A2_start+la]:
                        continue

                    lc = L - 1  # max length of C
                    lb = 1

                    while (lb <= n - start - 3 * la - L) and lc >= 1:
                        B1_start = A1_start + la
                        B2_start = A2_start + la
                        if(S[B1_start:B1_start+lb] == S[B2_start:B2_start+lb]):
                            answer += 1
                            # if((n-start-3*la-2*lb-lc) == 0 and start == 0):
                            #     print(answer, 'X'*start, A, A, S[B1_start:B1_start+lb],
                            #           S[B1_start+lb:B1_start+lb+lc], A, S[B1_start:B1_start+lb], 'X'*(n-start-3*la-2*lb-lc))

                        lc -= 1
                        lb += 1
    return answer


n = int(input())
for i in range(n):
    print(get_answer(input()))