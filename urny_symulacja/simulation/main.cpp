#include <iostream>
#include <vector>
#include <random>
#include <fstream>

using namespace std;
class Eksperyment{
    public:
        int B = 0;
        int U = 0;
        int L = 0;
        int C = 0;
        int D = 0;
        int DC = 0;
        int puste;
        int przynajmniej_dwa = 0;
        bool koniec = false;
        vector<int> urny;

        explicit Eksperyment(int liczba_urn){
            urny.resize(liczba_urn);
            this->puste=liczba_urn;
        }

        static int getRand(const int& A, const int& B) {
            static random_device randDev;
            static mt19937 twister(randDev());
            static uniform_int_distribution<int> dist;

            dist.param(uniform_int_distribution<int>::param_type(A, B));
            return dist(twister);
        };

        void wrzuc_kule_do_urny(int iteracja){
            int index = getRand(0,urny.size()-1);

            if(urny[index]==0){
                this->puste--;
            }else if(urny[index]==1){
                przynajmniej_dwa++;
                if(this->B==0) this->B=iteracja;
            }

            urny[index]+=1;

            if(iteracja<=urny.size()){
                if(urny[index]>this->L) this->L = urny[index];
                this->U = puste;
            }

            if(puste==0 && this->C==0) this->C = iteracja;

            if(przynajmniej_dwa==urny.size()){
                this->D=iteracja;
                this->DC= this->D - this->C;
                this->koniec = true;
            }
        }

};

void zapis_do_pliku(vector<int> values, const string& nazwa_pliku){
    ofstream f(nazwa_pliku);
    int i = 0;
    for(int n=1000; n<101000;n+=1000){
        f << "n=" << n << "::";
        for(int k=0; k<50; k++){
            f << values[i] << " ";
            i++;
        }
        f << endl;
    }
    f.close();
}

int main(){

    vector<int> B_values;
    vector<int> U_values;
    vector<int> L_values;
    vector<int> C_values;
    vector<int> D_values;
    vector<int> DC_values;

    for(int n=1000; n<101000; n+=1000){
        for(int k=0; k<50; k++){
            Eksperyment eksperyment(n);
            int iteracja = 1;
            while (!eksperyment.koniec) {
                eksperyment.wrzuc_kule_do_urny(iteracja);
                iteracja++;
            }
        B_values.push_back(eksperyment.B);
        U_values.push_back(eksperyment.U);
        L_values.push_back(eksperyment.L);
        C_values.push_back(eksperyment.C);
        D_values.push_back(eksperyment.D);
        DC_values.push_back(eksperyment.DC);
        }
    }

    zapis_do_pliku(B_values,"..//data//B.txt");
    zapis_do_pliku(U_values,"..//data//U.txt");
    zapis_do_pliku(L_values,"..//data//L.txt");
    zapis_do_pliku(C_values,"..//data//C.txt");
    zapis_do_pliku(D_values,"..//data//D.txt");
    zapis_do_pliku(DC_values,"..//data//DC.txt");
}