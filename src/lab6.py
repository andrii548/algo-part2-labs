from min_heap import MinHeap

def solve():
    try:
        with open('gamsrv.in', 'r') as f:
            input_data = f.read().split()
    except FileNotFoundError:
        print("Помилка: Файл gamsrv.in не знайдено.")
        return

    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    edge_tokens_count = 3 * m
    client_tokens = input_data[2 : len(input_data) - edge_tokens_count]
    clients = [int(x) for x in client_tokens]
    
    adjency_list = [[] for _ in range(n + 1)]
    edge_data = input_data[len(input_data) - edge_tokens_count:]
    pq = MinHeap()

    for i in range(m):
        current = int(edge_data[3 * i])
        next = int(edge_data[3 * i + 1])
        latency = int(edge_data[3 * i + 2])
        adjency_list[current].append((next, latency))
        adjency_list[next].append((current, latency))

    clients_set = set(clients)
    candidates = [i for i in range(1, n + 1) if i not in clients_set]

    answer = float('inf')

    if len(candidates) <= len(clients):
        for candidat in candidates:
            dist = [float('inf')] * (n + 1)
            dist[candidat] = 0
            pq.push((0, candidat))
            
            while pq:
                distance, current = MinHeap.pop(pq)
                if distance > dist[current]:
                    continue
                for next, weight in adjency_list[current]:
                    if dist[current] + weight < dist[next]:
                        dist[next] = dist[current] + weight
                        MinHeap.push(pq, (dist[next], next))
            
            max_dist_to_client = max(dist[client] for client in clients)
            if max_dist_to_client < answer:
                answer = max_dist_to_client

    else:

        max_dist_for_candidat = {candidat: 0 for candidat in candidates}
        
        for client in clients:
            dist = [float('inf')] * (n + 1)
            dist[client] = 0
            pq.push((0, client))
            
            while pq:
                distance, current = MinHeap.pop(pq)
                if distance > dist[current]:
                    continue
                for next, weight in adjency_list[current]:
                    if dist[current] + weight < dist[next]:
                        dist[next] = dist[current] + weight
                        MinHeap.push(pq, (dist[next], next))
            
            for candidat in candidates:
                if dist[candidat] > max_dist_for_candidat[candidat]:
                    max_dist_for_candidat[candidat] = dist[candidat]
        
        if candidates:
            answer = min(max_dist_for_candidat.values())

    with open('gamsrv.out', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == '__main__':
    solve()