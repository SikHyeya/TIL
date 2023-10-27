# 231027
# 프로그래머스
# https://school.programmers.co.kr/learn/courses/30/lessons/92343

# DFS
def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    
    def dfs(sheep, wolf):
        if sheep > wolf :
            answer.append(sheep)
        else:
            return
        
        for parent, child in edges:
            # 부모노드 방문, 자식노드 방문 안 했을 때
            if visited[parent] and not visited[child]:
                visited[child] = 1      # 자식 노드 방문 처리
                # 만약 자식 노드가 양이라면,
                if info[child] == 0:
                    dfs(sheep+1, wolf)  # 양의 수 +1
                else:
                    dfs(sheep, wolf+1)  # 늑대의 수 +1
                # 자식 노드 방문 취소 처리
                visited[child] = 0
    # 시작 노드 방문 처리
    visited[0] = 1
    # 양으로 시작
    dfs(1, 0)
    
    return max(answer)
