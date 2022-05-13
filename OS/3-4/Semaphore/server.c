#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>

#define BUF_SIZE 750000
#define PERM 0777
#define PROJECT_ID 16

static struct sembuf catch_resources[1] = {{0, -1, 0 }};
static struct sembuf free_resources[1] = {{0, 2, 0 }};
struct semid_ds semid_ds;
union semun {
    int val;
    struct semid_ds *buf;
    ushort *array;
} arg;
typedef struct mem_msg {
    int segment;
    char buff[BUF_SIZE];
} message;

int main()
{
    time_t rawtime= time(0) / 60 * 60;
    message* msgptr;

    open("/tmp/lab16",O_CREAT | O_WRONLY | O_TRUNC ,S_IRUSR | S_IWUSR );// 0400 | 0200, флаги просто потому что
    key_t ipckey = ftok("/tmp/lab16", PROJECT_ID);
    int shmid = shmget(ipckey, sizeof(message), PERM | IPC_CREAT | IPC_EXCL);
    int semid = semget(ipckey, 1, PERM | IPC_CREAT |  IPC_EXCL);

    semop(semid, &catch_resources[0], 1);
    msgptr = (message*)shmat(shmid, 0, 0);
    u_int64_t buf_count = strlen(msgptr->buff);
    char buf_copy[BUF_SIZE];
    memcpy(buf_copy, msgptr->buff, BUF_SIZE);
    memset(msgptr->buff, 0, BUF_SIZE);
    struct stat buf;
    char *pch = strtok(buf_copy, "\n");
    int msg_len=0;
    while (pch != NULL) //пока есть лексемы
    {
        stat(pch, &buf);
        msg_len+=sprintf(msgptr->buff + msg_len,"%s %o\n", pch, buf.st_mode);
        pch = strtok(NULL, "\n");
    }

    memset(buf_copy, 0, BUF_SIZE);
    semop(semid, &free_resources[0], 1);
    return 0;
}

