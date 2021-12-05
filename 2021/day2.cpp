#include <iostream>
#include <fstream>
#include <vector>


int part1() {
    std::fstream inputfile;
    int depth = 0;
    int pos = 0;
    std::string instruction;
    inputfile.open("day2.txt", std::ios::in);
    if(inputfile.is_open()){
	while(getline(inputfile, instruction)){
	    std::string command = instruction.substr(0, instruction.find(' '));
	    int amount = std::stoi(instruction.substr(instruction.find(' ')));
	    if (command == "up"){
		depth -= amount;
	    }
	    if (command == "down"){
		depth += amount;
	    }
	    if (command == "forward"){
		pos += amount;
	    }
	}
    }
    return depth * pos;
}


int part2(){
    std::fstream inputfile;
    int depth = 0;
    int pos = 0;
    int aim = 0;
    std::string instruction;
    inputfile.open("day2.txt", std::ios::in);
    if(inputfile.is_open()){
	while(getline(inputfile, instruction)){
	    std::string command = instruction.substr(0, instruction.find(' '));
	    int amount = std::stoi(instruction.substr(instruction.find(' ')));
	    if (command == "up"){
	        aim -= amount;
	    }
	    if (command == "down"){
	        aim += amount;
	    }
	    if (command == "forward"){
		pos += amount;
		depth += aim * amount;
	    }
	}
    }
    return depth * pos;
}



int main() {
    int result1 = part1();
    std::cout << "Result 1:" << result1 << std::endl;
    int result2 = part2();
    std::cout << "Result 2:" << result2 << std::endl;
}
