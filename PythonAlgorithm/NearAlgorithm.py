# 근삿값 알고리즘(Near Algorithm): 가까운 값 -> 차잇값의 절댓값의 최솟값

#[?] 원본 데이터 중에서 대상 데이터와 가장 가까운 값
import sys

def main():
    #[0] Initialize
    min = +sys.maxsize #차잇값의 절댓값의 최솟값이 담길 그릇
    
    #[1] Input
    numbers = [ 10, 20, 30, 27, 17 ]
    target = 25 # target과 가까운 값
    near = 0 # 가까운 값 담는 그릇
    N = len(numbers)
    
    #[2] Process: Near 
    for i in range(0, N):
        _abs = abs(numbers[i] - target) # 차이의 절대값
        if _abs < min:
            min = _abs # min
            near = numbers[i] # Near: 차잇값의 절대값의 최솟값일 때의 값
    
    #[3] Output
    print(f"{target}와/과 가장 가까운 값: {near}(차이: {min})")

if __name__ == "__main__":
    main()
    