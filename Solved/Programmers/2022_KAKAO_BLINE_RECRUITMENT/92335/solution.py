def solution(n, k):

    # k 진법으로 변환된 각 자리수를 저장하는 리스트
    k_base = []
    # n이 0이 될떄까지
    while n > 0:
        # k로 나눈 나머지들을 저장한다.
        k_base.append(str(n % k))
        n //= k

    # k 진법을 역으로 구하였으므로 이를 역전함
    # 그리고 0을 기준으로 문자열을 쪼개어서 숫자를 구함
    nums = [int(n) for n in (''.join(k_base[::-1])).split('0') if n]

    answer = 0
    # 담겨있는 숫자마다
    for num in nums:
        # 1은 소수가 아니므로 제외
        if (num == 1):
            continue
        # 2 체크
        if (num == 2):
            answer += 1
            continue
        # 값이 3 이상인 경우
        else:
            # 2 이후의 소수는 모두 홀수 이므로 2씩 더하고, 거듭제곱이 아닌 이상 제곱근까지의 수를 검사하면 소수 판별 가능
            for i in range(3, int(num**0.5)+1, 2):
                if num % i == 0:
                    break
            # 만약 약수가 존재하지 않은 경우
            else:
                answer += 1

    return answer
