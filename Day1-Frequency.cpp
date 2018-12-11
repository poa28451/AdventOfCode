#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
using namespace std;

int main(){
    int sum = 0;
    int change = 0;
    list<int> changeList;
    list<int> freqList;
    list<int>::iterator dupFreq, freqChange;
    ifstream file;
    bool isDup = false;

    freqList.push_front(0); // 0 frequency is always on the list.
    file.open("Day1-input.txt");
    if(!file){ //Check if the file is successfully opened.
        cout << "Cannot open input file.";
        return(1);
    }

    //First, read all the freq changes into the list
    while(file >> change){
        changeList.push_back(change);
    }
    file.close();

    while(!isDup){
        freqChange = changeList.begin();
        while(freqChange != changeList.end()){
            sum += *freqChange; // Change the frequency
            freqChange++;

            //Try to find if the most recent frequency is duplicated
            dupFreq = find(freqList.begin(), freqList.end(), sum);
            if(dupFreq != freqList.end()){ //If it's duplicated
                cout << "Freq " << sum << " is duplicated" << endl;
                isDup = true;
                break;
            } else{
                //If it's the unique frequency, remember the number
                freqList.push_back(sum);
            }

        }
    }
    return 0;
}
