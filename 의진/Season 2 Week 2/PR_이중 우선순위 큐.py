import heapq
def insert_heapq(max_heapq, min_heapq, operand):
    heapq.heappush(max_heapq, (-operand, operand))
    heapq.heappush(min_heapq, operand)
    return
    
def del_min(min_heapq, max_heapq):
  if len(min_heapq) != 0:
    del_data = heapq.heappop(min_heapq)
    max_heapq.remove((-del_data, del_data))
    
    
def del_max(min_heapq, max_heapq):
  if len(max_heapq) != 0:
    del_data = heapq.heappop(max_heapq)[1]
    min_heapq.remove(del_data)
  
    
def classifier(operation, max_heapq, min_heapq):
    if operation[0] == 'I':
        number = int(operation.split()[1])
        insert_heapq(max_heapq, min_heapq, number)
    elif operation == 'D 1':
        del_max(min_heapq, max_heapq)
    elif operation == 'D -1':
        del_min(min_heapq, max_heapq)

def solution(operations):
    max_heapq = []
    min_heapq = []
    for operation in operations:
        classifier(operation, max_heapq, min_heapq)

    if len(min_heapq) == 0 : return [0, 0]
    answer = [heapq.heappop(max_heapq)[1], heapq.heappop(min_heapq)]
    return answer

print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))