import csv
from re import split


def rec(identifier):
    if dict1[identifier] == [0]:
        return dict2[identifier]
    return dict2[identifier] + max(rec(i) for i in dict1[identifier])


filename = r'C:\Python_Projects\ЕГЭ_Информатика\22. Многопроцессорные системы\Поляков\7376\file.csv'
processes = {}
dict1 = dict()
dict2 = dict()
with open(filename, 'r') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=";"))[1:-6]
    print(reader)
    for row in reader:
        print(row)
        process_id = int(row[0])
        execution_time = int(row[1])
        dependencies = list(map(int, split(r"\D+", row[2])))
        processes[process_id] = [execution_time, dependencies]
        dict1[process_id] = dependencies
        dict2[process_id] = execution_time


def topological_sort(processes):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        if node != 0:
            for neighbor in processes[node][1]:
                dfs(neighbor)
            result.append(node)

    for node in processes:
        dfs(node)

    return result[::-1]


def max_concurrent_time(processes):
    sorted_processes = topological_sort(processes)
    dp = {}
    max_time = 0

    for process in sorted_processes:
        if processes[process][1] == [0]:
            dp[process] = processes[process][0]
        else:
            his_time = processes[process][0]
            maxim_process_time = rec(process) - his_time
            dp[process] = his_time + maxim_process_time
        max_time = max(max_time, dp[process])

    return max_time


max_time = max_concurrent_time(processes)
print(f"Максимальное время выполнения двух процессов одновременно: {max_time}")
