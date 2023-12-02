#include <aoc.h>

vector<string> getFile(string fileName) {
    vector<string> file; 
    ifstream fileStream(fileName);
    string line;
    if (!fileStream.is_open()) {
        cout << "Could not open file " << fileName << endl;
        return vector<string>();
    }
    while (getline(fileStream, line)) {
        cout << line << endl;
        file.push_back(line);
    }
    return file;
}