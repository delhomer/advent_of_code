#include <iostream>
#include <fstream>
#include <vector>


int part1() {
    std::fstream inputfile;
    inputfile.open("day3.txt", std::ios::in);
    int byte_counter[12] = {0};
    int nb_bytes = 0;
    std::string diagnostic;
    if(inputfile.is_open()){
	while(inputfile >> diagnostic){
	    for(unsigned int i = 0 ; i < diagnostic.length() ; i++){
		byte_counter[i] += (int)(diagnostic[i]) - '0';  // ASCII numbers begin to 48...
	    }
	    nb_bytes++;
	}
    }
    int gamma = 0;
    int epsilon = 0;
    for(unsigned int i = 0 ; i < diagnostic.length() ; i++){
	bool bit = (byte_counter[diagnostic.length() - 1 - i] >= nb_bytes / 2);
	gamma += (bit << i);
	epsilon += (!bit << i);
    }
    return gamma * epsilon;
}


int part2(){
    std::fstream inputfile;
    inputfile.open("day3.txt", std::ios::in);
    std::vector<std::string> oxygen_bytes;
    std::vector<std::string> co2_bytes;
    int gamma_counter = 0;
    int nb_bytes = 0;
    std::string diagnostic;
    if(inputfile.is_open()){
	while(inputfile >> diagnostic){
	    oxygen_bytes.push_back(diagnostic);
	    co2_bytes.push_back(diagnostic);
	    gamma_counter += (diagnostic[0] == '1') ? 1 : 0;
	    nb_bytes++;
	}
    }
    // Oxygen
    int char_idx = 1;
    int oxygen_counter = gamma_counter;
    int nb_oxygen_bytes = nb_bytes;
    while(oxygen_bytes.size() > 1){
	char gamma = (oxygen_counter >= nb_oxygen_bytes / 2.0) ? '1': '0';
	nb_oxygen_bytes = 0;
	oxygen_counter = 0;
	for (std::vector<std::string>::iterator it = oxygen_bytes.begin(); it != oxygen_bytes.end();) {
	    
	    if ((*it)[char_idx - 1] != gamma){
		it = oxygen_bytes.erase(it);
	    }
	    else{
		oxygen_counter += ((*it)[char_idx] == '1') ? 1 : 0;
		nb_oxygen_bytes++;
		++it;
	    }
	}
	char_idx++;
    }
    // CO2
    char_idx = 1;
    int co2_counter = gamma_counter;
    int nb_co2_bytes = nb_bytes;
    while(co2_bytes.size() > 1){
	char gamma = (co2_counter < nb_co2_bytes / 2.0) ? '1': '0';
	nb_co2_bytes = 0;
	co2_counter = 0;
	for (std::vector<std::string>::iterator it = co2_bytes.begin(); it != co2_bytes.end();) {
	    if ((*it)[char_idx - 1] != gamma){
		it = co2_bytes.erase(it);
	    }
	    else{
		co2_counter += ((*it)[char_idx] == '1') ? 1 : 0;
		nb_co2_bytes++;
		++it;
	    }
	}
	char_idx++;
    }
    std::string oxygen_byte = oxygen_bytes[0];
    std::string co2_byte = co2_bytes[0];
    int oxygen = 0;
    int co2 = 0;
    for(unsigned int i = 0 ; i < oxygen_byte.length() ; i++){
	oxygen += ((oxygen_byte[oxygen_byte.length() - 1 - i] - '0') << i);
	co2 += ((co2_byte[co2_byte.length() - 1 - i] - '0') << i);
    }
    return oxygen * co2;
}



int main() {
    int result1 = part1();
    std::cout << "Result 1: " << result1 << std::endl;
    int result2 = part2();
    std::cout << "Result 2: " << result2 << std::endl;
}
