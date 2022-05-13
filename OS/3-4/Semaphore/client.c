#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BUF_SIZE 65536
#define PROJECT_ID 16

static struct sembuf free_resources[1] = {{ 0, 1, 0 }};
static struct sembuf catch_resources[1] = {{ 0, -2, 0 }};
typedef struct mem_msg {
    int segment;
    char buff[BUF_SIZE];
} message;

int main()
{
    key_t ipckey;
    message *msgptr;
    int shmid, semid;

    while((ipckey = ftok("/tmp/lab6", PROJECT_ID))<0)
    {
        printf("Temp file is not created. Waiting\n");
        sleep(3);
    }
    while((shmid = shmget(ipckey, 0, 0))<0)
    {
        printf("Shared memory segment is not created. Waiting\n");
        sleep(3);
    }
    while((semid = semget(ipckey, 0, 0))<0)
    {
        printf("Semaphore is not created. Waiting\n");
        sleep(3);
    }

    msgptr = (message*)shmat(shmid, 0, 0);

    FILE *shell = popen("find / -user $(whoami) 2>/dev/null", "r");
    char buf[BUF_SIZE];
    fread(buf, 1, BUF_SIZE, shell);
    pclose(shell);

    sprintf(msgptr->buff,"%s",buf);
    shmdt(msgptr);
    semop(semid, &free_resources[0], 1);

    semop(semid, &catch_resources[0], 1);
    msgptr = (message*)shmat(shmid, 0, 0);
    printf("%s",msgptr->buff);
    shmdt(msgptr);
    
    struct shmid_ds ds;
    shmctl(shmid, IPC_STAT, &ds);

    printf("\nLast connection to shared memory was in %s\n",ctime(&ds.shm_atime));

    shmctl(shmid, IPC_RMID, 0);
    semctl(semid, 0, IPC_RMID);
    return 0;
}