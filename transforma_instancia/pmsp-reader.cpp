#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <fstream>
#include <limits>

class PmspInstance {
public:
   PmspInstance(const char *fname);
   virtual ~PmspInstance();

   int getNumMachines() const;
   int getNumJobs() const;

   int getProcTime(int job, int machine) const;
   int getSetupTime(int predJob, int succJob, int machine) const;
   int getGijk(int predJob, int succJob, int machine) const;

   const char *getName() const;
   void writeFile(const char *fname) const;
   void writeFormatGLPK(const char *fname) const;

protected:
   const std::string m_name;
   int m_num;
   int m_numMachines, m_numJobs;
   std::vector <std::vector <int>> m_procTimes; // [job][machine]
   std::vector <std::vector <std::vector <int>>> m_setupTimes; // [pred job][succ job][machine]
};

PmspInstance::PmspInstance(const char* fname): m_name(fname) {
   std::ifstream fid(fname);
   if (!fid) {
      std::cout << "Instance file could not be open to read.\n";
      std::abort();
   }

   fid >> m_num >> m_numMachines >> m_numJobs;

   m_procTimes.resize(m_numJobs);
   m_setupTimes.resize(m_numJobs);
   for (int i = 0; i < m_numJobs; ++i) {
      m_procTimes[i].resize(m_numMachines, std::numeric_limits<int>::max());
      m_setupTimes[i].resize(m_numJobs);
      for (int j = 0; j < m_numJobs; ++j) {
         m_setupTimes[i][j].resize(m_numMachines, std::numeric_limits<int>::max());
      }
   }

   for (int i = 0; i < m_numJobs; ++i) {
      for (int j = 0; j < m_numMachines; ++j) {
         fid >> m_procTimes[i][j];
      }
   }

   for (int k = 0; k < m_numMachines; ++k) {
      for (int i = 0; i < m_numJobs; ++i) {
         for (int j = 0; j < m_numJobs; ++j) {
            fid >> m_setupTimes[i][j][k];
         }
      }
   }

}

PmspInstance::~PmspInstance() {
   // Empty
}

int PmspInstance::getNumMachines() const {
   return m_numMachines;
}

int PmspInstance::getNumJobs() const {
   return m_numJobs;
}

int PmspInstance::getProcTime(int job, int machine) const {
   return m_procTimes[job][machine];
}

int PmspInstance::getSetupTime(int predJob, int succJob, int machine) const {
   return m_setupTimes[predJob][succJob][machine];
}

int PmspInstance::getGijk(int predJob, int succJob, int machine) const {
   return getProcTime(succJob, machine) + getSetupTime(predJob, succJob, machine);
}

const char *PmspInstance::getName() const {
   return m_name.c_str();
}

void PmspInstance::writeFile(const char* fname) const {
   std::ofstream fid(fname);
   if (!fid) {
      std::cout << "Output file could not be open to write.\n";
      std::abort();
   }

   fid << m_num << '\n' << m_numMachines << '\n' << m_numJobs << "\n\n";

   for (int i = 0; i < m_numJobs; ++i) {
      for (int j = 0; j < m_numMachines; ++j) {
         fid << m_procTimes[i][j] << ' ';
      }
      fid << '\n';
   }
   fid << "\n";

   for (int k = 0; k < m_numMachines; ++k) {
      for (int i = 0; i < m_numJobs; ++i) {
         for (int j = 0; j < m_numJobs; ++j) {
            fid << m_setupTimes[i][j][k] << ' ';
         }
         fid << "\n";
      }
      fid << "\n";
   }
}


void PmspInstance::writeFormatGLPK(const char* fname) const
{
    std::ofstream fid(fname);
    if (!fid)
    {
        std::cout << "Output file could not be open to write.\n";
        std::abort();
    }
	fid << "data;"<<"\n";
    // Monta set I;
    fid << "set J :=";
    for (int i=1; i<=m_numJobs; i++)
    {
        fid << " " << i ;
    }
    fid << ";" << "\n";

    // Monta set J;
    fid << "set I :=";
    for (int i=0; i<=m_numJobs; i++)
    {
        fid << " " << i ;
    }
    fid << ";" << "\n";

     // Monta set K;
    fid << "set K :=";
    for (int i=1; i<=m_numMachines; i++)
    {
        fid << " " << i ;
    }
    fid << ";" << "\n";

    fid <<"param V := 9999;" << "\n";

    fid << "\n";
    fid << "param G :=";
    // param G {i in I, j in J, k in K};


    for(int i=-1; i < m_numJobs; i++)
    {
        for(int j=-1; j<m_numJobs; j++)
        {
            for(int k=0; k<m_numMachines; k++)
            {
				if(j==-1 && i==-1){
				}
				else if(i==-1){
					fid <<"\n\t" << i+1 << " " << j+1 << " " << k+1 << " " << getProcTime(j,k);
				}
                else if(j==-1){
                    fid <<"\n\t" << i+1 << " " << j+1 << " " << k+1 << " " << getProcTime(i,k);
                }else
                    fid <<"\n\t" << i+1 << " " << j+1 << " " << k+1 << " " << getGijk(i,j,k);
            }
        }
    }
    fid << ";" << "\n\n";
	fid <<"end;"<<"\n\n";

}


int main(int argc, char **argv) {
   if (argc != 2) {
      std::cout << "Usage: " << argv[0] << " <instance file>\n";
      return EXIT_FAILURE;
   }
   std::cout<<"Starting\n";
   PmspInstance inst(argv[1]);
   std::cout<<"Read\n";
   inst.writeFormatGLPK("pmsp.dat");
   std::cout<<"Written\n";
   return EXIT_SUCCESS;
}
