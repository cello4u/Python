# 정렬 알고리즘(Sort Algorithm): 가장[작은|큰] 데이터를 왼쪽으로 순서대로 이동

#[?} 무작위 데이터를 순서대로 [오름차순(ASC)|내림차순(DESC)] 정렬

def main():
   
    #[1] Input: Data Structure(Array, List, Stack, Queue, Tree, DB, ...)
    data = [ 3, 2, 1, 5, 4 ] #정렬되지 않은 데이터
    N = len(data) 
    

    #[2] Process: Selection Sort(선택정렬) 알고리즘
    for i in range(0, N - 1): # i = 0 to N-1
        for j in range(i + 1, N): #j = i+1 to N
            if data[i] > data[j]: # 부등호 방향: 오름차순(>), 내림차순(<)
                temp = data[i]; data[i] = data[j]; data[j] = temp #swap 코드

    #[3] Output: UI(Console, Desktop, Web, Mobile, ...)
    for i in range(N):
        print(data[i])
    print(data)

if __name__ == "__main__":
    main()

