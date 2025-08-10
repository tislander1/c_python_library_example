#include <iostream>
#include <vector>
#include <thread>
#include <numeric> // For std::iota
#include <cstdlib> // For std::rand, std::srand

void add_segment(const std::vector<int>& vec1, const std::vector<int>& vec2,
                 std::vector<int>& result_vec, int start_index, int end_index) {
    for (int i = start_index; i < end_index; ++i) {
        result_vec[i] = vec1[i] + vec2[i];
    }
}

int main() {
    const int vector_size = 10002;
    std::vector<int> vec_a(vector_size);
    std::vector<int> vec_b(vector_size);
    std::vector<int> result_vec(vector_size);

    // Initialize vectors
    std::iota(vec_a.begin(), vec_a.end(), 1); // vec_a = {1, 2, 3, ...}
    std::iota(vec_b.begin(), vec_b.end(), 100); // vec_b = {100, 101, 102, ...}

    const int num_threads = 4;
    int segment_size = vector_size / num_threads;
    std::vector<std::thread> threads;

    for (int i = 0; i < num_threads; ++i) {
        int start_index = i * segment_size;
        int end_index = (i == num_threads - 1) ? vector_size : (i + 1) * segment_size;
        threads.emplace_back(add_segment, std::cref(vec_a), std::cref(vec_b),
                             std::ref(result_vec), start_index, end_index);
    }

    for (std::thread& t : threads) {
        t.join();
    }

    // Optional: Print a few elements to verify
    for (int i = 0; i < 10; ++i) {
        std::cout << result_vec[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}