from algo_crate.datastructures.heap import MinHeap


def heapsort(a):

    min_heap = MinHeap(a)
    return [min_heap.extract_min() for _ in range(len(min_heap))]


