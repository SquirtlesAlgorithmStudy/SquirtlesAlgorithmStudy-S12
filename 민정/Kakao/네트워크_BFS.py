def solution(n, computers):
    visited = [-1]*n
    answer = 0
    
    for i in range(len(visited)):
        if visited[i] == -1:
            answer += 1
            start = i
            queue = [start]
            visited[start] = 1
            print(start, "방문")
        
            while queue:
                tmp = queue.pop(0)
                for j in range(len(computers[tmp])):
                    if tmp == j:
                        print(tmp,j,"자기 자신과 연결")
                    elif visited[j] == 1:
                        print(tmp,j,"이미 방문")
                    elif computers[tmp][j]==0:
                        print(tmp,j,"연결 X")
                    else:
                        visited[j] = 1
                        queue.append(j)
                        print(start,j,"방문")
                        print("queue:",queue)
                print(tmp, "BFS", visited)
    
    return answer