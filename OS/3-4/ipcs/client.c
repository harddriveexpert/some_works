#include <stdio.h>
#include <sys/msg.h>
#include <stdlib.h>
#include <string.h>

struct
{
    long type;
    char text[8192];
} message, msg2;

struct msqid_ds ds;

int main()
{
    int mq_id;
    creat("/tmp/laba4",2);
    key_t key = ftok("/tmp/laba4", 161);
    if((mq_id = msgget(key, IPC_CREAT | 0666)) == -1)
    {
        printf("Message queue can't been created\n");
        return -1;
    }
    char buf[8192];
    FILE* c_sources = popen("file * | grep \"C source\" | awk '{print $1;}'", "r");
    fread(buf, 1, 8192, c_sources);
    message.type=1;
    memset(message.text, 0, 8192);
    strcpy(message.text, buf);
    msgsnd(mq_id, &message, strlen(message.text), 0);

    msgrcv(mq_id, &msg2, 8192, 4, 0);
    long num=strtol(msg2.text,NULL,10);
    for (int i = 0; i < num; ++i) {
        msgrcv(mq_id, &msg2, 8192, 5, 0);
        printf("%s\n",msg2.text);
    }
    msgctl(mq_id, IPC_RMID, 0);
    unlink("/tmp/laba4");
    return 0;
}