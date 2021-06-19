def record_to_code(message, database, history):
    if message[0] == 'E':
        state, iden, nick = message.split()
        database[iden] = nick
        history.append((1, iden))
    elif message[0] == "L":
        state, iden = message.split()
        history.append((0, iden))
    else:
        state, iden, nick = message.split()
        database[iden] = nick
        
def code_to_message(database, history):
    result = []
    for i in history:
        if i[0] == 1: result.append(database[i[1]] + "님이 들어왔습니다.")
        elif i[0] == 0: result.append(database[i[1]]+ "님이 나갔습니다.")
    return result
            
            
def solution(record):
    database = {}
    history = []
    for message in record:
        record_to_code(message,database,history)
    answer = code_to_message(database, history)
    return answer   

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))