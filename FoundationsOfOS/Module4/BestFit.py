def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        best_idx = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:
                if best_idx == -1 or memory_blocks[best_idx] > memory_blocks[j]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            memory_blocks[best_idx] -= process_sizes[i]

    return allocation

# Example usage
memory_blocks = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]
allocation = best_fit(memory_blocks, process_sizes)

print("Process No.\tProcess Size\tBlock No.")
for i in range(len(process_sizes)):
    print(f"{i + 1}\t\t{process_sizes[i]}\t\t{allocation[i] + 1 if allocation[i] != -1 else 'Not Allocated'}")
