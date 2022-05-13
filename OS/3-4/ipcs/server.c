#include <stdio.h>
#include <sys/msg.h>
#include <string.h>
#include <time.h>

struct
{
    long type;
    char text[8192];
} recieved,send;
struct msqid_ds ds;

int main() {
    int mq_id;
    key_t key = ftok("/tmp/laba4", 161);
    if (key == -1) {
        printf("No messages\n");
        return -1;
    }
    mq_id = msgget(key, 0);
    if (mq_id == -1) {
        printf("I have no idea what is going on\n");
        return -1;
    }

    int msg_count=0;
    msgrcv(mq_id, &recieved, sizeof(recieved.text), 0, 0);
    char* pch = strtok(recieved.text, "\n");
    char* comm;
    char buf[2];
    while(pch!= NULL)
    {
        size_t length= strlen(pch);
        pch[length-1]=0;
        asprintf(&comm, "grep -qE 'while|for\\(|for \\(' %s; echo $? ",pch);
        FILE* cycle= popen(comm,"r");
        fread(buf,1,2,cycle);
        send.type=5;
        if(buf[0]=='0')
        {
            printf("%s with cycle\n",pch);
            strcpy(send.text, pch);
            int s=msgsnd(mq_id, &send, strlen(send.text), IPC_NOWAIT );
            if(s==0)
            {
                msg_count++;
            }
        }
        pch=strtok(NULL, "\n");
    }
    char s_count[33];
    sprintf(s_count,"%d",msg_count);
    strcpy(send.text, s_count);
    send.type=4;
    msgsnd(mq_id, &send, strlen(send.text), IPC_NOWAIT );
    msgctl(mq_id, IPC_STAT, &ds);
    printf("Last recieved was read: %s\n", asctime(gmtime(&ds.msg_rtime)));
    return 0;
}