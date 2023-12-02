#include <aoc.h>
#include <regex>

vector<string> getFile(string fileName)
{
    vector<string> file;
    ifstream fileStream(fileName);
    string line;
    if (!fileStream.is_open())
    {
        cout << "Could not open file " << fileName << endl;
        return vector<string>();
    }
    while (getline(fileStream, line))
    {
        file.push_back(line);
    }
    return file;
}

void part1()
{
    vector<string> file = getFile("input.txt");
    int sum = 0;
    for (string line : file)
    {
        vector<int> nums;
        for (int i = 0; i < line.length(); i++)
        {
            if (isdigit(line[i]))
            {
                nums.push_back(line[i] - '0');
            }
        }
        int first = nums[0];
        int right = nums.back();
        string composed = to_string(first) + to_string(right);
        int composedInt = stoi(composed);
        sum += composedInt;
    }
    cout << "Part 1: " << sum << endl;
}



static const map<string, int> m{ {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};

string replace(const string& str) {
    string ergebnis = "";
    string temp = "";

    for (int i = 0; i < str.length(); i++)
    {
        char letter = str[i];
        if (isdigit(letter))
        {
            ergebnis += letter;
        }
        else if (isalpha(letter))
        {
            temp += letter;
        }
        else
        {
            if (temp != "")
            {
                ergebnis += to_string(m.at(temp));
                temp = "";
            }
        }
    }
    return ergebnis;
}

void part2()
{
    vector<string> file = getFile("test2.txt");
    int sum = 0;
    for (auto line : file)
    {

        vector<int> nums;
        for (int i = 0; i < line.length(); i++)
        {

            // cout << line << endl;

            char letter = line[i];
            if (isdigit(letter))
            {
                nums.push_back(letter - '0');
            }
        }
        int first = nums[0];
        int right = nums.back();
        string composed = to_string(first) + to_string(right);
        int composedInt = stoi(composed);
        sum += composedInt;
    }
    cout << "Part 2 " << sum << endl;
}

int main()
{
    part2();
    return 0;
}