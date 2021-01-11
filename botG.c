#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
pthread_mutex_t m;
int count = 0 ;


void *east (void *arg){
  pthread_mutex_lock(&m);
  count++;
  pthread_mutex_unlock(&m);
}

void *west (void *arg){
  pthread_mutex_lock(&m);
  count++;
  pthread_mutex_unlock(&m);
}

int main() {
  pthread_t tID[4];
  pthread_mutex_init(&m, NULL);
  for(int i=0; i<4;i++){
    pthread_create(&tID[i],NULL,east,NULL);
    pthread_create(&tID[i],NULL,west,NULL);
  }
  for(int i=0; i<4;i++){
    pthread_join(tID[i],NULL);
    pthread_mutex_destroy(&m);
  }
  printf("People inside the garden = %d\n",count);
  return 0;
}
