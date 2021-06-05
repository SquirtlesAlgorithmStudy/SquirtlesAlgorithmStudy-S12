import heapq
def avgcalculate(jobs_f, end):
    total = 0
    for i in range(len(jobs_f)):
        total += end[i]-jobs_f[i][0]
    total //= len(jobs_f)
    return total

def solution(jobs):
    jobs = sorted(jobs, key = lambda x:-x[0])
    clock = 0
    task = [] # 현재 작업 중인 작업 ([요청시간, 걸리는 시간], 시작한 시간)
    request = [] # 요청 작업 힙
    jobs_f = [] # 끝난 작업의 요청시간
    end = [] # 끝난 작업의 끝난 시간
    while True:
      if len(task) != 0:
          if task[0][1] + task[0][0][1] == clock:
             jobs_f.append(task[0][0])
             end.append(clock)    
             task.pop()        # 작업 끝나면 task 목록에서 내보내기
      
      while True:
          if(len(jobs) != 0):
             if jobs[len(jobs)-1][0] == clock:   # 현재 클락에 작업 요청이 있으면
                temp1 = jobs.pop()
                heapq.heappush(request, (temp1[1], temp1))  # 리퀘스트 목록에 힙으로 넣기
             else : break
          else : break
      if len(jobs) == 0 and len(task) == 0 and len(request) == 0: break #요청도 일도 없으면 반복 종료

      if len(task) == 0 and len(request) != 0: 
        temp2 = heapq.heappop(request)[1]
        task.append((temp2, clock)) # 테스크가 비어 있고 리퀘스트가 있으면 작업 시작

     
      clock += 1
    return avgcalculate(jobs_f, end)