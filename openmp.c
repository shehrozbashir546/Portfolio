#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
int count = 5 ;

void WestEntrance() {
  count++;
  printf("Person #%d has entered\n", omp_get_thread_num());

}

void EastEntrance() {
  count++;
  printf("Person #%d has entered\n", omp_get_thread_num());

}



int main() {

    #pragma omp parallel sections
        {
          for (int i = 0; i < 10; i++) {
            #pragma omp section
            EastEntrance();
            #pragma omp section
            WestEntrance();
          }

        }
        printf("The count is %d\n",count);

    return 0;
  }
