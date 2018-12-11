#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
using namespace std;

int main(){
    ifstream file;
    string boxID;
    int twoTimes = 0, threeTimes = 0;

    file.open("Day2-input.txt");
    if(!file){
        cout <<  "Failed to open the file." << endl;
        return 1;
    }

    while(file >> boxID){
        char letter;
        bool twoCounted = false, threeCounted = false; //These two vars are for checking that the two and three occurrences are already found or not
        for(int i=0; i<boxID.size(); i++){
            if(twoCounted && threeCounted) break; //If all type of occurrences is found, drop the count for this ID

            letter =  boxID[i];
            int occur = count(boxID.begin(), boxID.end(), letter); //Count  the total occurrence for this letter
            if(occur == 2 && !twoCounted){ //If it appears two times and has not been found yet
                twoTimes++;
                twoCounted = true; //Mark the two occurrences as found
            } else if(occur == 3 && !threeCounted){ //If it appears three times and has not been found yet
                threeTimes++;
                threeCounted = true; //Mark the three occurrences as found
            }
        }
    }
    file.close();
    cout << twoTimes << " x " << threeTimes << " = " << twoTimes*threeTimes << endl;
    return 0;
}
