#include <iostream>
#include <fstream>
#include <vector>

int part1() {
    std::fstream day1_file;
    int decreasing_depths = 0;
    day1_file.open("day1.txt", std::ios::in);
    if(day1_file.is_open()){
	int last_depth = 1000000;
	int depth;
	while(day1_file >> depth){
	    if(last_depth < depth)
		decreasing_depths++;
	    last_depth = depth;
	}
    }
    return decreasing_depths;
}


int part2() {
    std::fstream day1_file;
    std::vector<int> depth_list;
    int decreasing_depths = 0;
    day1_file.open("day1.txt", std::ios::in);
    if(day1_file.is_open()){
	int depth;
	while(day1_file >> depth){
	    depth_list.push_back(depth);
	    if (depth_list.size() < 4)
	        continue;
	    int previous_tuple_sum = depth_list.at(depth_list.size() - 2) + depth_list.at(depth_list.size() - 3) + depth_list.at(depth_list.size() - 4);
	    int tuple_sum = depth_list.at(depth_list.size() - 1) + depth_list.at(depth_list.size() - 2) + depth_list.at(depth_list.size() - 3);
	    if(previous_tuple_sum < tuple_sum){
		decreasing_depths++;
	    }
	}
    }
    return decreasing_depths;
}

int main() {
    int decreasing_depths = part1();
    std::cout << "Number of decreasing depths:" << decreasing_depths << std::endl;
    int decreasing_tuples = part2();
    std::cout << "Number of decreasing tuples:" << decreasing_tuples << std::endl;
}
